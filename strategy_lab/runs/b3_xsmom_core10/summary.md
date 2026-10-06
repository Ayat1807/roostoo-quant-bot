# Run: b3_xsmom_core10

Strategy `xsmom`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +487.92% | +30.58% | 0.95 | 1.33 | -49.89% | 0.61 | 1.00 |
| in_sample | 2020-02-15 → 2024-12-31 | +729.01% | +54.22% | 1.35 | 1.90 | -47.82% | 1.13 | 1.50 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -29.16% | -17.81% | -0.72 | -0.99 | -48.23% | -0.37 | -0.72 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -19.70% | -19.70% | -0.98 | -1.36 | -39.08% | -0.50 | -0.99 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.00% | 41% | -21.31% | -22.40% | -3.04 | 11 | 23% |
| out_of_sample | 628 | -1.94% | 37% | -9.74% | -11.64% | -5.86 | 10 | 5% |
| in_sample | 1768 | -0.86% | 43% | -21.31% | -22.40% | -2.44 | 12 | 29% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.618% | 40% | 3.61 | +170.47% |
| bull | 687 | 28% | +0.297% | 48% | 2.84 | +571.15% |
| bear | 400 | 17% | -0.182% | 25% | -3.15 | -52.92% |
| chop | 1160 | 48% | -0.019% | 31% | -0.28 | -27.04% |

## Turnover, fees, activity

- trades: 11473 (4.73/day); active days 76%
- turnover 127.1x equity/year; fees 12.71% of equity/year ($229,671 total)
- average gross exposure 0.27; brake active 45.5% of hours
- correlation of daily returns with s3v2 baseline: 0.38
