"""Load the reference research code read-only from _reference/roostoo-bot/research.

`research/strategies.py` would collide with our `strategies` package, so it is loaded
under the module name `ref_strategies`; `research/engine.py` is loaded as `engine`
(the name strategies.py imports).
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import ModuleType

RESEARCH = Path(__file__).resolve().parents[2] / "_reference" / "roostoo-bot" / "research"


def _load(name: str, file: str) -> ModuleType:
    if name in sys.modules:
        return sys.modules[name]
    path = RESEARCH / file
    if not path.exists():
        raise FileNotFoundError(f"reference code missing: {path} (unzip roostoo-bot.zip "
                                "into Trading_Competition/_reference/)")
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


engine = _load("engine", "engine.py")
ref_strategies = _load("ref_strategies", "strategies.py")
