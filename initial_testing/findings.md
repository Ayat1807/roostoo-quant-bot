# Roostoo API: initial testing findings

_Generated 2026-10-04 09:50:26 UTC by `generate_findings.py` from `logs/` (60 logged requests). Re-run after each test to refresh._

## 1. Connectivity and clock

- Base URL `https://mock-api.roostoo.com`: 55/55 Roostoo requests returned HTTP 200.
- HTTP status counts: {'200': 55}
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

| Fee type | Fills | Implied fee (fee / notional) | CommissionPercent field | Total fee USD |
|---|---|---|---|---|
| short_close | 2 | 0.1000% | n/a | 0.019621 |
| short_open | 1 | 0.1000% | n/a | 0.019622 |
| spot_maker | 1 | 0.0500% | 0.0005 | 0.007251 |
| spot_taker | 3 | 0.1000% | 0.001 | 0.043509 |

Expected: taker 0.1%, maker 0.05%, short open/close 0.1%.

- Market BUY filled at 85316.01 vs ticker ask 85316.01 (+0.0000%).
- Market SELL filled at 85316.0 vs ticker bid 85316.0 (+0.0000%).
- Limit/cancel lifecycle: placed status `PENDING`, after cancel `CANCELED`, CanceledList=[3421109].
- Reconciliation: USD spent 0.090000; explained by fees 0.090003, spot PnL -0.000002, short PnL -0.000002, retained coin 0.000000 -> unexplained **-0.000007 USD**. Total test notional $98.92.

## 4. Is shorting allowed?

**Yes** on the testing account: short_open, partial close (50%) and final close all succeeded. Positions after close: `[]`.

- Requested collateral $20 -> response `Collateral`=19.62, `ShortQty`=0.00023, `EntryPrice`=85316, `OpenFee`=0.019622. Collateral is re-computed as ShortQty x EntryPrice after rounding the quantity DOWN, so slightly less than requested is locked (1x, no leverage).
- Entry vs bid: +0.0000% (fills at MaxBid); closes fill at MinAsk, so every short round trip pays the spread + 0.2%.

This does NOT prove the competition account allows shorts; ask organizers.

## 5. Response field names (live vs docs)

`<key>` = a pair or coin name. Fields documented but not seen may simply be zero-valued (the API omits zero fields) or the case did not occur.

- `/v3/balance`: `ErrMsg`, `MarginWallet`, `SpotWallet.<key>.Free`, `SpotWallet.<key>.Lock`, `SpotWallet.<key>.PendingOrders`, `SpotWallet.<key>.ShortCollateral`, `Success`
  - **Undocumented, seen live:** MarginWallet, SpotWallet.<key>.Free, SpotWallet.<key>.Lock, SpotWallet.<key>.PendingOrders, SpotWallet.<key>.ShortCollateral
  - Documented, not seen: Wallet.<key>.Free, Wallet.<key>.Lock
- `/v3/cancel_order`: `CanceledList[]`, `ErrMsg`, `Success`
- `/v3/exchangeInfo`: `InitialWallet.<key>`, `IsRunning`, `TradePairs.<key>.AmountPrecision`, `TradePairs.<key>.AssetType`, `TradePairs.<key>.CanTrade`, `TradePairs.<key>.Coin`, `TradePairs.<key>.CoinFullName`, `TradePairs.<key>.MiniOrder`, `TradePairs.<key>.PricePrecision`, `TradePairs.<key>.Unit`, `TradePairs.<key>.UnitFullName`
  - **Undocumented, seen live:** TradePairs.<key>.AssetType
- `/v3/pending_count`: no successful live response logged yet.
- `/v3/place_order`: `ErrMsg`, `OrderDetail.CoinChange`, `OrderDetail.CommissionChargeValue`, `OrderDetail.CommissionCoin`, `OrderDetail.CommissionPercent`, `OrderDetail.CreateTimestamp`, `OrderDetail.FilledAverPrice`, `OrderDetail.FilledQuantity`, `OrderDetail.FinishTimestamp`, `OrderDetail.OrderID`, `OrderDetail.OrderSource`, `OrderDetail.OrderWalletType`, `OrderDetail.Pair`, `OrderDetail.Price`, `OrderDetail.Quantity`, `OrderDetail.Role`, `OrderDetail.ServerTimeUsage`, `OrderDetail.Side`, `OrderDetail.Status`, `OrderDetail.StopType`, `OrderDetail.Type`, `OrderDetail.UnitChange`, `Success`
  - **Undocumented, seen live:** OrderDetail.OrderSource, OrderDetail.OrderWalletType
- `/v3/query_order`: `ErrMsg`, `OrderMatched[].CoinChange`, `OrderMatched[].CommissionChargeValue`, `OrderMatched[].CommissionCoin`, `OrderMatched[].CommissionPercent`, `OrderMatched[].CreateTimestamp`, `OrderMatched[].FilledAverPrice`, `OrderMatched[].FilledQuantity`, `OrderMatched[].FinishTimestamp`, `OrderMatched[].OrderID`, `OrderMatched[].OrderSource`, `OrderMatched[].OrderWalletType`, `OrderMatched[].Pair`, `OrderMatched[].Price`, `OrderMatched[].Quantity`, `OrderMatched[].Role`, `OrderMatched[].ServerTimeUsage`, `OrderMatched[].Side`, `OrderMatched[].Status`, `OrderMatched[].StopType`, `OrderMatched[].Type`, `OrderMatched[].UnitChange`, `Success`
  - **Undocumented, seen live:** OrderMatched[].OrderSource, OrderMatched[].OrderWalletType
- `/v3/serverTime`: `ServerTime`
- `/v3/ticker`: `Data.<key>.Change`, `Data.<key>.CoinTradeValue`, `Data.<key>.LastPrice`, `Data.<key>.MaxBid`, `Data.<key>.MinAsk`, `Data.<key>.UnitTradeValue`, `ErrMsg`, `ServerTime`, `Success`
- `/v6/short_close`: `CloseFee`, `ClosePrice`, `ClosedQty`, `FullyClosed`, `RealizedPNL`, `RemainingCollateral`, `RemainingQty`, `ReturnAmount`, `Success`
- `/v6/short_open`: `Collateral`, `CreateTimestamp`, `EntryPrice`, `ID`, `OpenFee`, `OrderType`, `Pair`, `ShortQty`, `Status`, `Success`
- `/v6/short_positions`: `Positions[]`, `Positions[].Collateral`, `Positions[].CreateTimestamp`, `Positions[].CurrentPrice`, `Positions[].EntryPrice`, `Positions[].ID`, `Positions[].Pair`, `Positions[].PositionStatus`, `Positions[].PositionValue`, `Positions[].ShortQty`, `Positions[].UnrealizedPNL`, `Positions[].UnrealizedPNLPct`, `Success`
  - **Undocumented, seen live:** Positions[]

## 6. ErrMsg / errors encountered

| Endpoint | ErrMsg | Count | Params (example) |
|---|---|---|---|
| `/v3/pending_count` | no pending order under this account | 4 | `{}` |
| `/v3/place_order` | price should not less than market price 30% | 1 | `{"pair": "BTC/USD", "side": "BUY", "type": "LIMIT", "quantity": "0.00003", "price": "42658"}` |

`no pending order under this account` and `no order matched` are documented 'empty' answers (Success=false), not failures.

- `price should not less than market price 30%`: Undocumented rule: a LIMIT price may not be more than 30% below market (seen with a BUY at 50% of bid; 75% works). Expect a symmetric cap above market for SELLs.

## 7. Latency per endpoint (ms)

| Endpoint | Calls | Mean | Median | p95 | Max |
|---|---|---|---|---|---|
| `/v3/balance` | 10 | 460 | 367 | 700 | 700 |
| `/v3/cancel_order` | 1 | 364 | 364 | 364 | 364 |
| `/v3/exchangeInfo` | 3 | 577 | 684 | 688 | 688 |
| `/v3/pending_count` | 4 | 623 | 671 | 694 | 694 |
| `/v3/place_order` | 6 | 1288 | 1235 | 1932 | 1932 |
| `/v3/query_order` | 3 | 584 | 687 | 694 | 694 |
| `/v3/serverTime` | 8 | 1148 | 1497 | 1667 | 1667 |
| `/v3/ticker` | 12 | 653 | 682 | 718 | 1524 |
| `/v6/short_close` | 2 | 1862 | 1862 | 1881 | 1881 |
| `/v6/short_open` | 1 | 1490 | 1490 | 1490 | 1490 |
| `/v6/short_positions` | 5 | 553 | 684 | 691 | 691 |
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
- `/v6/short_open` returns `Collateral` = ShortQty x EntryPrice (after rounding qty down), not the requested collateral.
- `/v3/balance` returns undocumented fields: MarginWallet, SpotWallet.<key>.Free, SpotWallet.<key>.Lock, SpotWallet.<key>.PendingOrders, SpotWallet.<key>.ShortCollateral
- `/v3/exchangeInfo` returns undocumented fields: TradePairs.<key>.AssetType
- `/v3/place_order` returns undocumented fields: OrderDetail.OrderSource, OrderDetail.OrderWalletType
- `/v3/query_order` returns undocumented fields: OrderMatched[].OrderSource, OrderMatched[].OrderWalletType
- `/v6/short_positions` returns undocumented fields: Positions[]
- `/v3/place_order`: Undocumented rule: a LIMIT price may not be more than 30% below market (seen with a BUY at 50% of bid; 75% works). Expect a symmetric cap above market for SELLs.

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
