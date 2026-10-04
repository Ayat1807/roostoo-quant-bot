"""Small reusable client for the Roostoo mock exchange API.

Reference: https://github.com/roostoo/Roostoo-API-Documents

Design notes
------------
* Signing: params are sorted by key and joined as ``k=v&k=v``; the HMAC-SHA256
  hex digest (key = API secret) goes in the ``MSG-SIGNATURE`` header. POST sends
  that exact string as the form body; GET sends it as the query string.
* Only the documented params of each endpoint are ever sent, because the server
  rebuilds the signature from documented params only.
* Clock: signed requests need a 13-digit ms timestamp within 60 s of server time,
  so we keep an offset measured from ``GET /v3/serverTime``.
* Errors: the API answers business failures with HTTP 200 and ``Success=false``.
  Those raise ``RoostooAPIError`` and are never retried. Only network errors and
  HTTP 5xx are retried, and order-creating calls are NOT retried after the
  request may have reached the server (to avoid duplicate orders).
* Safety: signed requests are refused unless ``ROOSTOO_KEY_LABEL`` is in
  ``allowed_labels`` (default: only "testing"). The bot widens this to include
  "competition" only when its config explicitly allows it.
* Copied from initial_testing/roostoo_client.py; the only change is the
  ``allowed_labels`` safety parameter (replacing ``require_testing_key``).
* Logging: every request/response is appended to ``logs/api_log.jsonl``. The API
  secret is never logged or printed; the API key is masked to its first 4 chars.
"""

from __future__ import annotations

import hashlib
import hmac
import json
import os
import time
from decimal import ROUND_DOWN, ROUND_UP, Decimal
from pathlib import Path
from typing import Any

import requests

BASE_URL = "https://mock-api.roostoo.com"
HERE = Path(__file__).resolve().parent
LOG_DIR = HERE / "logs"
API_LOG = LOG_DIR / "api_log.jsonl"

# ErrMsg values that mean "nothing found" rather than a real failure.
EMPTY_RESULT_MESSAGES = (
    "no pending order under this account",
    "no order matched",
)
SHORTS_DISABLED_MESSAGE = "this competition does not allow short positions"


class RoostooAPIError(Exception):
    """Business-level failure: HTTP 200 but ``Success=false``."""

    def __init__(self, endpoint: str, err_msg: str, response: dict[str, Any]) -> None:
        super().__init__(f"{endpoint}: {err_msg}")
        self.endpoint = endpoint
        self.err_msg = err_msg
        self.response = response


class KeySafetyError(RuntimeError):
    """Raised when a signed request is attempted with a disallowed key label."""


# --------------------------------------------------------------------------- #
# Helpers (pure functions, easy to unit test)
# --------------------------------------------------------------------------- #

def sign(secret: str, params: dict[str, str]) -> tuple[str, str]:
    """Return (totalParams, hex signature) exactly as the docs describe."""
    total_params = "&".join(f"{k}={params[k]}" for k in sorted(params))
    signature = hmac.new(
        secret.encode("utf-8"), total_params.encode("utf-8"), hashlib.sha256
    ).hexdigest()
    return total_params, signature


def mask_key(api_key: str) -> str:
    """Show only the first 4 characters of an API key."""
    return (api_key[:4] + "****") if api_key else ""


def fmt_decimal(value: float | Decimal | str) -> str:
    """Format a number without scientific notation (str(1e-05) would break orders)."""
    d = Decimal(str(value))
    text = format(d, "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return text or "0"


def round_to_precision(value: float, precision: int, down: bool = True) -> Decimal:
    """Round to ``precision`` decimals; DOWN by default (for quantities)."""
    step = Decimal(1).scaleb(-precision)  # e.g. precision 3 -> 0.001
    return Decimal(str(value)).quantize(step, rounding=ROUND_DOWN if down else ROUND_UP)


def round_price(value: float, precision: int) -> Decimal:
    """Round a price to the nearest allowed tick."""
    return Decimal(str(round(value, precision))).quantize(Decimal(1).scaleb(-precision))


def num(d: dict[str, Any], key: str) -> float:
    """Read a numeric field; the API omits zero-valued fields, so missing means 0."""
    v = d.get(key)
    return float(v) if v is not None else 0.0


def extract_wallet(balance_resp: dict[str, Any]) -> dict[str, Any]:
    """Coin -> {Free, Lock, ...} from a balance response.

    The docs show ``Wallet``; the live API returns ``SpotWallet`` (with extra
    ``PendingOrders`` and ``ShortCollateral`` fields) plus ``MarginWallet``.
    Prefer the live field, fall back to the documented one.
    """
    return balance_resp.get("SpotWallet") or balance_resp.get("Wallet") or {}


def append_log(record: dict[str, Any], path: Path = API_LOG) -> None:
    """Append one JSON record to a JSONL log file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, default=str) + "\n")


# --------------------------------------------------------------------------- #
# Client
# --------------------------------------------------------------------------- #

class RoostooClient:
    """Thin wrapper around every documented Roostoo endpoint."""

    def __init__(
        self,
        api_key: str = "",
        api_secret: str = "",
        key_label: str = "",
        base_url: str = BASE_URL,
        timeout: float = 10.0,
        max_retries: int = 3,
        allowed_labels: tuple[str, ...] = ("testing",),
        log_path: Path = API_LOG,
    ) -> None:
        self.api_key = api_key
        self._api_secret = api_secret  # never logged or printed
        self.key_label = key_label
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries
        self.allowed_labels = allowed_labels
        self.log_path = log_path
        self.clock_offset_ms = 0  # server_time - local_time
        self.session = requests.Session()

    def __repr__(self) -> str:  # keep secrets out of tracebacks/prints
        return f"RoostooClient(key={mask_key(self.api_key)}, label={self.key_label!r})"

    # ----- construction ---------------------------------------------------- #

    @classmethod
    def from_env(cls, env_path: Path | None = None, **kwargs: Any) -> "RoostooClient":
        """Build a client from pipeline_bot/.env (python-dotenv)."""
        from dotenv import load_dotenv

        load_dotenv(env_path or HERE / ".env", override=False)
        return cls(
            api_key=os.getenv("ROOSTOO_API_KEY", "").strip(),
            api_secret=os.getenv("ROOSTOO_API_SECRET", "").strip(),
            key_label=os.getenv("ROOSTOO_KEY_LABEL", "").strip(),
            **kwargs,
        )

    def assert_key_allowed(self) -> None:
        """Refuse to sign anything unless the key label is explicitly allowed."""
        if self.key_label not in self.allowed_labels:
            raise KeySafetyError(
                f"REFUSED: ROOSTOO_KEY_LABEL is {self.key_label!r}; allowed here: "
                f"{list(self.allowed_labels)}. Any manual call with the COMPETITION key "
                "can disqualify the team. Fix pipeline_bot/.env and retry."
            )
        if not self.api_key or not self._api_secret:
            raise KeySafetyError(
                "ROOSTOO_API_KEY / ROOSTOO_API_SECRET missing. Copy .env.example to "
                ".env inside pipeline_bot/ and fill in the key pair."
            )

    # ----- clock ----------------------------------------------------------- #

    def sync_clock(self) -> int:
        """Measure server-local clock offset (ms) using the request midpoint."""
        t0 = time.time() * 1000
        resp = self.server_time()
        t1 = time.time() * 1000
        self.clock_offset_ms = int(resp["ServerTime"] - (t0 + t1) / 2)
        return self.clock_offset_ms

    def timestamp(self) -> str:
        """13-digit ms timestamp corrected by the measured clock offset."""
        return str(int(time.time() * 1000) + self.clock_offset_ms)

    # ----- core request ---------------------------------------------------- #

    def _request(
        self,
        method: str,
        path: str,
        params: dict[str, Any] | None = None,
        *,
        signed: bool = False,
        with_timestamp: bool = False,
        retry_after_send: bool = True,
    ) -> dict[str, Any]:
        """Send one API call with retries, logging and Success checking.

        retry_after_send=False is used for order-creating endpoints: we only
        retry if the connection could not be established at all, never after a
        read timeout, dropped connection or 5xx, since the order may already exist.
        """
        if signed:
            self.assert_key_allowed()

        clean = {k: str(v) for k, v in (params or {}).items() if v is not None}
        url = self.base_url + path
        last_exc: Exception | None = None

        for attempt in range(1, self.max_retries + 1):
            # Fresh timestamp/signature on every attempt (60 s window).
            payload = dict(clean)
            if signed or with_timestamp:
                payload["timestamp"] = self.timestamp()
            headers: dict[str, str] = {}
            total_params = "&".join(f"{k}={payload[k]}" for k in sorted(payload))
            if signed:
                total_params, signature = sign(self._api_secret, payload)
                headers["RST-API-KEY"] = self.api_key
                headers["MSG-SIGNATURE"] = signature

            record: dict[str, Any] = {
                "ts": int(time.time() * 1000),
                "method": method,
                "endpoint": path,
                "params": payload,  # never contains secrets
                "signed": signed,
                "api_key": mask_key(self.api_key) if signed else None,
                "attempt": attempt,
            }
            start = time.perf_counter()
            try:
                if method == "GET":
                    full_url = f"{url}?{total_params}" if total_params else url
                    r = self.session.get(full_url, headers=headers, timeout=self.timeout)
                else:
                    headers["Content-Type"] = "application/x-www-form-urlencoded"
                    r = self.session.post(url, data=total_params, headers=headers,
                                          timeout=self.timeout)
            except requests.RequestException as exc:
                record.update(latency_ms=round((time.perf_counter() - start) * 1000, 1),
                              http_status=None, error=f"{type(exc).__name__}: {exc}")
                append_log(record, self.log_path)
                last_exc = exc
                # A ConnectTimeout means the request never reached the server, so
                # even order-creating calls are safe to resend in that case.
                safe_to_retry = retry_after_send or isinstance(exc, requests.ConnectTimeout)
                if safe_to_retry and attempt < self.max_retries:
                    time.sleep(0.5 * 2 ** (attempt - 1))
                    continue
                raise

            record["latency_ms"] = round((time.perf_counter() - start) * 1000, 1)
            record["http_status"] = r.status_code
            try:
                body: Any = r.json()
            except ValueError:
                body = {"_raw_text": r.text[:2000]}
            record["response"] = body
            append_log(record, self.log_path)

            if r.status_code >= 500:
                last_exc = requests.HTTPError(f"HTTP {r.status_code} on {path}")
                if retry_after_send and attempt < self.max_retries:
                    time.sleep(0.5 * 2 ** (attempt - 1))
                    continue
                raise last_exc
            if r.status_code >= 400:
                raise requests.HTTPError(f"HTTP {r.status_code} on {path}: {r.text[:300]}")
            if not isinstance(body, dict):
                raise RoostooAPIError(path, "non-object JSON response", {"body": body})

            # Business-level check. Endpoints without a Success field
            # (serverTime, exchangeInfo) pass through unchanged.
            if body.get("Success") is False:
                err = str(body.get("ErrMsg", ""))
                if err in EMPTY_RESULT_MESSAGES:
                    return body  # documented "empty" answer, not an error
                raise RoostooAPIError(path, err, body)
            return body

        raise RuntimeError(f"retries exhausted for {path}") from last_exc

    # ----- public endpoints ------------------------------------------------ #

    def server_time(self) -> dict[str, Any]:
        return self._request("GET", "/v3/serverTime")

    def exchange_info(self) -> dict[str, Any]:
        return self._request("GET", "/v3/exchangeInfo")

    def ticker(self, pair: str | None = None) -> dict[str, Any]:
        """Unsigned, but the timestamp param is mandatory."""
        return self._request("GET", "/v3/ticker", {"pair": pair}, with_timestamp=True)

    # ----- signed, read-only ----------------------------------------------- #

    def balance(self) -> dict[str, Any]:
        return self._request("GET", "/v3/balance", signed=True)

    def pending_count(self) -> dict[str, Any]:
        return self._request("GET", "/v3/pending_count", signed=True)

    def query_order(
        self,
        order_id: int | str | None = None,
        pair: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        pending_only: bool | None = None,
    ) -> dict[str, Any]:
        """If order_id is given, no other optional param may be sent."""
        if order_id is not None:
            params: dict[str, Any] = {"order_id": order_id}
        else:
            params = {
                "pair": pair,
                "offset": offset,
                "limit": limit,
                "pending_only": None if pending_only is None
                else ("TRUE" if pending_only else "FALSE"),
            }
        return self._request("POST", "/v3/query_order", params, signed=True)

    def short_positions(self) -> dict[str, Any]:
        return self._request("GET", "/v6/short_positions", signed=True)

    # ----- signed, trading ------------------------------------------------- #

    def place_order(
        self,
        pair: str,
        side: str,
        quantity: Decimal | float | str,
        order_type: str = "MARKET",
        price: Decimal | float | str | None = None,
    ) -> dict[str, Any]:
        order_type = order_type.upper()
        if order_type == "LIMIT" and price is None:
            raise ValueError("LIMIT orders require a price")
        params = {
            "pair": pair,
            "side": side.upper(),
            "type": order_type,
            "quantity": fmt_decimal(quantity),
            "price": fmt_decimal(price) if order_type == "LIMIT" else None,
        }
        return self._request("POST", "/v3/place_order", params, signed=True,
                             retry_after_send=False)

    def cancel_order(self, order_id: int | str | None = None,
                     pair: str | None = None) -> dict[str, Any]:
        """Cancel by order_id OR pair. Sending neither would cancel ALL orders,
        so this client refuses that on purpose."""
        if (order_id is None) == (pair is None):
            raise ValueError("cancel_order needs exactly one of order_id or pair")
        params = {"order_id": order_id} if order_id is not None else {"pair": pair}
        return self._request("POST", "/v3/cancel_order", params, signed=True)

    def short_open(
        self,
        pair: str,
        collateral: Decimal | float | str,
        order_type: str | None = None,
        price: Decimal | float | str | None = None,
    ) -> dict[str, Any]:
        """Market short by default; order_type='LIMIT' requires a price."""
        if order_type == "LIMIT" and price is None:
            raise ValueError("LIMIT short requires a price")
        params = {
            "pair": pair,
            "collateral": fmt_decimal(collateral),
            "order_type": "LIMIT" if order_type == "LIMIT" else None,
            "price": fmt_decimal(price) if order_type == "LIMIT" else None,
        }
        return self._request("POST", "/v6/short_open", params, signed=True,
                             retry_after_send=False)

    def short_close(
        self,
        pair: str,
        close_qty: Decimal | float | str | None = None,
        close_pct: float | str | None = None,
    ) -> dict[str, Any]:
        """Send close_qty OR close_pct (or neither = close all of this pair)."""
        params: dict[str, Any] = {"pair": pair}
        if close_qty is not None:
            params["close_qty"] = fmt_decimal(close_qty)
        elif close_pct is not None:
            params["close_pct"] = fmt_decimal(close_pct)
        return self._request("POST", "/v6/short_close", params, signed=True,
                             retry_after_send=False)
