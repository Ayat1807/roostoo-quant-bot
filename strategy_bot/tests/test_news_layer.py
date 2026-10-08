"""News risk layer (news_layer.py), offline with mocked feeds and a mocked LLM.

    python -m tests.test_news_layer

1. Validation and relevance: strict JSON schema (bad types, unknown coin, bool severity rejected); headline filter.
2. Fake hack headline -> veto logged (72h), the coin's would-be target 0; in SHADOW mode a 10-day replay places exactly the
   same orders as the same bot without the layer, and the shadow log shows the would-be change.
3. LLM JSON failure -> item skipped, logged as llm_invalid, no veto, no exception.
4. Outage (every source and the LLM time out) -> refresh returns, errors logged, trading steps run normally.
5. Cost cap -> once the day's cost reaches the cap, items are not classified (cost_cap logged).
6. Calendar (CPI / FOMC within 24h or < 4h after) x0.7; Fear & Greed >= 85 / <= 10 x0.8; stale F&G ignored.
7. Reduce-only: on random targets |new| <= |old| and no sign flip.
8. The API key never appears in any log (incl. an exception message that contains it); maybe_refresh does not block.
9. Fingerprint unchanged by the layer; heartbeat and status.py show it.
"""

from __future__ import annotations

import copy
import json
import shutil
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
import requests

from bot import StrategyBot, load_config
from news_layer import NewsLayer, validate
from tests.hist_data import load_closes

HERE = Path(__file__).resolve().parent.parent
OUT = HERE / ".cache" / "news_layer"
KEY = "sk-test-NEVER-LOG-THIS-KEY-1234567890"
PAIRS = ["BTC/USD", "ETH/USD", "SOL/USD", "BNB/USD", "XRP/USD", "ADA/USD", "DOGE/USD", "AVAX/USD", "LINK/USD", "DOT/USD"]
HACK = "Solana DeFi bridge suffers $300M exploit, SOL plunges"


def rss(*titles: str) -> bytes:
    items = "".join(f"<item><title>{t}</title><link>https://example.com/{i}</link><pubDate>now</pubDate></item>"
                    for i, t in enumerate(titles))
    return f'<?xml version="1.0"?><rss><channel>{items}</channel></rss>'.encode()


class Resp:
    def __init__(self, content=b"", js=None, status=200):
        self.content, self._js, self.status_code = content, js, status

    def json(self):
        return self._js

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(f"{self.status_code}")


class FakeHTTP:
    """RSS / F&G / CryptoPanic / LLM mocks. llm(headline) -> text; outage -> every call times out."""

    def __init__(self, titles=(), fng=50, fng_time=None, llm=None, outage=False, usage=(200, 60), delay=0.0):
        self.titles, self.fng, self.fng_time, self.llm = list(titles), fng, fng_time, llm
        self.outage, self.usage, self.delay, self.posts = outage, usage, delay, 0

    def get(self, url, timeout=None, headers=None, params=None):
        time.sleep(self.delay)
        if self.outage:
            raise requests.Timeout(f"simulated timeout {url}")
        if "alternative.me" in url:
            ts = int((self.fng_time or pd.Timestamp.now(tz="UTC")).timestamp())
            return Resp(js={"data": [{"value": str(self.fng), "value_classification": "x", "timestamp": str(ts)}]})
        if "cryptopanic" in url:
            return Resp(js={"results": []})
        return Resp(content=rss(*self.titles))

    def post(self, url, json=None, timeout=None, headers=None):
        self.posts += 1
        if self.outage:
            raise requests.Timeout(f"simulated LLM timeout with key {headers.get('x-api-key')}")
        head = json["messages"][0]["content"].split("Headline: ")[1].split("\n")[0]
        text = self.llm(head) if self.llm else "{}"
        return Resp(js={"content": [{"type": "text", "text": text}],
                        "usage": {"input_tokens": self.usage[0], "output_tokens": self.usage[1]}})


def llm_ok(head: str) -> str:
    if "exploit" in head:
        return json.dumps({"coin": "SOL", "event_type": "exploit", "direction": "negative", "severity": 5,
                           "confidence": 0.9, "reason": "bridge exploit"})
    return json.dumps({"coin": "BTC", "event_type": "other", "direction": "neutral", "severity": 1,
                       "confidence": 0.6, "reason": "routine"})


def layer(tag: str, http: FakeHTTP, now: pd.Timestamp, cfg: dict | None = None, key: str | None = KEY) -> NewsLayer:
    d = OUT / tag
    shutil.rmtree(d, ignore_errors=True)
    return NewsLayer({"enabled": True, "shadow": True, "rss": ["https://rss.example.com/feed"], **(cfg or {})}, PAIRS,
                     d / "logs", d / "state", HERE, http=http, clock=lambda: now, api_key=key, cp_token=None)


def read(nl: NewsLayer, name: str = "news_shadow") -> list[dict]:
    p = nl.log_path if name == "news_shadow" else nl.err_path
    return [json.loads(x) for x in p.read_text().splitlines()] if p.exists() else []


def report(title: str, checks: dict) -> bool:
    print(f"\n== {title}")
    for k, v in checks.items():
        print(f"   [{'PASS' if v else 'FAIL'}] {k}")
    return all(checks.values())


def test_units() -> bool:
    t = ["BTC", "SOL"]
    good = {"coin": "SOL", "event_type": "hack", "direction": "negative", "severity": 4, "confidence": 0.8, "reason": "x"}
    now = pd.Timestamp("2026-10-08 12:00", tz="UTC")
    nl = layer("units", FakeHTTP(), now)
    return report("validation and relevance", {
        "valid JSON accepted": validate(good, t) is not None,
        "severity as bool rejected": validate({**good, "severity": True}, t) is None,
        "severity out of range rejected": validate({**good, "severity": 6}, t) is None,
        "unknown event_type rejected": validate({**good, "event_type": "rugpull"}, t) is None,
        "coin outside the universe rejected": validate({**good, "coin": "PEPE"}, t) is None,
        "confidence > 1 rejected": validate({**good, "confidence": 1.5}, t) is None,
        "missing field rejected": validate({k: v for k, v in good.items() if k != "direction"}, t) is None,
        "headline about Solana kept": nl.relevant({"headline": HACK}),
        "macro headline (CPI) kept": nl.relevant({"headline": "US CPI comes in hot, Fed cut odds fall"}),
        "unrelated headline dropped": not nl.relevant({"headline": "New NFT collection sells out in minutes"}),
    })


def test_veto_and_rules() -> bool:
    now = pd.Timestamp("2026-10-08 12:00", tz="UTC")
    http = FakeHTTP(titles=[HACK, "Bitcoin holds steady above support", HACK], llm=llm_ok)
    nl = layer("veto", http, now)
    nl.refresh(now)
    items = [r for r in read(nl) if r["event"] == "item"]
    tgt = {p: 0.05 for p in PAIRS} | {"SOL/USD": 0.12, "XRP/USD": -0.08}
    new, info = nl.adjust(tgt, now)
    later, info2 = nl.adjust(tgt, now + pd.Timedelta(hours=73))
    # calendar and F&G (fresh layer, no veto)
    cpi = pd.Timestamp("2026-10-14 12:30", tz="UTC")
    nl2 = layer("rules", FakeHTTP(fng=90, fng_time=cpi - pd.Timedelta(hours=12)), now)   # fresh F&G at CPI time
    nl2.fetch_fng()
    m_before = nl2.adjust({"BTC/USD": 0.1}, cpi - pd.Timedelta(hours=10))[1]["mult"]
    m_after3 = nl2.adjust({"BTC/USD": 0.1}, cpi + pd.Timedelta(hours=3))[1]["mult"]
    nl2.fng = None
    m_far = nl2.adjust({"BTC/USD": 0.1}, cpi - pd.Timedelta(hours=30))[1]["mult"]
    m_after5 = nl2.adjust({"BTC/USD": 0.1}, cpi + pd.Timedelta(hours=5))[1]["mult"]
    nl3 = layer("fng", FakeHTTP(fng=8, fng_time=now - pd.Timedelta(hours=60)), now)
    nl3.fetch_fng()
    m_stale = nl3.adjust({"BTC/USD": 0.1}, now)[1]["mult"]
    nl4 = layer("fng2", FakeHTTP(fng=8, fng_time=now - pd.Timedelta(hours=2)), now)
    nl4.fetch_fng()
    m_fear = nl4.adjust({"BTC/USD": 0.1}, now)[1]["mult"]
    rng = np.random.default_rng(0)
    ok_reduce = True
    for _ in range(200):
        t = {p: float(rng.normal(0, 0.1)) for p in PAIRS}
        n, _ = nl.adjust(t, now)
        ok_reduce &= all(abs(n[p]) <= abs(t[p]) + 1e-15 and n[p] * t[p] >= 0 for p in PAIRS)
    return report("veto, calendar, Fear & Greed, reduce-only", {
        f"hack headline -> veto SOL/USD logged ({[i.get('rule') for i in items if i.get('rule')]})":
            any((i.get("rule") or "").startswith("veto SOL/USD 72h") for i in items),
        "duplicate headline classified once": sum(1 for i in items if i["headline"] == HACK) == 1,
        "neutral headline: no rule": any(i["llm"]["coin"] == "BTC" and i["rule"] is None for i in items),
        "vetoed coin -> 0, others unchanged": new["SOL/USD"] == 0 and new["BTC/USD"] == 0.05 and new["XRP/USD"] == -0.08,
        "veto expires after 72h": later["SOL/USD"] == 0.12 and not info2["vetoed"],
        f"CPI in 10h -> x0.7 x F&G 90 x0.8 ({m_before})": abs(m_before - 0.56) < 1e-9,
        f"3h after CPI still x0.7 (x0.8 F&G) ({m_after3}); 5h after: none ({m_after5})": abs(m_after3 - 0.56) < 1e-9 and m_after5 == 1.0,
        f"30h before CPI: none ({m_far})": m_far == 1.0,
        f"F&G 8 (extreme fear) -> x0.8 ({m_fear}); 60h old -> ignored ({m_stale})": m_fear == 0.8 and m_stale == 1.0,
        "reduce-only on 200 random target sets (no increase, no sign flip)": ok_reduce,
    })


def test_failures() -> bool:
    now = pd.Timestamp("2026-10-08 12:00", tz="UTC")
    bad = layer("badjson", FakeHTTP(titles=[HACK], llm=lambda h: "Sure! Here is my answer: severe hack"), now)
    bad.refresh(now)
    inv = [r for r in read(bad) if r["event"] == "llm_invalid"]
    down = layer("outage", FakeHTTP(titles=[HACK], outage=True), now)
    down.refresh(now)
    errs = read(down, "errors")
    cap = layer("cap", FakeHTTP(titles=[HACK, "Ethereum upgrade goes live", "Cardano partnership announced",
                                        "Chainlink oracle news"], llm=llm_ok, usage=(1_000_000, 0)), now,
                {"daily_cost_cap_usd": 1.0})
    cap.refresh(now)
    capped = [r for r in read(cap) if r["event"] == "cost_cap"]
    classified = [r for r in read(cap) if r["event"] == "item"]
    leak = layer("leak", FakeHTTP(titles=[HACK], outage=False, llm=None), now)
    leak.http.outage = False
    leak.http.get = FakeHTTP(titles=[HACK]).get
    leak.http.post = lambda *a, **k: (_ for _ in ()).throw(requests.ConnectionError(f"failed with key {KEY}"))
    leak.refresh(now)
    logs_text = "".join(p.read_text() for d in (OUT / "leak", OUT / "outage", OUT / "veto") for p in d.rglob("*.jsonl"))
    slow = layer("slow", FakeHTTP(titles=[HACK], llm=llm_ok, delay=1.5), now)
    t0 = time.time()
    slow.maybe_refresh(now)
    dt = time.time() - t0
    slow.thread.join(10)
    nokey = layer("nokey", FakeHTTP(titles=[HACK], llm=llm_ok), now, key="")
    nokey.refresh(now)
    return report("failures never block, never leak", {
        f"JSON failure -> llm_invalid logged, no veto ({len(inv)})": len(inv) == 1 and not bad.vetoes,
        f"outage -> refresh returns, {len(errs)} source errors logged (RSS, F&G), no veto, LLM never called":
            len(errs) >= 2 and not down.vetoes and down.http.posts == 0 and all(e["where"].startswith("news:") for e in errs),
        f"cost cap -> 1 classified, {len(capped)} items stopped by the cap": len(classified) == 1 and len(capped) >= 1,
        "API key never in any log (incl. an exception that contains it)": KEY not in logs_text and "***" in logs_text,
        f"maybe_refresh returns at once while the fetch runs in the background ({dt:.2f}s)": dt < 0.3 and bool(slow.vetoes),
        "no NEWS_LLM_API_KEY -> headlines fetched, nothing classified, no veto": not nokey.vetoes and nokey.http.posts == 0,
    })


def test_shadow_replay() -> bool:
    import tests.test_sleeves as ts
    from tests.test_sleeves import Sim
    ts.OUT = OUT
    cfg = load_config(HERE / "config_competition_s3v2e.yaml")
    cfg.update(dry_run=False, poll_s=0, limit_wait_s=0, limit_poll_s=0, allow_competition=False,
               paths={"log_dir": "logs", "state_dir": "state", "kill_file": "KILL"})
    cfg_news = copy.deepcopy(cfg)
    cfg_news["news_layer"] = {"enabled": True, "shadow": True, "rss": ["https://rss.example.com/feed"]}
    c = load_closes()
    hours = c.index[-24 * 10:]
    vetoed_at = hours[len(hours) // 2]

    class NewsSim(Sim):
        def new_bot(self):
            bot = StrategyBot(self.cfg, self.ex, base_dir=self.base, clock=lambda: self.now["t"], sleep=lambda s: None,
                              bars=self.bars)
            if self.cfg.get("news_layer"):
                bot.news = NewsLayer(self.cfg["news_layer"], list(self.cfg["universe"]), bot.log_dir, bot.state_dir, HERE,
                                     http=FakeHTTP(titles=[HACK], llm=llm_ok), clock=lambda: self.now["t"],
                                     api_key=KEY, cp_token=None)
                bot.news.maybe_refresh = lambda now: None          # deterministic: refresh called explicitly below
            bot.setup()
            return bot

    a, b = NewsSim("plain", c, hours[0], cfg), NewsSim("shadow", c, hours[0], cfg_news)
    for h in hours:
        if h == vetoed_at:
            b.bot.news.refresh(h)
        a.run_hour(h)
        b.run_hour(h)
    key = lambda o: (o["time"], o["action"], json.dumps(o.get("request"), sort_keys=True))
    oa = [key(o) for o in a.read("orders") if "response" in o]
    ob = [key(o) for o in b.read("orders") if "response" in o]
    sh = [json.loads(x) for x in (b.base / "logs" / "news_shadow.jsonl").read_text().splitlines()]
    steps = [r for r in sh if r["event"] == "step"]
    veto_steps = [r for r in steps if any(f.startswith("veto SOL/USD") for f in r["fired"])]
    summaries = [r for r in sh if r["event"] == "daily_summary"]
    hb = json.loads((b.base / "state" / "heartbeat.json").read_text())
    import status
    lines, _ = status.render(cfg_news, status.build(cfg_news, b.base))
    fp_same = a.bot._fingerprint() == b.bot._fingerprint()
    errors = b.read("errors")
    print(f"\n   {len(oa)} orders either way; {len(steps)} shadow steps, {len(veto_steps)} with the SOL veto, "
          f"{len(summaries)} daily summaries")
    return report("SHADOW mode in a 10-day replay (config_competition_s3v2e strategy, testing paths)", {
        f"orders identical with and without the shadow layer ({len(oa)})": oa == ob and len(oa) > 0,
        "the veto shows in the shadow log as a would-be change": bool(veto_steps)
            and all(r["changed"].get("SOL/USD", [None, 0])[1] == 0 for r in veto_steps if "SOL/USD" in r["changed"]),
        "a shadow record every step after start, daily summaries written": len(steps) >= 24 * 9 and len(summaries) >= 8,
        "heartbeat carries the news state; status.py shows it": bool(hb.get("news")) and any("News layer (SHADOW)" in x for x in lines),
        "target fingerprint unchanged by the layer": fp_same,
        f"0 errors ({len(errors)})": not errors,
    })


def main() -> int:
    shutil.rmtree(OUT, ignore_errors=True)
    ok = test_units() & test_veto_and_rules() & test_failures() & test_shadow_replay()
    print(f"\nnews layer tests: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
