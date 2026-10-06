"""Safety rules that the replay can't exercise. Offline.

    python -m tests.test_safety

1. An order request that times out AFTER reaching the exchange is never resent: the bot
   looks up pending orders on that pair, cancels them, logs, and moves on.
2. Key-label gate: 'competition' is refused unless allow_competition is true; unknown
   labels are refused; 'testing' is accepted.
3. Strategy plug-in contract: unknown strategy names are rejected; gross <= 1.
"""

from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path

import pandas as pd
import requests

from infra import JsonlLogs, build_client
from portfolio import Portfolio
from roostoo_client import KeySafetyError
from strategies import get_strategy
from tests.mock_exchange import MockRoostoo

OUT = Path(__file__).resolve().parent.parent / ".cache" / "safety"
PAIRS = ["BTC/USD", "ETH/USD"]


class TimeoutAfterSend(MockRoostoo):
    """place_order reaches the exchange (order rests) but the response is lost."""

    def place_order(self, *a, **kw):
        self.pending_every, self.n_limit = 1, 0
        super().place_order(*a, **kw)
        raise requests.ReadTimeout("simulated: response lost after the order was accepted")


def test_no_resend_after_timeout() -> bool:
    shutil.rmtree(OUT, ignore_errors=True)
    ex = TimeoutAfterSend(PAIRS)
    ex.set_prices({"BTC/USD": 85000.0, "ETH/USD": 2700.0})
    logs = JsonlLogs(OUT)
    port = Portfolio(ex, PAIRS, ex.exchange_info()["TradePairs"], logs, entry="limit",
                     limit_wait_s=0, capital_cap_usd=3000)
    port.rebalance({"BTC/USD": 0.2, "ETH/USD": 0.0}, ex.ticker()["Data"], band=0.06)
    sent = ex.calls.get("place_order", 0)
    pending = [o for o in ex.orders.values() if o["Status"] == "PENDING"]
    ok = sent == 1 and not pending and ex.calls.get("query_order", 0) >= 1
    print(f"[{'PASS' if ok else 'FAIL'}] timeout after send: place_order called {sent}x (expect 1), "
          f"lookup {ex.calls.get('query_order', 0)}x, orphan canceled={not pending}")
    return ok


def test_key_gate() -> bool:
    saved = {k: os.environ.get(k) for k in ("ROOSTOO_API_KEY", "ROOSTOO_API_SECRET", "ROOSTOO_KEY_LABEL")}
    os.environ.update(ROOSTOO_API_KEY="k" * 64, ROOSTOO_API_SECRET="s" * 64)
    results = []
    try:
        for label, allow, expect_ok in (("testing", False, True), ("competition", False, False),
                                        ("", False, False), ("prod", True, False)):
            os.environ["ROOSTOO_KEY_LABEL"] = label
            try:
                build_client(allow, OUT / "api.jsonl")
                got = True
            except KeySafetyError:
                got = False
            results.append(got == expect_ok)
            print(f"[{'PASS' if got == expect_ok else 'FAIL'}] label={label!r} "
                  f"allow_competition={allow}: {'accepted' if got else 'refused'}")
    finally:
        for k, v in saved.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v
    return all(results)


def test_plugin_contract() -> bool:
    try:
        get_strategy("nope")
        ok1 = False
    except ValueError:
        ok1 = True
    idx = pd.date_range("2026-01-01", periods=400, freq="1h", tz="UTC")
    up = pd.DataFrame({p: [100 * 1.001 ** i for i in range(400)] for p in PAIRS}, index=idx)
    w = get_strategy("s3v2").target_weights(up, {})
    ok2 = sum(abs(v) for v in w.values()) <= 1 + 1e-12 and set(w) == set(PAIRS)
    print(f"[{'PASS' if ok1 else 'FAIL'}] unknown strategy rejected")
    print(f"[{'PASS' if ok2 else 'FAIL'}] s3v2 on a steady uptrend: {w} (gross <= 1)")
    return ok1 and ok2


def test_env_file_gate() -> bool:
    """Competition configs read keys from env_file (.env.competition): a missing file stops the
    bot before any request; a key file with an unknown label is refused."""
    import subprocess
    import tempfile
    here = Path(__file__).resolve().parent.parent
    missing = not (here / ".env.competition").exists()
    if missing:
        r = subprocess.run([sys.executable, "bot.py", "--config", "config_competition.yaml", "--dry-run",
                            "--max-cycles", "0"], cwd=here, capture_output=True, text=True, timeout=120)
        ok1 = r.returncode == 2 and "SAFETY" in (r.stdout + r.stderr)
    else:
        ok1 = True                    # a real .env.competition exists here: don't start the bot
    saved = {k: os.environ.pop(k, None) for k in ("ROOSTOO_API_KEY", "ROOSTOO_API_SECRET", "ROOSTOO_KEY_LABEL")}
    d = Path(tempfile.mkdtemp())
    f = d / ".env.x"
    f.write_text("ROOSTOO_API_KEY=abcd1234\nROOSTOO_API_SECRET=s\nROOSTOO_KEY_LABEL=bogus\n")
    try:
        build_client(True, d / "api.jsonl", f)
        ok2 = False
    except KeySafetyError:
        ok2 = True
    finally:
        for k, v in saved.items():
            if v is not None:
                os.environ[k] = v
    print(f"[{'PASS' if ok1 else 'FAIL'}] env_file missing -> bot refuses to start (exit 2)"
          f"{' (skipped: .env.competition present)' if not missing else ''}")
    print(f"[{'PASS' if ok2 else 'FAIL'}] env_file with an unknown key label -> refused")
    return ok1 and ok2


if __name__ == "__main__":
    ok = test_no_resend_after_timeout() & test_key_gate() & test_plugin_contract() & test_env_file_gate()
    print(f"\nsafety tests: {'PASS' if ok else 'FAIL'}")
    sys.exit(0 if ok else 1)
