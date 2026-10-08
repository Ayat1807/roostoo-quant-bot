# Run: b8_h_U6

Strategy `s3v2x_regime`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'regime_hmm': 2, 'floor_breadth': 7, 'floor_gross': 0.5}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +103.77% | +11.32% | 0.71 | 1.03 | -18.75% | 0.60 | 0.81 |
| in_sample | 2020-02-15 → 2024-12-31 | +60.78% | +10.22% | 0.64 | 0.93 | -18.75% | 0.54 | 0.73 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +26.89% | +14.51% | 0.93 | 1.37 | -12.83% | 1.13 | 1.17 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +14.21% | +14.21% | 0.87 | 1.28 | -12.83% | 1.11 | 1.11 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.29% | 46% | -7.95% | -11.46% | -1.18 | 14 | 100% |
| out_of_sample | 628 | +0.06% | 51% | -5.21% | -5.34% | 0.36 | 14 | 100% |
| in_sample | 1768 | -0.36% | 45% | -7.95% | -11.46% | -1.51 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.396% | 56% | 4.96 | +96.58% |
| bull | 687 | 28% | +0.065% | 53% | 1.49 | +52.35% |
| bear | 400 | 17% | -0.000% | 49% | -0.01 | -1.10% |
| chop | 1160 | 48% | -0.026% | 44% | -0.55 | -29.30% |

## Turnover, fees, activity

- trades: 7531 (3.11/day); active days 100%
- turnover 59.6x equity/year; fees 5.96% of equity/year ($28,588 total)
- average gross exposure 0.22; brake active 18.6% of hours
- correlation of daily returns with s3v2 baseline: 0.80
