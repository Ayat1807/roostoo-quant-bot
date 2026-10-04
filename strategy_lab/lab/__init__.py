"""strategy_lab: offline research harness (data, backtester, scorecard, analogs)."""

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent          # strategy_lab/
REPO = ROOT.parent                                      # Trading_Competition/


def load_config(path: Path | None = None) -> dict:
    return yaml.safe_load((path or ROOT / "config" / "lab.yaml").read_text(encoding="utf-8"))
