"""Sleeve allocator: several strategies in one account, each on its own book and schedule.

Each sleeve owns a VIRTUAL book (cash + signed units per pair; short = negative units) that
starts at weight x the capped account capital and then evolves with its own PnL and fees,
exactly like the sleeve's standalone backtest. The account's real orders are the per-pair
NET of all sleeves' book changes, so a coin held by two sleeves (e.g. SOL in s3v2 and
xsmom) gets one order per step and never ping-pongs.

Execution modes (per sleeve, matching each sleeve's backtest):
  band       every completed hour: a pair trades only if |target - book weight| > band, or
             the target is 0 while the book still holds it (s3v2 / live single-strategy rule)
  scheduled  the book moves FULLY to its target only at the sleeve's decision step (and when
             the account-wide brake / KILL multiplier changes); no drift trades in between
             (xsmom: decision on the 14:00 UTC bar)
Account-wide: the drawdown brake / KILL multiplier scales every sleeve's targets; the
capital cap scales sleeve sizing so that the books together never size above it.
This module is pure (no I/O): the bot feeds it prices and persists `state()`.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import pandas as pd

EPS_UNITS = 1e-12


@dataclass
class SleeveSpec:
    name: str
    weight: float
    strategy: dict[str, Any]
    universe: list[str]
    execution: str = "band"            # band | scheduled
    band: float = 0.06
    decision_hour_utc: int = 0         # wall-clock hour of the decision step
    fee_rate: float = 0.001            # book-keeping fee (taker), as in the backtests

    @classmethod
    def from_cfg(cls, d: dict[str, Any], default_strategy: dict[str, Any], default_universe: list[str],
                 default_band: float, default_hour: int) -> "SleeveSpec":
        s = cls(name=str(d["name"]), weight=float(d["weight"]),
                strategy=dict(d.get("strategy") or default_strategy),
                universe=list(d.get("universe") or default_universe),
                execution=str(d.get("execution", "band")), band=float(d.get("band", default_band)),
                decision_hour_utc=int(d.get("decision_hour_utc", default_hour)),
                fee_rate=float(d.get("fee_rate", 0.001)))
        if s.execution not in ("band", "scheduled"):
            raise ValueError(f"sleeve {s.name}: execution must be band|scheduled")
        if not 0 < s.weight <= 1:
            raise ValueError(f"sleeve {s.name}: weight must be in (0, 1]")
        return s


@dataclass
class SleeveBook:
    cash: float
    units: dict[str, float] = field(default_factory=dict)
    target: dict[str, float] | None = None
    slot: str | None = None
    computed_at: str | None = None
    fingerprint: dict[str, Any] | None = None
    last_mult: float | None = None

    def equity(self, px: dict[str, float]) -> float:
        return self.cash + sum(u * px[p] for p, u in self.units.items() if u)

    def weights(self, px: dict[str, float]) -> dict[str, float]:
        e = self.equity(px)
        return {p: (u * px[p] / e if e > 0 else 0.0) for p, u in self.units.items()}

    def to_json(self) -> dict[str, Any]:
        return {"cash": self.cash, "units": {p: u for p, u in self.units.items() if abs(u) > EPS_UNITS},
                "target": self.target, "slot": self.slot, "computed_at": self.computed_at,
                "fingerprint": self.fingerprint, "last_mult": self.last_mult}

    @classmethod
    def from_json(cls, d: dict[str, Any]) -> "SleeveBook":
        return cls(cash=float(d["cash"]), units={p: float(u) for p, u in (d.get("units") or {}).items()},
                   target=d.get("target"), slot=d.get("slot"), computed_at=d.get("computed_at"),
                   fingerprint=d.get("fingerprint"), last_mult=d.get("last_mult"))


def decision_slot(now: pd.Timestamp, hour: int) -> pd.Timestamp:
    """Most recent decision time (wall clock `hour`:00 UTC) <= now."""
    slot = now.floor("D") + pd.Timedelta(hours=hour)
    return slot if slot <= now else slot - pd.Timedelta(days=1)


def desired_units(spec: SleeveSpec, book: SleeveBook, px: dict[str, float], mult: float,
                  scale: float, decide: bool) -> dict[str, float]:
    """Units the sleeve wants to hold after this step (before netting)."""
    tgt = {p: w * mult for p, w in (book.target or {}).items()}
    eq = book.equity(px) * scale
    pairs = set(spec.universe) | set(book.units)
    cur = book.units
    want = dict(cur)
    if spec.execution == "scheduled":
        if decide or book.last_mult is None or mult != book.last_mult:
            want = {p: tgt.get(p, 0.0) * eq / px[p] for p in pairs if px.get(p)}
        return want
    wcur = {p: (cur.get(p, 0.0) * px[p] / eq if eq > 0 else 0.0) for p in pairs if px.get(p)}
    for p in wcur:
        tw, cw = tgt.get(p, 0.0), wcur[p]
        holding = abs(cur.get(p, 0.0)) > EPS_UNITS
        if abs(tw - cw) > spec.band or (tw == 0 and holding):
            want[p] = tw * eq / px[p]
    return want


def apply_fills(spec: SleeveSpec, book: SleeveBook, want: dict[str, float], px: dict[str, float]) -> float:
    """Move the book to `want` at `px`, charging fee_rate on traded notional. Returns fees."""
    fee = 0.0
    for p, u in want.items():
        d = u - book.units.get(p, 0.0)
        if abs(d) <= EPS_UNITS:
            continue
        notional = d * px[p]
        f = abs(notional) * spec.fee_rate
        book.cash -= notional + f
        fee += f
        book.units[p] = u
    book.units = {p: u for p, u in book.units.items() if abs(u) > EPS_UNITS}
    return fee
