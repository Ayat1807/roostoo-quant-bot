"""Research block 4a report (event-day variants of xsmom on R1): leaderboard_b4_events.md.

    python -m lab.b4e

Rules are fixed in variants_b4_events.yaml (declared before any run). Judged on data to
2026-06-30: IS = 2020-02-15 -> 2024-12-31, OOS = 2025-01-01 -> 2026-06-30; Jul-Oct 2026 is
informational only. Event windows = rolling 14-day windows containing a CPI release or an FOMC
decision (data/events.csv).
"""

from __future__ import annotations

import sys

import numpy as np
import pandas as pd
import yaml

from lab import ROOT
from lab.b3 import INFO0, IS_END, OOS0, OOS_END, windows
from lab.data import load_close
from lab.events import load_events
from lab.leaderboard import N01, declared_total
from lab.runner import load_hourly

FILE = "variants_b4_events.yaml"
CONTROL = "b3_xsmom_r1"
HALVES = {"IS": (None, IS_END), "OOS": (OOS0, OOS_END), "INFO": (INFO0, None)}
FEW = 5


def tag_windows(w: pd.DataFrame, ev: pd.DatetimeIndex) -> pd.DataFrame:
    w = w.copy()
    w["events"] = [tuple(str(t) for t in ev[(ev >= s) & (ev < s + pd.Timedelta(days=14))]) for s in w["start"]]
    w["has_event"] = w["events"].map(bool)
    return w


def stats(r: pd.Series) -> dict:
    if r.empty:
        return {"n": 0}
    return {"n": int(len(r)), "p10": float((r >= 0.10).mean()), "pm10": float((r <= -0.10).mean()),
            "worst": float(r.min()), "median": float(r.median())}


def event_day_returns(h: pd.DataFrame, ev: pd.DatetimeIndex, a, b) -> pd.Series:
    """Return from 00:00 UTC two days before each event day to 00:00 three days after it."""
    eq = h["equity"]
    out = {}
    for t in ev:
        d = t.floor("D")
        s, e = d - pd.Timedelta(days=2), d + pd.Timedelta(days=3)
        if (a is not None and s < a) or (b is not None and e > b + pd.Timedelta(hours=1)):
            continue
        if s < eq.index[0] or e > eq.index[-1]:
            continue
        out[t] = eq.asof(e) / eq.asof(s) - 1
    return pd.Series(out, dtype=float)


def breakout_counts(ev: pd.DatetimeIndex) -> dict:
    """How often the breakout rule fires (BTC +/-2% within 4h of the event), per half."""
    btc = load_close(["BTCUSDT"])["BTCUSDT"]
    tau = btc.index + pd.Timedelta(hours=1)
    out = {k: {"up": 0, "down": 0, "none": 0} for k in HALVES}
    for t in ev:
        k = next((k for k, (a, b) in HALVES.items() if (a is None or t >= a) and (b is None or t <= b)), None)
        pre = tau.searchsorted(t, side="right") - 1
        if k is None or pre < 0 or pre + 5 > len(btc):
            continue
        p0, res = btc.iloc[pre], "none"
        j = pre + 1
        while j < len(btc) and tau[j] <= t + pd.Timedelta(hours=4):
            r = btc.iloc[j] / p0 - 1
            if r > 0.02:
                res = "up"
                break
            if r < -0.02:
                res = "down"
                break
            j += 1
        out[k][res] += 1
    return out


def main() -> int:
    doc = yaml.safe_load((ROOT / FILE).read_text(encoding="utf-8"))
    ev_all = load_events(("CPI", "FOMC_DECISION"))
    ev = pd.DatetimeIndex(ev_all["time"]).sort_values()
    names = [CONTROL] + [r["name"] for r in doc["runs"]]
    rows, wins = {}, {}
    for name in names:
        h = load_hourly(name)
        if h is None:
            print(f"  {name}: not run")
            continue
        row: dict = {"run": name}
        for k, (a, b) in HALVES.items():
            w = tag_windows(windows(h, a, b), ev)
            wins[(name, k)] = w
            hj = h.loc[a:b]
            yrs = (hj.index[-1] - hj.index[0]) / pd.Timedelta(days=365)
            edr = event_day_returns(h, ev, a, b)
            row[k] = {"event": stats(w.loc[w["has_event"], "ret"]) if not w.empty else {"n": 0},
                      "all": stats(w["ret"]) if not w.empty else {"n": 0},
                      "share_event_windows": float(w["has_event"].mean()) if not w.empty else 0.0,
                      "n_events": int(((ev >= (a or hj.index[0])) & (ev <= (b or hj.index[-1]))).sum()),
                      "edr_mean": float(edr.mean()) if len(edr) else np.nan,
                      "edr_median": float(edr.median()) if len(edr) else np.nan, "edr_n": int(len(edr)),
                      "fees_yr": float(hj["fees"].sum() / hj["equity"].mean() / yrs),
                      "trades_day": float(hj["trades"].groupby(hj.index.floor("D")).sum().mean())}
        rows[name] = row
    # few-events flag and adopt rule (vs the control), per half
    for name, row in rows.items():
        if name == CONTROL:
            continue
        passes = True
        for k in ("IS", "OOS"):
            v, c = wins[(name, k)], wins[(CONTROL, k)]
            m = v.merge(c, on="start", suffixes=("", "_c"))
            m = m[m["has_event"]]
            gain = m[(m["ret"] >= 0.10) & (m["ret_c"] < 0.10)]
            loss = m[(m["ret"] < 0.10) & (m["ret_c"] >= 0.10)]
            ev_gain = {e for es in gain["events"] for e in es}
            row[k]["diff_windows"] = (len(gain), len(loss))
            row[k]["gain_events"] = len(ev_gain)
            row[k]["few"] = len(gain) > len(loss) and len(ev_gain) < FEW
            rv, rc = row[k], rows[CONTROL][k]
            beat = rv["event"]["p10"] > rc["event"]["p10"]
            safe = rv["all"]["pm10"] <= rc["all"]["pm10"]
            row[k]["beats"], row[k]["safe"] = beat, safe
            passes &= beat and safe
        row["adopt"] = passes
    cand = [r for n, r in rows.items() if n != CONTROL and r["adopt"]]
    cand.sort(key=lambda r: (r["OOS"]["event"]["p10"], r["IS"]["event"]["p10"]), reverse=True)
    winner = cand[0]["run"] if cand else None
    write(rows, winner, breakout_counts(ev), ev)
    print(f"adopted: {winner}")
    return 0


def write(rows: dict, winner: str | None, bo: dict, ev: pd.DatetimeIndex) -> None:
    pct = lambda x: "" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{x:+.1%}"
    pr = lambda x: "" if x is None else f"{x:.0%}"
    n_tr = declared_total()
    sr0 = N01.inv_cdf(1 - 1 / n_tr)
    L = ["# Research block 4a: event-day variants of the live strategy (xsmom on R1)\n",
         f"_Generated {pd.Timestamp.now(tz='UTC'):%Y-%m-%d %H:%M} UTC. Rules in `variants_b4_events.yaml` "
         f"(declared before any run). Judged on data to 2026-06-30: IS = 2020-02-15 to 2024-12-31, OOS = "
         f"2025-01-01 to 2026-06-30. **Jul-Oct 2026 is informational only.**_\n",
         f"**Trials:** {n_tr} declared across all blocks (this block: 9). Luck threshold: with that many tries "
         f"the best result is expected to look about {sr0:.1f} standard errors better than its true value.\n",
         "**Event windows** = rolling 14-day windows (daily step) containing a CPI release or an FOMC decision. "
         "**Adopt rule:** event-window P(14d >= +10%) strictly above the control in BOTH halves, and all-window "
         "P(14d <= -10%) not above the control in both halves.\n",
         f"**Adopted: {'`' + winner + '`' if winner else 'none (no variant passes the rule)'}**\n"]
    for k in ("IS", "OOS", "INFO"):
        c = rows[CONTROL][k]
        L += [f"\n## {k}{' (informational only)' if k == 'INFO' else ''}: {c['n_events']} independent CPI/FOMC "
              f"events, {c['event'].get('n', 0)} event windows of {c['all'].get('n', 0)} "
              f"({c['share_event_windows']:.0%})\n",
              "| run | event windows: P>=10% / P<=-10% / worst / median | all windows: P>=10% / P<=-10% / worst / "
              "median | event day +/-2d: mean / median (n) | fees/yr | trades/day | "
              + ("beats on events / P<=-10% ok | windows won-lost vs control (events) |" if k != "INFO" else ""),
              "|" + "---|" * (8 if k != "INFO" else 6)]
        for name, r in rows.items():
            x = r[k]
            cell = lambda s: (f"{pr(s['p10'])} / {pr(s['pm10'])} / {pct(s['worst'])} / {pct(s['median'])}"
                              if s.get("n") else "n/a")
            extra = ""
            if k != "INFO":
                if name == CONTROL:
                    extra = " control | |"
                else:
                    dw = x["diff_windows"]
                    extra = (f" {'yes' if x['beats'] else 'no'} / {'yes' if x['safe'] else 'no'} | "
                             f"+{dw[0]} / -{dw[1]} ({x['gain_events']} events){' **FEW EVENTS**' if x['few'] else ''} |")
            L.append(f"| {name}{' (control)' if name == CONTROL else ''} | {cell(x['event'])} | {cell(x['all'])} | "
                     f"{pct(x['edr_mean'])} / {pct(x['edr_median'])} ({x['edr_n']}) | {x['fees_yr']:.1%} | "
                     f"{x['trades_day']:.2f} |{extra}")
    L += ["\n## How often the breakout rule fires (BTC beyond +/-2% within 4h of a CPI/FOMC event)\n",
          "| period | up (extra decision) | down (cash to next daily) | neither |", "|---|---|---|---|"]
    for k, v in bo.items():
        L.append(f"| {k} | {v['up']} | {v['down']} | {v['none']} |")
    L.append("\n_Windows won-lost: event windows where the variant reaches +10% and the control does not (won) "
             "and the reverse (lost); (events) = distinct events inside the won windows. FEW EVENTS = net gain "
             f"resting on fewer than {FEW} distinct events in that half._")
    (ROOT / "leaderboard_b4_events.md").write_text("\n".join(L) + "\n", encoding="utf-8")


if __name__ == "__main__":
    sys.exit(main())
