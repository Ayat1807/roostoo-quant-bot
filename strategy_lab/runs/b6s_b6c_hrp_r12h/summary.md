# Run: b6s_b6c_hrp_r12h

Strategy `s3v2x_alloc`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'alloc': 'hrp'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +143.85% | +14.37% | 0.93 | 1.37 | -20.94% | 0.69 | 1.04 |
| in_sample | 2020-02-15 → 2024-12-31 | +124.30% | +17.99% | 1.13 | 1.66 | -20.94% | 0.86 | 1.26 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +8.85% | +4.94% | 0.39 | 0.57 | -14.81% | 0.33 | 0.44 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +16.21% | +16.21% | 0.92 | 1.37 | -14.81% | 1.09 | 1.15 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.31% | 44% | -5.40% | -6.50% | -1.92 | 14 | 100% |
| out_of_sample | 628 | -0.55% | 41% | -4.93% | -6.10% | -2.86 | 14 | 100% |
| in_sample | 1768 | -0.22% | 45% | -5.40% | -6.50% | -1.45 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.354% | 55% | 4.22 | +82.29% |
| bull | 687 | 28% | +0.072% | 50% | 1.94 | +61.14% |
| bear | 400 | 17% | +0.026% | 45% | 0.69 | +9.82% |
| chop | 1160 | 48% | -0.019% | 40% | -0.48 | -22.45% |

## Turnover, fees, activity

- trades: 7281 (3.00/day); active days 100%
- turnover 78.9x equity/year; fees 7.89% of equity/year ($48,248 total)
- average gross exposure 0.20; brake active 13.3% of hours
- correlation of daily returns with s3v2 baseline: 0.79
