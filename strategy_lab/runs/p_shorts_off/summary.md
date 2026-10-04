# Run: p_shorts_off

Strategy `s3v2`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +217.95% | +19.03% | 1.42 | 2.01 | -17.26% | 1.10 | 1.56 |
| in_sample | 2020-02-15 → 2024-12-31 | +141.18% | +19.76% | 1.50 | 2.10 | -16.16% | 1.22 | 1.66 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +31.81% | +17.02% | 1.22 | 1.78 | -17.26% | 0.99 | 1.37 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +12.19% | +12.19% | 0.89 | 1.29 | -17.26% | 0.71 | 1.00 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.16% | 39% | -4.80% | -6.98% | -4.21 | 13 | 43% |
| out_of_sample | 628 | -0.20% | 31% | -4.38% | -6.98% | -4.86 | 12 | 31% |
| in_sample | 1768 | -0.15% | 41% | -4.80% | -6.59% | -3.90 | 13 | 47% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.238% | 40% | 3.58 | +49.90% |
| bull | 687 | 28% | +0.127% | 56% | 3.51 | +135.16% |
| bear | 400 | 17% | -0.035% | 28% | -3.86 | -13.26% |
| chop | 1160 | 48% | +0.008% | 35% | 0.24 | +7.06% |

## Turnover, fees, activity

- trades: 3216 (1.33/day); active days 84%
- turnover 26.2x equity/year; fees 2.62% of equity/year ($16,410 total)
- average gross exposure 0.11; brake active 4.7% of hours
- correlation of daily returns with s3v2 baseline: 0.61
