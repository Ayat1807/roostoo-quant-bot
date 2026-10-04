# Roostoo API: initial testing

These scripts check the Roostoo mock-exchange API from end to end and record the real response formats before we write the trading bot. `roostoo_client.py` is the reusable client the bot will build on.
Docs: <https://github.com/roostoo/Roostoo-API-Documents>

## Safety rules (read first)

- Keys are read **only** from `initial_testing/.env`. They are never hardcoded and never printed. In logs the API key is masked to its first 4 characters, and the secret never appears.
- Every signed request is **refused** unless `ROOSTOO_KEY_LABEL=testing`. **Never put the COMPETITION key in this folder.** A manual call with that key can disqualify the team.
- `.env`, `logs/`, `.venv/` and `__pycache__/` are git-ignored by the root `.gitignore`.
- `test_trading.py` places real orders on the testing account. It only runs with `--confirm`, trades only BTC/USD, and stops before total notional reaches $200.

## Setup

Python 3.10+ is required. The commands below are run from `Trading_Competition/initial_testing/`.

**Windows (PowerShell)**
```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1          # if blocked: Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
python -m pip install -r requirements.txt
Copy-Item .env.example .env            # then edit .env with the TESTING key
```

**Linux / macOS**
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env                   # then edit .env with the TESTING key
```

## Run order

| Step | Command | Needs keys | What it checks |
|---|---|---|---|
| 1 | `python test_signature.py` | no (offline) | HMAC signature matches the docs example (`20b7fd55...`). Also checks number formatting, quantity rounding (down), key masking, and that a non-testing label is refused. |
| 2 | `python test_public.py` | no | `serverTime` and clock offset, full `exchangeInfo` (saved to `logs/exchange_info.json`), all-pairs `ticker` (saved to `logs/ticker_snapshot.json`), and a precision/MiniOrder table for the top 10 pairs by `UnitTradeValue`. |
| 3 | `python test_account.py` | testing | Signed read-only calls: `balance`, `pending_count`, `short_positions`. Prints starting USD and holdings. |
| 4 | `python test_data_sources.py` | no | Binance `api.binance.com` and `data-api.binance.vision` 1h klines (48h of BTCUSDT), with closes compared to Roostoo `LastPrice` for BTC/ETH/SOL. |
| 5 | `python test_trading.py --confirm` | testing | (a) limit order, query, cancel, query; (b) market buy then sell, to measure the taker fee and fill vs bid/ask; (c) limit order at the bid, to measure the maker fee if it fills within 2 minutes; (d) short open, close 50%, close the rest; (e) USD reconciliation. |
| 6 | `python generate_findings.py` | no | Builds `findings.md` from `logs/` and prints average latency per endpoint. |

You can re-run `generate_findings.py` after any step. Sections for tests that haven't run yet are marked as such.

## Files

- `roostoo_client.py`: the `RoostooClient` class, which wraps every endpoint (`server_time`, `exchange_info`, `ticker`, `balance`, `pending_count`, `place_order`, `query_order`, `cancel_order`, `short_open`, `short_close`, `short_positions`). It also provides:
  - clock sync (`sync_clock`) and signing
  - retries with backoff, for network errors and HTTP 5xx only. Order-creating calls are never resent once the request may have reached the server, which prevents duplicate orders.
  - `Success`-flag checking: failures raise `RoostooAPIError`; documented "empty" answers are passed through
  - JSONL logging to `logs/api_log.jsonl` (time, endpoint, params, masked key, HTTP code, latency in ms, full response)
  - a refusal to call `cancel_order` with neither `order_id` nor `pair`, which would cancel *all* orders
- `logs/results_*.json`: the machine-readable result of each test, read by `generate_findings.py`.
- `findings.md`: the generated summary.

## API behaviours the client relies on

- Signature: sort the params by key, join them as `k=v&...`, then take the HMAC-SHA256 hex digest using the secret. It goes in the `MSG-SIGNATURE` header, with the key in `RST-API-KEY`. A POST sends the same string as a form body; a GET sends it as the query string.
- Only the documented params of each endpoint are sent, because extra params break the server-side signature.
- HTTP 200 with `Success=false` means a business error. `no pending order under this account` and `no order matched` mean an empty result.
- Zero-valued fields are omitted from responses. Use `num(d, key)`, which treats a missing field as 0.
- Prices are rounded to `PricePrecision` and quantities rounded **down** to `AmountPrecision`. An order must satisfy `price * qty > MiniOrder`.

## Results summary

See [findings.md](findings.md). It covers connectivity, the pair list, observed fees, whether shorting works, live field names vs the docs, errors seen, latency, the Binance price match, and open questions for the organizers.
