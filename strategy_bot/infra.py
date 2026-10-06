"""Shared plumbing, reused from pipeline_bot: JSONL logs, rotating bot.log, atomic JSON
writes and the key-label safety gate."""

from __future__ import annotations

import json
import logging
import os
import sys
import time
import traceback
from datetime import datetime, timezone
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Any

from roostoo_client import KeySafetyError, RoostooClient, append_log

log = logging.getLogger("strategy_bot")


def utc_iso(ts: float | None = None) -> str:
    return datetime.fromtimestamp(ts or time.time(), tz=timezone.utc).isoformat(timespec="seconds")


def replace_with_retry(tmp: Path, path: Path, attempts: int = 10) -> None:
    """os.replace, retried briefly: on Windows a just-written file can be locked for a
    moment by antivirus/indexers (WinError 5). No-op difference on Linux."""
    for i in range(attempts):
        try:
            os.replace(tmp, path)
            return
        except PermissionError:
            if i == attempts - 1:
                raise
            time.sleep(0.05 * (i + 1))


def write_json_atomic(path: Path, data: Any) -> None:
    """Temp file + rename, so readers (status.py) never see a half-written file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=2, default=str), encoding="utf-8")
    replace_with_retry(tmp, path)


class JsonlLogs:
    """decisions / orders / equity / errors .jsonl, one record per line.

    `clock` lets replays stamp records with simulated time; `ts` is always wall-clock ms
    (status.py uses it for the 24h error count)."""

    def __init__(self, log_dir: Path, clock: Any = None) -> None:
        self.dir = Path(log_dir)
        self.dir.mkdir(parents=True, exist_ok=True)
        self.clock = clock

    def write(self, name: str, record: dict[str, Any]) -> None:
        t = self.clock().isoformat() if self.clock else utc_iso()
        append_log({"time": t, "ts": int(time.time() * 1000), **record}, self.dir / f"{name}.jsonl")

    def error(self, where: str, exc: BaseException) -> None:
        self.write("errors", {"where": where, "type": type(exc).__name__,
                              "message": str(exc)[:1000],
                              "traceback": traceback.format_exc()[-4000:]})


def setup_logging(log_dir: Path, max_bytes: int, backups: int) -> None:
    log_dir.mkdir(parents=True, exist_ok=True)
    fmt = logging.Formatter("%(asctime)s %(levelname)-7s %(name)s: %(message)s", "%Y-%m-%d %H:%M:%S")
    fh = RotatingFileHandler(log_dir / "bot.log", maxBytes=max_bytes, backupCount=backups,
                             encoding="utf-8")
    fh.setFormatter(fmt)
    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(fmt)
    root = logging.getLogger("strategy_bot")
    root.handlers[:] = [fh, sh]
    root.setLevel(logging.INFO)


def build_client(allow_competition: bool, api_log: Path, env_path: Path | None = None) -> RoostooClient:
    """Key-label gate: 'testing' always; 'competition' only with allow_competition: true,
    after a 10-second warning. Anything else is refused. `env_path`: the key file (default
    strategy_bot/.env; the competition configs use .env.competition)."""
    label = RoostooClient.from_env(env_path).key_label
    if label == "testing":
        allowed: tuple[str, ...] = ("testing",)
    elif label == "competition":
        if not allow_competition:
            raise KeySafetyError("ROOSTOO_KEY_LABEL=competition but config has "
                                 "allow_competition: false. Refusing to start.")
        allowed = ("competition",)
        print("\n" + "!" * 70 + "\n  WARNING: COMPETITION KEY. Real scored account.\n"
              "  Press Ctrl+C within 10 seconds to abort.\n" + "!" * 70, flush=True)
        for i in range(10, 0, -1):
            print(f"  starting in {i}...", flush=True)
            time.sleep(1)
    else:
        raise KeySafetyError(f"ROOSTOO_KEY_LABEL={label!r}: must be 'testing' "
                             "(or 'competition' with allow_competition: true).")
    client = RoostooClient.from_env(env_path, allowed_labels=allowed, log_path=api_log)
    client.assert_key_allowed()
    return client
