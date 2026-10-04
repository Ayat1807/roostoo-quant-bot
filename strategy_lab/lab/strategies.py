"""Strategy loader: the live strategies from strategy_bot/strategies plus experimental ones
in strategy_lab/strategies/*.py, all implementing the same interface:

    class MyStrategy(Strategy):
        name = "my_strategy"
        def target_weights(self, closes: pd.DataFrame, cfg: dict) -> dict[str, float]: ...

The live package is imported straight from strategy_bot (as `live_strategies`), so the
lab always backtests the exact code the bot runs. A lab strategy that proves itself is
promoted by copying its file into strategy_bot/strategies and registering it there.
"""

from __future__ import annotations

import importlib.util
import inspect
import sys
from types import ModuleType

from lab import REPO, ROOT

LIVE_DIR = REPO / "strategy_bot" / "strategies"
LAB_DIR = ROOT / "strategies"


def _load_live() -> ModuleType:
    if "live_strategies" in sys.modules:
        return sys.modules["live_strategies"]
    spec = importlib.util.spec_from_file_location(
        "live_strategies", LIVE_DIR / "__init__.py", submodule_search_locations=[str(LIVE_DIR)])
    mod = importlib.util.module_from_spec(spec)
    sys.modules["live_strategies"] = mod
    spec.loader.exec_module(mod)
    return mod


live = _load_live()
Strategy = live.Strategy  # the one shared base class


def _lab_strategies() -> dict[str, type]:
    found: dict[str, type] = {}
    for f in sorted(LAB_DIR.glob("*.py")):
        if f.name.startswith("_"):
            continue
        name = f"lab_strategies.{f.stem}"
        spec = importlib.util.spec_from_file_location(name, f)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[name] = mod
        spec.loader.exec_module(mod)
        for _, obj in inspect.getmembers(mod, inspect.isclass):
            if issubclass(obj, Strategy) and obj is not Strategy and obj.__module__ == name:
                found[obj.name] = obj
    return found


def registry() -> dict[str, tuple[type, str]]:
    """name -> (class, origin) with origin 'live' or 'lab'. Lab names may not shadow live ones."""
    reg = {n: (c, "live") for n, c in live.STRATEGIES.items()}
    for n, c in _lab_strategies().items():
        if n in reg:
            raise ValueError(f"lab strategy {n!r} shadows a live strategy; rename it")
        reg[n] = (c, "lab")
    return reg


def get_strategy(name: str):
    reg = registry()
    if name not in reg:
        raise ValueError(f"unknown strategy {name!r}; available: {sorted(reg)}")
    return reg[name][0]()
