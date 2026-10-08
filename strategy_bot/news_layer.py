"""News risk layer (config `news_layer`): a filter that can only REDUCE exposure, never add. Shadow mode first.

Sources (every 15 min, in a background thread, so news / LLM problems never delay or block trading):
  CryptoPanic API (optional, CRYPTOPANIC_TOKEN), CoinDesk and Cointelegraph RSS, Crypto Fear & Greed (alternative.me),
  and the static calendar data/events.csv (CPI / FOMC decisions).
Headlines are deduplicated (normalised-text hash) and kept only if they mention a coin of the active universe or macro.
Kept items are classified by an LLM (Anthropic Messages API, pinned model, temperature 0, strict JSON); a response that
fails validation is skipped. The API key comes from NEWS_LLM_API_KEY (env file) and is never logged. A daily cost cap
(from the API's reported token usage) stops classification for the rest of the UTC day.

Deterministic rules (config):
  veto       severity >= 4, direction negative, confidence >= 0.7, event_type in {hack, exploit, delisting,
             regulatory_action, depeg} -> that coin's target 0 (close) for 72h
  calendar   a CPI or FOMC decision within the next 24h, or less than 4h ago -> all targets x 0.7
  sentiment  Fear & Greed >= 85 or <= 10 (value at most 48h old) -> all targets x 0.8
Rules combine multiplicatively; a vetoed coin is 0. adjust() guarantees |new weight| <= |old weight| for every coin.

shadow: true  -> trading is unchanged; what the rules WOULD do is logged to <logs>/news_shadow.jsonl
shadow: false -> the reduced targets are traded (not enabled anywhere yet)
"""

from __future__ import annotations

import hashlib
import json
import logging
import os
import re
import threading
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any, Callable

import pandas as pd
import requests

from infra import append_log, utc_iso, write_json_atomic

log = logging.getLogger("strategy_bot.news")

EVENT_TYPES = ["hack", "exploit", "delisting", "regulatory_action", "depeg", "outage", "upgrade", "etf", "partnership",
               "macro", "other"]
VETO_TYPES = {"hack", "exploit", "delisting", "regulatory_action", "depeg"}
DIRECTIONS = {"negative", "positive", "neutral"}
NAMES = {"BTC": ["bitcoin", "btc"], "ETH": ["ethereum", "ether", "eth"], "SOL": ["solana", "sol"],
         "BNB": ["bnb", "binance coin", "bnb chain"], "XRP": ["xrp", "ripple"], "ADA": ["cardano", "ada"],
         "DOGE": ["dogecoin", "doge"], "AVAX": ["avalanche", "avax"], "LINK": ["chainlink", "link"],
         "DOT": ["polkadot", "dot"]}
MACRO = ["fed", "fomc", "cpi", "inflation", "powell", "interest rate", "rate cut", "rate hike", "sec ", "tariff",
         "treasury", "recession", "jobs report", "nonfarm", "etf"]
DEFAULTS: dict[str, Any] = {
    "enabled": False, "shadow": True, "poll_min": 15, "timeout_s": 8, "max_items_per_poll": 20,
    "rss": ["https://www.coindesk.com/arc/outboundfeeds/rss/", "https://cointelegraph.com/rss"],
    "cryptopanic_url": "https://cryptopanic.com/api/developer/v2/posts/",
    "fng_url": "https://api.alternative.me/fng/?limit=1",
    "calendar": "data/events.csv", "calendar_types": ["CPI", "FOMC_DECISION"],
    "llm_url": "https://api.anthropic.com/v1/messages", "llm_model": "claude-haiku-4-5-20251001",
    "llm_max_tokens": 300, "price_in_per_mtok": 1.0, "price_out_per_mtok": 5.0, "daily_cost_cap_usd": 1.0,
    "veto_hours": 72, "veto_min_severity": 4, "veto_min_confidence": 0.7,
    "calendar_before_h": 24, "calendar_after_h": 4, "calendar_mult": 0.7,
    "fng_high": 85, "fng_low": 10, "fng_mult": 0.8, "fng_max_age_h": 48,
}
PROMPT = """You classify one crypto news headline for a trading risk filter. Answer with ONE JSON object and nothing else:
{"coin": <ticker of the main coin affected, one of %s, or "MACRO" or null>,
 "event_type": <one of %s>,
 "direction": <"negative", "positive" or "neutral" for that coin's price>,
 "severity": <integer 1-5, 5 = existential for the coin>,
 "confidence": <number 0-1>,
 "reason": <at most 25 words>}
Headline: %s
Source: %s"""


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9 ]", "", text.lower()).strip()


def validate(d: Any, tickers: list[str]) -> dict | None:
    """Strict check of the LLM JSON; None if anything is off."""
    if not isinstance(d, dict):
        return None
    try:
        coin = d.get("coin")
        if coin is not None and coin != "MACRO" and coin not in tickers:
            return None
        if d["event_type"] not in EVENT_TYPES or d["direction"] not in DIRECTIONS:
            return None
        sev = d["severity"]
        if isinstance(sev, bool) or not isinstance(sev, int) or not 1 <= sev <= 5:
            return None
        conf = float(d["confidence"])
        if not 0 <= conf <= 1:
            return None
        reason = str(d.get("reason", ""))[:300]
    except (KeyError, TypeError, ValueError):
        return None
    return {"coin": coin, "event_type": d["event_type"], "direction": d["direction"], "severity": sev,
            "confidence": conf, "reason": reason}


class NewsLayer:
    def __init__(self, cfg: dict[str, Any], pairs: list[str], log_dir: Path, state_dir: Path, base_dir: Path,
                 http: Any = requests, clock: Callable[[], pd.Timestamp] | None = None,
                 api_key: str | None = None, cp_token: str | None = None) -> None:
        self.c = {**DEFAULTS, **(cfg or {})}
        self.pairs = list(pairs)
        self.tickers = sorted({p.split("/")[0] for p in pairs})
        self.log_path = Path(log_dir) / "news_shadow.jsonl"
        self.err_path = Path(log_dir) / "errors.jsonl"
        self.state_path = Path(state_dir) / "news_state.json"
        self.http = http
        self.clock = clock or (lambda: pd.Timestamp.now(tz="UTC"))
        self._key = api_key if api_key is not None else os.environ.get("NEWS_LLM_API_KEY")
        self._cp = cp_token if cp_token is not None else os.environ.get("CRYPTOPANIC_TOKEN")
        self.lock = threading.Lock()
        self.thread: threading.Thread | None = None
        self.last_refresh: pd.Timestamp | None = None
        st = {}
        if self.state_path.exists():
            try:
                st = json.loads(self.state_path.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                st = {}
        self.seen: list[str] = list(st.get("seen", []))[-3000:]
        self.vetoes: dict[str, dict] = dict(st.get("vetoes", {}))
        self.fng: dict | None = st.get("fng")
        self.cost: dict = st.get("cost", {"day": None, "usd": 0.0})
        self.day_stats: dict = st.get("day_stats", {})
        cal = Path(base_dir) / self.c["calendar"]
        self.events = pd.DatetimeIndex([])
        if cal.exists():
            df = pd.read_csv(cal)
            self.events = pd.DatetimeIndex(pd.to_datetime(df.loc[df["type"].isin(self.c["calendar_types"]), "time_utc"],
                                                          utc=True)).sort_values()
        if not self._key:
            log.warning("news_layer: NEWS_LLM_API_KEY not set; headlines are fetched but not classified")

    # ----- logging --------------------------------------------------------- #
    def _log(self, rec: dict) -> None:
        append_log({"time": str(self.clock()), "ts": int(time.time() * 1000), **rec}, self.log_path)

    def _err(self, where: str, exc: BaseException | str) -> None:
        msg = str(exc)
        if self._key:
            msg = msg.replace(self._key, "***")
        append_log({"time": utc_iso(), "ts": int(time.time() * 1000), "where": f"news:{where}",
                    "type": type(exc).__name__ if isinstance(exc, BaseException) else "NewsError", "message": msg[:300]},
                   self.err_path)

    def _save(self) -> None:
        write_json_atomic(self.state_path, {"seen": self.seen[-3000:], "vetoes": self.vetoes, "fng": self.fng,
                                            "cost": self.cost, "day_stats": self.day_stats})

    # ----- sources --------------------------------------------------------- #
    def _get(self, url: str, **kw) -> Any:
        return self.http.get(url, timeout=float(self.c["timeout_s"]), headers={"User-Agent": "strategy_bot-news/1.0"}, **kw)

    def fetch_rss(self, url: str) -> list[dict]:
        r = self._get(url)
        r.raise_for_status()
        root = ET.fromstring(r.content)
        out = []
        for it in root.iter("item"):
            title = (it.findtext("title") or "").strip()
            if title:
                out.append({"headline": title, "source": url.split("/")[2], "url": (it.findtext("link") or "").strip(),
                            "published": (it.findtext("pubDate") or "").strip()})
        return out

    def fetch_cryptopanic(self) -> list[dict]:
        if not self._cp:
            return []
        r = self._get(self.c["cryptopanic_url"], params={"auth_token": self._cp, "public": "true",
                                                         "currencies": ",".join(self.tickers)})
        r.raise_for_status()
        out = []
        for p in (r.json() or {}).get("results", []) or []:
            title = (p.get("title") or "").strip()
            if title:
                out.append({"headline": title, "source": "cryptopanic", "url": p.get("url") or "",
                            "published": p.get("published_at") or "",
                            "currencies": [c.get("code") for c in (p.get("currencies") or []) if isinstance(c, dict)]})
        return out

    def fetch_fng(self) -> None:
        r = self._get(self.c["fng_url"])
        r.raise_for_status()
        d = (r.json() or {}).get("data", [])[0]
        self.fng = {"value": int(d["value"]), "label": d.get("value_classification"),
                    "time": str(pd.Timestamp(int(d["timestamp"]), unit="s", tz="UTC"))}

    def relevant(self, item: dict) -> bool:
        if any(c in self.tickers for c in item.get("currencies") or []):
            return True
        t = " " + norm(item["headline"]) + " "
        if any(f" {n} " in t for tk in self.tickers for n in NAMES.get(tk, [tk.lower()])):
            return True
        return any(m.strip() in t for m in MACRO)

    # ----- LLM --------------------------------------------------------------- #
    def classify(self, item: dict) -> dict | None:
        if not self._key:
            return None
        day = str(self.clock().date())
        if self.cost.get("day") != day:
            self.cost = {"day": day, "usd": 0.0}
        if self.cost["usd"] >= float(self.c["daily_cost_cap_usd"]):
            self._log({"event": "cost_cap", "headline": item["headline"], "cost_usd": round(self.cost["usd"], 4)})
            return None
        body = {"model": self.c["llm_model"], "max_tokens": int(self.c["llm_max_tokens"]), "temperature": 0,
                "messages": [{"role": "user", "content": PROMPT % (self.tickers, EVENT_TYPES, item["headline"],
                                                                   item["source"])}]}
        try:
            r = self.http.post(self.c["llm_url"], json=body, timeout=float(self.c["timeout_s"]) * 2,
                               headers={"x-api-key": self._key, "anthropic-version": "2023-06-01",
                                        "content-type": "application/json"})
            r.raise_for_status()
            resp = r.json()
        except Exception as exc:                                     # never let it propagate
            self._err("llm", exc)
            return None
        u = resp.get("usage") or {}
        self.cost["usd"] += (u.get("input_tokens", 0) * float(self.c["price_in_per_mtok"])
                             + u.get("output_tokens", 0) * float(self.c["price_out_per_mtok"])) / 1e6
        text = "".join(b.get("text", "") for b in resp.get("content", []) if isinstance(b, dict))
        m = re.search(r"\{.*\}", text, re.S)
        try:
            out = validate(json.loads(m.group(0)) if m else None, self.tickers)
        except ValueError:
            out = None
        if out is None:
            self._log({"event": "llm_invalid", "headline": item["headline"], "source": item["source"],
                       "raw": text[:300]})
        return out

    # ----- refresh ------------------------------------------------------------ #
    def maybe_refresh(self, now: pd.Timestamp) -> None:
        """Start a background refresh if due (non-blocking; at most one at a time)."""
        if self.thread is not None and self.thread.is_alive():
            return
        if self.last_refresh is not None and now - self.last_refresh < pd.Timedelta(minutes=float(self.c["poll_min"])):
            return
        self.last_refresh = now
        self.thread = threading.Thread(target=self._safe_refresh, args=(now,), daemon=True)
        self.thread.start()

    def _safe_refresh(self, now: pd.Timestamp) -> None:
        try:
            self.refresh(now)
        except Exception as exc:                                     # the trading loop must never see this
            self._err("refresh", exc)

    def refresh(self, now: pd.Timestamp) -> None:
        items: list[dict] = []
        for name, fn in [("cryptopanic", self.fetch_cryptopanic)] + [(u, (lambda u=u: self.fetch_rss(u))) for u in self.c["rss"]]:
            try:
                items += fn()
            except Exception as exc:
                self._err(f"source:{name}", exc)
        try:
            self.fetch_fng()
        except Exception as exc:
            self._err("source:fng", exc)
        new = []
        for it in items:
            h = hashlib.sha1(norm(it["headline"]).encode()).hexdigest()[:16]
            if h in self.seen:
                continue
            self.seen.append(h)
            if self.relevant(it):
                new.append(it)
        ds = self.day_stats.setdefault(str(now.date()), {"fetched": 0, "relevant": 0, "classified": 0, "vetoes": 0})
        ds["fetched"] += len(items)
        ds["relevant"] += len(new)
        for it in new[: int(self.c["max_items_per_poll"])]:
            out = self.classify(it)
            if out is None:
                continue
            ds["classified"] += 1
            rule = self._veto_rule(out)
            with self.lock:
                if rule:
                    pair = f"{out['coin']}/USD"
                    until = now + pd.Timedelta(hours=float(self.c["veto_hours"]))
                    self.vetoes[pair] = {"until": str(until), "headline": it["headline"], "event_type": out["event_type"]}
                    ds["vetoes"] += 1
            self._log({"event": "item", "headline": it["headline"], "source": it["source"], "url": it["url"],
                       "llm": out, "rule": rule})
        with self.lock:
            self._save()

    def _veto_rule(self, o: dict) -> str | None:
        if (o["coin"] not in (None, "MACRO") and f"{o['coin']}/USD" in self.pairs and o["event_type"] in VETO_TYPES
                and o["direction"] == "negative" and o["severity"] >= int(self.c["veto_min_severity"])
                and o["confidence"] >= float(self.c["veto_min_confidence"])):
            return f"veto {o['coin']}/USD {int(self.c['veto_hours'])}h ({o['event_type']}, severity {o['severity']})"
        return None

    # ----- rules ------------------------------------------------------------ #
    def adjust(self, target: dict[str, float], now: pd.Timestamp) -> tuple[dict[str, float], dict]:
        """Reduced targets and the rules that fired. Never increases |weight|, never flips a sign."""
        fired, mult = [], 1.0
        ev = self.events
        if len(ev):
            near = ev[(ev > now - pd.Timedelta(hours=float(self.c["calendar_after_h"])))
                      & (ev <= now + pd.Timedelta(hours=float(self.c["calendar_before_h"])))]
            if len(near):
                mult *= float(self.c["calendar_mult"])
                fired.append(f"calendar x{self.c['calendar_mult']} (event {near[0]:%Y-%m-%d %H:%M})")
        f = self.fng
        if f and now - pd.Timestamp(f["time"]) <= pd.Timedelta(hours=float(self.c["fng_max_age_h"])):
            if f["value"] >= int(self.c["fng_high"]) or f["value"] <= int(self.c["fng_low"]):
                mult *= float(self.c["fng_mult"])
                fired.append(f"fear&greed {f['value']} x{self.c['fng_mult']}")
        with self.lock:
            vetoed = {p for p, v in self.vetoes.items() if pd.Timestamp(v["until"]) > now}
        out = {}
        for p, w in target.items():
            nw = 0.0 if p in vetoed else w * min(mult, 1.0)
            assert abs(nw) <= abs(w) + 1e-15 and nw * w >= 0, "news layer may only reduce exposure"
            out[p] = nw
        for p in sorted(vetoed & set(target)):
            fired.append(f"veto {p} until {self.vetoes[p]['until'][:16]} ({self.vetoes[p]['event_type']})")
        return out, {"mult": round(mult, 4), "vetoed": sorted(vetoed), "fired": fired}
