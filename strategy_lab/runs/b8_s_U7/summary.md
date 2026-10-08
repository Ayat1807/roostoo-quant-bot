# Run: b8_s_U7

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.04; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +165.21% | +15.82% | 0.87 | 1.25 | -20.62% | 0.77 | 0.99 |
| in_sample | 2020-02-15 → 2024-12-31 | +129.09% | +18.51% | 1.01 | 1.47 | -18.56% | 1.00 | 1.19 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +15.89% | +8.75% | 0.51 | 0.73 | -20.62% | 0.42 | 0.58 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +2.36% | +2.36% | 0.22 | 0.31 | -20.62% | 0.11 | 0.22 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.32% | 44% | -10.03% | -10.73% | -1.65 | 14 | 99% |
| out_of_sample | 628 | -0.62% | 41% | -10.03% | -10.73% | -2.06 | 14 | 100% |
| in_sample | 1768 | -0.25% | 45% | -6.60% | -8.03% | -1.30 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.287% | 53% | 3.16 | +61.43% |
| bull | 687 | 28% | +0.100% | 54% | 2.37 | +94.80% |
| bear | 400 | 17% | +0.034% | 48% | 0.68 | +12.55% |
| chop | 1160 | 48% | -0.018% | 45% | -0.38 | -22.39% |

## Turnover, fees, activity

- trades: 8405 (3.47/day); active days 100%
- turnover 60.9x equity/year; fees 6.09% of equity/year ($37,321 total)
- average gross exposure 0.23; brake active 21.3% of hours
- correlation of daily returns with s3v2 baseline: 0.90
