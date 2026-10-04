"""Strategy registry. Add new strategies here (see strategies/base.py)."""

from __future__ import annotations

from .base import Strategy
from .s3v2 import S3v2

STRATEGIES: dict[str, type[Strategy]] = {
    S3v2.name: S3v2,
}


def get_strategy(name: str) -> Strategy:
    try:
        return STRATEGIES[name]()
    except KeyError:
        raise ValueError(f"unknown strategy {name!r}; available: {sorted(STRATEGIES)}") from None
