# Roostoo API: initial testing findings

_Generated 2026-10-04 09:04:53 UTC by `generate_findings.py` from `logs/` (23 logged requests). Re-run after each test to refresh._

## 1. Connectivity and clock

- Base URL `https://mock-api.roostoo.com`: 18/18 Roostoo requests returned HTTP 200.
- HTTP status counts: {'200': 18}
- Clock offset (server - local): **-111 ms** (samples [359, -264, -111]); well inside the +-60 s window. The client still applies the offset to every timestamp.
- `IsRunning`=True, `InitialWallet`={'USD': 50000}

## 2. Trading pairs and order rules

**88 pairs** in exchangeInfo, **86** in the all-pairs ticker.

AssetType counts: {'crypto': 67, 'stock': 21}

Full list: `1000CHEEMS/USD`, `AAVE/USD`, `ADA/USD`, `AMDB/USD`, `APT/USD`, `ARB/USD`, `ASTER/USD`, `AVAX/USD`, `AVNT/USD`, `BIO/USD`, `BMT/USD`, `BNB/USD`, `BONK/USD`, `BTC/USD`, `CAKE/USD`, `CBRSB/USD`, `CFX/USD`, `COINB/USD`, `CRCLB/USD`, `CRV/USD`, `DOGE/USD`, `DOT/USD`, `EDEN/USD`, `EIGEN/USD`, `ENA/USD`, `ETH/USD`, `FET/USD`, `FIL/USD`, `FLOKI/USD`, `FORM/USD`, `GLWB/USD`, `GOOGLB/USD`, `HBAR/USD`, `HEMI/USD`, `ICP/USD`, `INTCB/USD`, `LINEA/USD`, `LINK/USD`, `LISTA/USD`, `LITEB/USD`, `LTC/USD`, `METAB/USD`, `MIRA/USD`, `MSFTB/USD`, `MSTRB/USD`, `MUB/USD`, `NBISB/USD`, `NEAR/USD`, `NVDAB/USD`, `OMNI/USD`, `ONDO/USD`, `OPEN/USD`, `PAXG/USD`, `PENDLE/USD`, `PENGU/USD`, `PEPE/USD`, `PLTRB/USD`, `PLUME/USD`, `POL/USD`, `PUMP/USD`, `QCOMB/USD`, `S/USD`, `SEI/USD`, `SHIB/USD`, `SKHYB/USD`, `SNDKB/USD`, `SOL/USD`, `SOMI/USD`, `SPCXB/USD`, `STO/USD`, `SUI/USD`, `TAO/USD`, `TON/USD`, `TRUMP/USD`, `TRX/USD`, `TSLAB/USD`, `TUT/USD`, `UNI/USD`, `VIRTUAL/USD`, `WDCB/USD`, `WIF/USD`, `WLD/USD`, `WLFI/USD`, `XLM/USD`, `XPL/USD`, `XRP/USD`, `ZEC/USD`, `ZEN/USD`

Non-crypto pairs (tokenised stocks etc.): AMDB/USD, CBRSB/USD, COINB/USD, CRCLB/USD, GLWB/USD, GOOGLB/USD, INTCB/USD, LITEB/USD, METAB/USD, MSFTB/USD, MSTRB/USD, MUB/USD, NBISB/USD, NVDAB/USD, PLTRB/USD, QCOMB/USD, SKHYB/USD, SNDKB/USD, SPCXB/USD, TSLAB/USD, WDCB/USD

Pairs with CanTrade=false: none

Top 10 by 24h `UnitTradeValue` (USD volume) at snapshot time:

| Pair | 24h USD vol | LastPrice | PricePrecision | AmountPrecision | MiniOrder |
|---|---|---|---|---|---|
| BTC/USD | 591,621,839 | 85069.99 | 2 | 5 | 1 |
| ETH/USD | 191,741,950 | 2699.43 | 2 | 4 | 1 |
| SOL/USD | 114,865,232 | 120.9 | 2 | 3 | 1 |
| ZEC/USD | 109,580,403 | 1329.01 | 2 | 3 | 1 |
| BNB/USD | 77,111,519 | 788.54 | 2 | 3 | 1 |
| NEAR/USD | 72,433,803 | 4.785 | 3 | 1 | 1 |
| WLD/USD | 71,366,443 | 0.5865 | 4 | 1 | 1 |
| XRP/USD | 65,290,949 | 1.4967 | 4 | 1 | 1 |
| SUI/USD | 49,638,018 | 1.1759 | 4 | 1 | 1 |
| PUMP/USD | 40,375,903 | 0.006374 | 6 | 0 | 1 |

MiniOrder values across all pairs: {1: 88} (rule: price x quantity must be > MiniOrder, in USD).

## 3. Observed fees

test_trading.py not run yet (needs `--confirm` and the TESTING key).

## 4. Is shorting allowed?

Unknown: test_trading.py not run yet.

## 5. Response field names (live vs docs)

`<key>` = a pair or coin name. Fields documented but not seen may simply be zero-valued (the API omits zero fields) or the case did not occur.

- `/v3/balance`: `ErrMsg`, `MarginWallet`, `SpotWallet.<key>.Free`, `SpotWallet.<key>.Lock`, `SpotWallet.<key>.PendingOrders`, `SpotWallet.<key>.ShortCollateral`, `Success`
  - **Undocumented, seen live:** MarginWallet, SpotWallet.<key>.Free, SpotWallet.<key>.Lock, SpotWallet.<key>.PendingOrders, SpotWallet.<key>.ShortCollateral
  - Documented, not seen: Wallet.<key>.Free, Wallet.<key>.Lock
- `/v3/cancel_order`: no successful live response logged yet.
- `/v3/exchangeInfo`: `InitialWallet.<key>`, `IsRunning`, `TradePairs.<key>.AmountPrecision`, `TradePairs.<key>.AssetType`, `TradePairs.<key>.CanTrade`, `TradePairs.<key>.Coin`, `TradePairs.<key>.CoinFullName`, `TradePairs.<key>.MiniOrder`, `TradePairs.<key>.PricePrecision`, `TradePairs.<key>.Unit`, `TradePairs.<key>.UnitFullName`
  - **Undocumented, seen live:** TradePairs.<key>.AssetType
- `/v3/pending_count`: no successful live response logged yet.
- `/v3/place_order`: no successful live response logged yet.
- `/v3/query_order`: no successful live response logged yet.
- `/v3/serverTime`: `ServerTime`
- `/v3/ticker`: `Data.<key>.Change`, `Data.<key>.CoinTradeValue`, `Data.<key>.LastPrice`, `Data.<key>.MaxBid`, `Data.<key>.MinAsk`, `Data.<key>.UnitTradeValue`, `ErrMsg`, `ServerTime`, `Success`
- `/v6/short_close`: no successful live response logged yet.
- `/v6/short_open`: no successful live response logged yet.
- `/v6/short_positions`: `Positions[]`, `Success`
  - **Undocumented, seen live:** Positions[]
  - Documented, not seen: Positions[].Collateral, Positions[].CreateTimestamp, Positions[].CurrentPrice, Positions[].EntryPrice, Positions[].ID, Positions[].Pair, Positions[].PositionStatus, Positions[].PositionValue, Positions[].ShortQty, Positions[].UnrealizedPNL, Positions[].UnrealizedPNLPct

## 6. ErrMsg / errors encountered

| Endpoint | ErrMsg | Count | Params (example) |
|---|---|---|---|
| `/v3/pending_count` | no pending order under this account | 2 | `{}` |

`no pending order under this account` and `no order matched` are documented 'empty' answers (Success=false), not failures.

## 7. Latency per endpoint (ms)

| Endpoint | Calls | Mean | Median | p95 | Max |
|---|---|---|---|---|---|
| `/v3/balance` | 2 | 507 | 507 | 659 | 659 |
| `/v3/exchangeInfo` | 1 | 684 | 684 | 684 | 684 |
| `/v3/pending_count` | 2 | 554 | 554 | 655 | 655 |
| `/v3/serverTime` | 6 | 1007 | 1042 | 1667 | 1667 |
| `/v3/ticker` | 5 | 732 | 692 | 1524 | 1524 |
| `/v6/short_positions` | 2 | 522 | 522 | 691 | 691 |
| `api.binance.com/api/v3/klines` | 4 | 1151 | 959 | 1744 | 1744 |
| `data-api.binance.vision/api/v3/klines` | 1 | 2701 | 2701 | 2701 | 2701 |

Measured from a home connection; latency from AWS will differ.

## 8. Binance data vs Roostoo prices

- `https://api.binance.com/api/v3/klines`: OK, 48 hourly rows 2026-10-02 09:00 -> 2026-10-04 08:00 UTC
- `https://data-api.binance.vision/api/v3/klines`: OK, 48 hourly rows 2026-10-02 09:00 -> 2026-10-04 08:00 UTC

| Pair | Roostoo LastPrice | Binance last 1h close | Diff % | Binance 48h low-high |
|---|---|---|---|---|
| BTC/USD | 85070.0 | 85070.0 | +0.0000% | 84262.01-86810.0 |
| ETH/USD | 2699.44 | 2699.43 | +0.0004% | 2661.74-2755.18 |
| SOL/USD | 120.95 | 120.95 | +0.0000% | 117.77-122.56 |

Max abs difference 0.0004%. Roostoo prices track Binance USDT spot almost exactly, so Binance klines can seed indicators.

## 9. Testing account snapshot

- USD Free 49,999.99, Lock 0.00; wallet value $49,999.99; other holdings: none
- Pending: {'TotalPending': 0.0, 'OrderPairs': {}, 'ErrMsg': 'no pending order under this account'}
- Short positions: []

## 10. Live API vs documentation

- Pairs listed in exchangeInfo with `CanTrade=true` but absent from the ticker: OMNI/USD, TON/USD. Do not trade them.
- `/v3/balance` returns undocumented fields: MarginWallet, SpotWallet.<key>.Free, SpotWallet.<key>.Lock, SpotWallet.<key>.PendingOrders, SpotWallet.<key>.ShortCollateral
- `/v3/exchangeInfo` returns undocumented fields: TradePairs.<key>.AssetType
- `/v6/short_positions` returns undocumented fields: Positions[]

## 11. Open questions for the organizers

1. What are the rate limits (requests per second/minute, per key or per IP)? What happens when we exceed them (HTTP 429, ErrMsg, ban)?
2. Does the **competition** account allow short positions (`/v6/short_*`), or will it return `this competition does not allow short positions`?
3. What counts as "enough trades per day"? Is there a minimum number of orders, fills or notional, and does a canceled order count?
4. Are fees on the competition account the same as testing (taker 0.1%, maker 0.05%, short 0.1%)?
5. Is the leaderboard scored on total portfolio value at LastPrice, at bid, or something else? How are open shorts and locked collateral valued?
6. Are OMNI/USD and TON/USD (and any other pairs missing from the ticker) tradeable? Will the pair list change during the competition?
7. Is the Roostoo price feed derived from Binance spot (the match is near-exact)? If so, is using Binance historical data and live data allowed?
8. Do LIMIT orders fill against real Binance order-book moves or only on LastPrice crossing our price? Is there partial-fill behaviour?
9. Is there a maximum number of open orders per account or per pair?
10. The exchange lists tokenised stocks (`AssetType: stock`, e.g. NVDAB/USD, TSLAB/USD). Do they trade 24/7 or only in market hours, where does their price come from, and do they count toward scoring like crypto?
11. Will the bot's own automated calls on the competition key from AWS be whitelisted by IP, and what exactly counts as a disqualifying 'manual' call?
