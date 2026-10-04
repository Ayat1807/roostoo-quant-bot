"""Build findings.md from logs/api_log.jsonl and the logs/results_*.json files.

    python generate_findings.py

Safe to re-run at any time; sections whose test has not run yet say so.
Also prints average latency per endpoint (task 7).
"""

from __future__ import annotations

import json
import statistics
import time
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from roostoo_client import API_LOG, HERE, LOG_DIR

OUT = HERE / "findings.md"

# Containers whose keys are data (pair/coin names), not field names.
DYNAMIC_CONTAINERS = {"TradePairs", "Data", "Wallet", "OrderPairs", "InitialWallet",
                      "SpotWallet", "MarginWallet"}

_ORDER = ["Pair", "OrderID", "Status", "Role", "ServerTimeUsage", "CreateTimestamp",
          "FinishTimestamp", "Side", "Type", "StopType", "Price", "Quantity",
          "FilledQuantity", "FilledAverPrice", "CoinChange", "UnitChange",
          "CommissionCoin", "CommissionChargeValue", "CommissionPercent"]

# Field paths as documented in the official README (success responses).
DOC_FIELDS: dict[str, set[str]] = {
    "/v3/serverTime": {"ServerTime"},
    "/v3/exchangeInfo": {"IsRunning", "InitialWallet.<key>"} | {
        f"TradePairs.<key>.{f}" for f in ["Coin", "CoinFullName", "Unit", "UnitFullName",
                                          "CanTrade", "PricePrecision", "AmountPrecision",
                                          "MiniOrder"]},
    "/v3/ticker": {"Success", "ErrMsg", "ServerTime"} | {
        f"Data.<key>.{f}" for f in ["MaxBid", "MinAsk", "LastPrice", "Change",
                                    "CoinTradeValue", "UnitTradeValue"]},
    "/v3/balance": {"Success", "ErrMsg", "Wallet.<key>.Free", "Wallet.<key>.Lock"},
    "/v3/pending_count": {"Success", "ErrMsg", "TotalPending", "OrderPairs.<key>"},
    "/v3/place_order": {"Success", "ErrMsg"} | {f"OrderDetail.{f}" for f in _ORDER},
    "/v3/query_order": {"Success", "ErrMsg"} | {f"OrderMatched[].{f}" for f in _ORDER},
    "/v3/cancel_order": {"Success", "ErrMsg", "CanceledList[]"},
    "/v6/short_open": {"Success", "ID", "Pair", "OrderType", "EntryPrice", "ShortQty",
                       "Collateral", "OpenFee", "Status", "CreateTimestamp"},
    "/v6/short_close": {"Success", "ClosePrice", "RealizedPNL", "CloseFee", "ReturnAmount",
                        "ClosedQty", "FullyClosed", "RemainingQty", "RemainingCollateral"},
    "/v6/short_positions": {"Success"} | {
        f"Positions[].{f}" for f in ["ID", "Pair", "EntryPrice", "ShortQty", "Collateral",
                                     "CurrentPrice", "UnrealizedPNL", "UnrealizedPNLPct",
                                     "PositionValue", "CreateTimestamp", "PositionStatus"]},
}


# --------------------------------------------------------------------------- #
# Loading
# --------------------------------------------------------------------------- #

def load_log() -> list[dict[str, Any]]:
    if not API_LOG.exists():
        return []
    rows = []
    for line in API_LOG.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def load_json(name: str) -> Any:
    p = LOG_DIR / name
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


# --------------------------------------------------------------------------- #
# Analysis
# --------------------------------------------------------------------------- #

def field_paths(obj: Any, prefix: str = "", parent: str = "") -> set[str]:
    """All key paths in a JSON value, with data keys replaced by <key>."""
    paths: set[str] = set()
    if isinstance(obj, dict):
        for k, v in obj.items():
            name = "<key>" if parent in DYNAMIC_CONTAINERS else k
            p = f"{prefix}.{name}" if prefix else name
            sub = field_paths(v, p, k if name != "<key>" else "")
            paths |= sub if sub else {p}
    elif isinstance(obj, list):
        p = f"{prefix}[]"
        sub: set[str] = set()
        for item in obj:
            sub |= field_paths(item, p, "")
        paths |= sub if sub else {p}
    return paths


def latency_table(log: list[dict[str, Any]]) -> list[tuple[str, int, float, float, float, float]]:
    by_ep: dict[str, list[float]] = defaultdict(list)
    for r in log:
        if r.get("latency_ms") is not None and r.get("http_status") is not None:
            by_ep[r["endpoint"]].append(float(r["latency_ms"]))
    rows = []
    for ep, xs in sorted(by_ep.items()):
        xs_sorted = sorted(xs)
        p95 = xs_sorted[min(len(xs) - 1, int(round(0.95 * (len(xs) - 1))))]
        rows.append((ep, len(xs), statistics.mean(xs), statistics.median(xs), p95, max(xs)))
    return rows


def err_messages(log: list[dict[str, Any]]) -> list[tuple[str, str, int, str]]:
    """(endpoint, ErrMsg, count, example params) for Success=false and transport errors."""
    c: Counter[tuple[str, str]] = Counter()
    example: dict[tuple[str, str], str] = {}
    for r in log:
        resp = r.get("response")
        msg = None
        if isinstance(resp, dict) and resp.get("Success") is False:
            msg = str(resp.get("ErrMsg"))
        elif r.get("error"):
            msg = "TRANSPORT: " + str(r["error"])[:120]
        elif r.get("http_status") not in (None, 200):
            msg = f"HTTP {r.get('http_status')}"
        if msg:
            key = (r["endpoint"], msg)
            c[key] += 1
            example.setdefault(key, json.dumps(
                {k: v for k, v in (r.get("params") or {}).items() if k != "timestamp"}))
    return [(ep, m, n, example[(ep, m)]) for (ep, m), n in c.most_common()]


# --------------------------------------------------------------------------- #
# Rendering
# --------------------------------------------------------------------------- #

def md_table(headers: list[str], rows: list[list[Any]]) -> str:
    out = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    out += ["| " + " | ".join(str(x) for x in row) + " |" for row in rows]
    return "\n".join(out)


def main() -> None:
    log = load_log()
    pub = load_json("results_public.json")
    acct = load_json("results_account.json")
    trade = load_json("results_trading.json")
    data_src = load_json("results_data_sources.json")
    info = load_json("exchange_info.json")
    tick = load_json("ticker_snapshot.json")
    diffs: list[str] = []  # live-vs-docs differences, collected as we go
    L: list[str] = []

    L.append("# Roostoo API: initial testing findings\n")
    L.append(f"_Generated {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())} by "
             f"`generate_findings.py` from `logs/` ({len(log)} logged requests). "
             "Re-run after each test to refresh._\n")

    # 1. Connectivity
    L.append("## 1. Connectivity and clock\n")
    roostoo = [r for r in log if r["endpoint"].startswith("/v")]
    ok_http = sum(1 for r in roostoo if r.get("http_status") == 200)
    L.append(f"- Base URL `https://mock-api.roostoo.com`: {ok_http}/{len(roostoo)} "
             "Roostoo requests returned HTTP 200.")
    statuses = Counter(str(r.get("http_status")) for r in roostoo)
    L.append(f"- HTTP status counts: {dict(statuses)}")
    if pub:
        L.append(f"- Clock offset (server - local): **{pub['clock_offset_ms']} ms** "
                 f"(samples {pub['clock_offset_samples_ms']}); well inside the +-60 s window. "
                 "The client still applies the offset to every timestamp.")
        L.append(f"- `IsRunning`={pub['is_running']}, `InitialWallet`={pub['initial_wallet']}")
    else:
        L.append("- test_public.py not run yet.")
    L.append("")

    # 2. Pairs
    L.append("## 2. Trading pairs and order rules\n")
    if info and pub:
        tp = info.get("TradePairs", {})
        L.append(f"**{len(tp)} pairs** in exchangeInfo, **{pub['ticker_pair_count']}** in "
                 "the all-pairs ticker.\n")
        missing = sorted(set(tp) - set((tick or {}).get("Data", {})))
        if missing:
            diffs.append(f"Pairs listed in exchangeInfo with `CanTrade=true` but absent from "
                         f"the ticker: {', '.join(missing)}. Do not trade them.")
        types = Counter(v.get("AssetType", "?") for v in tp.values())
        L.append(f"AssetType counts: {dict(types)}\n")
        L.append("Full list: " + ", ".join(f"`{p}`" for p in sorted(tp)) + "\n")
        non_crypto = sorted(p for p, v in tp.items() if v.get("AssetType") not in (None, "crypto"))
        if non_crypto:
            L.append(f"Non-crypto pairs (tokenised stocks etc.): {', '.join(non_crypto)}\n")
        not_tradeable = sorted(p for p, v in tp.items() if not v.get("CanTrade"))
        L.append(f"Pairs with CanTrade=false: {not_tradeable or 'none'}\n")
        L.append("Top 10 by 24h `UnitTradeValue` (USD volume) at snapshot time:\n")
        L.append(md_table(["Pair", "24h USD vol", "LastPrice", "PricePrecision",
                           "AmountPrecision", "MiniOrder"],
                          [[r["pair"], f"{r['UnitTradeValue']:,.0f}", r["LastPrice"],
                            r["PricePrecision"], r["AmountPrecision"], r["MiniOrder"]]
                           for r in pub["top10"]]))
        minis = Counter(v.get("MiniOrder") for v in tp.values())
        L.append(f"\nMiniOrder values across all pairs: {dict(minis)} (rule: "
                 "price x quantity must be > MiniOrder, in USD).\n")
    else:
        L.append("test_public.py not run yet.\n")

    # 3. Fees
    L.append("## 3. Observed fees\n")
    if trade:
        by_kind: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for f in trade.get("fees", []):
            by_kind[f["kind"]].append(f)
        rows = []
        for kind, fs in sorted(by_kind.items()):
            pcts = [f["implied_pct"] for f in fs if f.get("implied_pct") is not None]
            quoted = sorted({str(f.get("CommissionPercent")) for f in fs
                             if f.get("CommissionPercent") is not None})
            rows.append([kind, len(fs), f"{statistics.mean(pcts):.4f}%" if pcts else "n/a",
                         ", ".join(quoted) or "n/a",
                         f"{sum(f['fee_usd'] for f in fs):.6f}"])
        L.append(md_table(["Fee type", "Fills", "Implied fee (fee / notional)",
                           "CommissionPercent field", "Total fee USD"], rows))
        L.append("\nExpected: taker 0.1%, maker 0.05%, short open/close 0.1%.\n")
        c = trade.get("c", {})
        if c.get("note"):
            L.append(f"- Maker test: {c['note']} (waited {c.get('waited_s')} s, "
                     f"final status {c.get('final_status')}).")
        for f in trade.get("b", []):
            if f.get("slippage_vs_ask_pct") is not None:
                L.append(f"- Market BUY filled at {f['price']} vs ticker ask "
                         f"{f['ticker_ask']} ({f['slippage_vs_ask_pct']:+.4f}%).")
            if f.get("slippage_vs_bid_pct") is not None:
                L.append(f"- Market SELL filled at {f['price']} vs ticker bid "
                         f"{f['ticker_bid']} ({f['slippage_vs_bid_pct']:+.4f}%).")
        a = trade.get("a") or (load_json("results_trading_a.json") or {}).get("a", {})
        if a:
            L.append(f"- Limit/cancel lifecycle: placed status `{a.get('placed_status')}`, "
                     f"after cancel `{a.get('status_after_cancel')}`, "
                     f"CanceledList={a.get('canceled_list')}.")
        e = trade.get("e", {})
        if e:
            L.append(f"- Reconciliation: USD spent {e['usd_spent']:.6f}; explained by fees "
                     f"{e['fees_total_usd']:.6f}, spot PnL {e['spot_pnl']:.6f}, short PnL "
                     f"{e['short_pnl']:.6f}, retained coin {e['retained_coin_cost']:.6f} -> "
                     f"unexplained **{e['unexplained']:+.6f} USD**. Total test notional "
                     f"${e['notional_used']:.2f}.")
        L.append("")
    else:
        L.append("test_trading.py not run yet (needs `--confirm` and the TESTING key).\n")

    # 4. Shorts
    L.append("## 4. Is shorting allowed?\n")
    d = (trade or {}).get("d")
    if d is None:
        L.append("Unknown: test_trading.py not run yet.\n")
    elif d.get("skipped"):
        L.append(f"Not tested: {d['skipped']}\n")
    elif d.get("allowed"):
        L.append("**Yes** on the testing account: short_open, partial close (50%) and "
                 f"final close all succeeded. Positions after close: "
                 f"`{d.get('positions_after_close')}`.\n")
        op = d.get("open", {})
        if op:
            L.append(f"- Requested collateral $20 -> response `Collateral`={op.get('Collateral')}, "
                     f"`ShortQty`={op.get('ShortQty')}, `EntryPrice`={op.get('EntryPrice')}, "
                     f"`OpenFee`={op.get('OpenFee')}. Collateral is re-computed as "
                     "ShortQty x EntryPrice after rounding the quantity DOWN, so slightly "
                     "less than requested is locked (1x, no leverage).")
            L.append(f"- Entry vs bid: {d.get('entry_vs_bid_pct'):+.4f}% (fills at MaxBid); "
                     "closes fill at MinAsk, so every short round trip pays the spread + 0.2%.")
            diffs.append("`/v6/short_open` returns `Collateral` = ShortQty x EntryPrice (after "
                         "rounding qty down), not the requested collateral.")
        L.append("\nThis does NOT prove the competition account allows shorts; ask organizers.\n")
    else:
        L.append(f"**No / failed**: ErrMsg `{d.get('ErrMsg')}`.\n")

    # 5. Field names
    L.append("## 5. Response field names (live vs docs)\n")
    L.append("`<key>` = a pair or coin name. Fields documented but not seen may simply be "
             "zero-valued (the API omits zero fields) or the case did not occur.\n")
    seen: dict[str, set[str]] = defaultdict(set)
    for r in roostoo:
        resp = r.get("response")
        if isinstance(resp, dict) and resp.get("Success") is not False:
            seen[r["endpoint"]] |= field_paths(resp)
    for ep in sorted(set(seen) | set(DOC_FIELDS)):
        live, doc = seen.get(ep, set()), DOC_FIELDS.get(ep, set())
        if not live:
            L.append(f"- `{ep}`: no successful live response logged yet.")
            continue
        extra, absent = sorted(live - doc), sorted(doc - live)
        L.append(f"- `{ep}`: " + ", ".join(f"`{p}`" for p in sorted(live)))
        if extra:
            L.append(f"  - **Undocumented, seen live:** {', '.join(extra)}")
            diffs.append(f"`{ep}` returns undocumented fields: {', '.join(extra)}")
        if absent:
            L.append(f"  - Documented, not seen: {', '.join(absent)}")
    L.append("")

    # 6. Errors
    L.append("## 6. ErrMsg / errors encountered\n")
    errs = err_messages(log)
    if errs:
        L.append(md_table(["Endpoint", "ErrMsg", "Count", "Params (example)"],
                          [[f"`{ep}`", m, n, f"`{p}`"] for ep, m, n, p in errs]))
        L.append("\n`no pending order under this account` and `no order matched` are "
                 "documented 'empty' answers (Success=false), not failures.\n")
        known = {
            "price should not less than market price 30%":
                "Undocumented rule: a LIMIT price may not be more than 30% below market "
                "(seen with a BUY at 50% of bid; 75% works). Expect a symmetric cap above "
                "market for SELLs.",
        }
        for ep, m, _, _ in errs:
            if m in known:
                L.append(f"- `{m}`: {known[m]}")
                diffs.append(f"`{ep}`: {known[m]}")
        L.append("")
    else:
        L.append("None.\n")

    # 7. Latency
    L.append("## 7. Latency per endpoint (ms)\n")
    lat = latency_table(log)
    L.append(md_table(["Endpoint", "Calls", "Mean", "Median", "p95", "Max"],
                      [[f"`{ep}`", n, f"{m:.0f}", f"{md:.0f}", f"{p:.0f}", f"{mx:.0f}"]
                       for ep, n, m, md, p, mx in lat]) if lat else "No calls logged.")
    L.append("\nMeasured from a home connection; latency from AWS will differ.\n")

    # 8. Binance
    L.append("## 8. Binance data vs Roostoo prices\n")
    if data_src:
        for host, v in data_src["hosts"].items():
            extra = (f", {v['rows']} hourly rows {v['first_open_utc']} -> "
                     f"{v['last_open_utc']} UTC" if v.get("rows") else "")
            L.append(f"- `{host}/api/v3/klines`: {v['status']}{extra}")
        if data_src["comparison"]:
            L.append("")
            L.append(md_table(["Pair", "Roostoo LastPrice", "Binance last 1h close",
                               "Diff %", "Binance 48h low-high"],
                              [[c["pair"], c["roostoo_last"], c["binance_close"],
                                f"{c['diff_pct']:+.4f}%",
                                f"{c['binance_48h_low']}-{c['binance_48h_high']}"]
                               for c in data_src["comparison"]]))
            mx = max(abs(c["diff_pct"]) for c in data_src["comparison"])
            verdict = ("Roostoo prices track Binance USDT spot almost exactly, so Binance "
                       "klines can seed indicators." if mx < 0.1 else
                       "Prices differ noticeably. Check the basis before using Binance history.")
            L.append(f"\nMax abs difference {mx:.4f}%. {verdict}\n")
    else:
        L.append("test_data_sources.py not run yet.\n")

    # 9. Account snapshot
    L.append("## 9. Testing account snapshot\n")
    if acct:
        if "start_usd_free" in acct:
            L.append(f"- USD Free {acct['start_usd_free']:,.2f}, Lock "
                     f"{acct['start_usd_lock']:,.2f}; wallet value "
                     f"${acct['wallet_value_usd']:,.2f}; other holdings: "
                     f"{list(acct.get('holdings', {})) or 'none'}")
        L.append(f"- Pending: {acct.get('pending')}")
        L.append(f"- Short positions: {acct.get('short_positions')}")
        L.append("")
    else:
        L.append("test_account.py not run yet (needs `.env` with the TESTING key).\n")

    # 10. Differences
    L.append("## 10. Live API vs documentation\n")
    L.extend(f"- {x}" for x in diffs) if diffs else L.append("- None found so far.")
    L.append("")

    # 11. Questions
    L.append("## 11. Open questions for the organizers\n")
    L.extend([
        "1. What are the rate limits (requests per second/minute, per key or per IP)? What "
        "happens when we exceed them (HTTP 429, ErrMsg, ban)?",
        "2. Does the **competition** account allow short positions (`/v6/short_*`), or will "
        "it return `this competition does not allow short positions`?",
        "3. What counts as \"enough trades per day\"? Is there a minimum number of orders, "
        "fills or notional, and does a canceled order count?",
        "4. Are fees on the competition account the same as testing (taker 0.1%, maker "
        "0.05%, short 0.1%)?",
        "5. Is the leaderboard scored on total portfolio value at LastPrice, at bid, or "
        "something else? How are open shorts and locked collateral valued?",
        "6. Are OMNI/USD and TON/USD (and any other pairs missing from the ticker) "
        "tradeable? Will the pair list change during the competition?",
        "7. Is the Roostoo price feed derived from Binance spot (the match is near-exact)? "
        "If so, is using Binance historical data and live data allowed?",
        "8. Do LIMIT orders fill against real Binance order-book moves or only on "
        "LastPrice crossing our price? Is there partial-fill behaviour?",
        "9. Is there a maximum number of open orders per account or per pair?",
        "10. The exchange lists tokenised stocks (`AssetType: stock`, e.g. NVDAB/USD, "
        "TSLAB/USD). Do they trade 24/7 or only in market hours, where does their price "
        "come from, and do they count toward scoring like crypto?",
        "11. Will the bot's own automated calls on the competition key from AWS be "
        "whitelisted by IP, and what exactly counts as a disqualifying 'manual' call?",
    ])
    L.append("")

    OUT.write_text("\n".join(L), encoding="utf-8")
    print(f"Wrote {OUT}")
    print("\nAverage latency per endpoint (ms):")
    for ep, n, m, md, p, mx in lat:
        print(f"  {ep:<40} n={n:<4} mean={m:7.1f} median={md:7.1f} p95={p:7.1f} max={mx:7.1f}")


if __name__ == "__main__":
    main()
