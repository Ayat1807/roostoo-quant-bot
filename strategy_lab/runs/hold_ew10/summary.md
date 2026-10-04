# Run: hold_ew10

Strategy `hold_ew`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake False; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +2132.13% | +59.63% | 1.02 | 1.39 | -78.49% | 0.76 | 1.09 |
| in_sample | 2020-02-15 → 2024-12-31 | +3460.96% | +107.88% | 1.35 | 1.84 | -78.49% | 1.37 | 1.55 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -37.92% | -23.76% | -0.22 | -0.31 | -65.63% | -0.36 | -0.30 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -41.11% | -41.11% | -0.78 | -1.08 | -65.28% | -0.63 | -0.86 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | +1.28% | 54% | -49.22% | -58.00% | 2.03 | 0 | 0% |
| out_of_sample | 628 | -0.95% | 47% | -31.18% | -31.96% | -0.76 | 0 | 0% |
| in_sample | 1768 | +2.15% | 57% | -49.22% | -58.00% | 3.21 | 0 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.776% | 57% | 1.92 | +130.41% |
| bull | 687 | 28% | +0.791% | 60% | 5.10 | +16558.85% |
| bear | 400 | 17% | -0.516% | 44% | -2.85 | -90.06% |
| chop | 1160 | 48% | +0.005% | 51% | 0.04 | -37.21% |

## Turnover, fees, activity

- trades: 75 (0.03/day); active days 3%
- turnover 0.5x equity/year; fees 0.05% of equity/year ($2,859 total)
- average gross exposure 0.88; brake active 0.0% of hours
- correlation of daily returns with s3v2 baseline: -0.06
