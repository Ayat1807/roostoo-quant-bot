"""Drawdown brake + kill switch (port of the reference bot/risk.py; same rules as the backtest).

Equity vs its rolling 14-day peak:
  below dd_soft (-4%) -> exposure x0.5
  below dd_hard (-7%) -> flat for cooloff_h (24h), then the peak resets (only equity
                         from the reset time on counts toward the new peak)
A file named KILL in the bot folder -> exposure 0 (flatten and idle) while it exists.
State (equity history, cool-off) is persisted so restarts keep the brake.
"""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from infra import replace_with_retry


class RiskManager:
    def __init__(self, soft: float = -0.04, hard: float = -0.07, cooloff_h: int = 24,
                 peak_days: int = 14, state: Path | str = "state/risk.json",
                 kill_file: Path | str = "KILL") -> None:
        self.soft, self.hard, self.cool = soft, hard, pd.Timedelta(hours=cooloff_h)
        self.win = pd.Timedelta(days=peak_days)
        self.state_path, self.kill_file = Path(state), Path(kill_file)
        self.hist: list[tuple[pd.Timestamp, float]] = []
        self.flat_until: pd.Timestamp | None = None
        self.reset_at: pd.Timestamp | None = None
        if self.state_path.exists():
            d = json.loads(self.state_path.read_text(encoding="utf-8"))
            self.hist = [(pd.Timestamp(t), e) for t, e in d.get("hist", [])]
            self.flat_until = pd.Timestamp(d["flat_until"]) if d.get("flat_until") else None
            self.reset_at = pd.Timestamp(d["reset_at"]) if d.get("reset_at") else None

    def kill_active(self) -> bool:
        return self.kill_file.exists()

    def scale(self, now: pd.Timestamp, equity: float) -> tuple[float, str]:
        """Return (exposure multiplier, reason)."""
        if self.kill_active():
            return 0.0, "kill_switch"
        self.hist = [(t, e) for t, e in self.hist if t > now - self.win] + [(now, equity)]
        floor = self.reset_at or pd.Timestamp(0, tz="UTC")
        peak = (max(e for t, e in self.hist if t >= floor)
                if any(t >= floor for t, _ in self.hist) else equity)
        dd = equity / peak - 1
        out = (1.0, f"dd={dd:.4f}")
        if self.flat_until and now < self.flat_until:
            out = (0.0, f"cooloff dd={dd:.4f}")
        elif dd < self.hard:
            self.flat_until = self.reset_at = now + self.cool
            out = (0.0, f"hard_stop dd={dd:.4f}")
        elif dd < self.soft:
            out = (0.5, f"soft_brake dd={dd:.4f}")
        self._save()
        return out

    def _save(self) -> None:
        self.state_path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.state_path.with_suffix(".tmp")
        tmp.write_text(json.dumps({
            "hist": [(str(t), e) for t, e in self.hist],
            "flat_until": str(self.flat_until) if self.flat_until else None,
            "reset_at": str(self.reset_at) if self.reset_at else None}), encoding="utf-8")
        replace_with_retry(tmp, self.state_path)
