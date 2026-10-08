# Run: b6s_b6d_meta_p_r6h

Strategy `s3v2x_meta`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'size_map': 'p'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +95.46% | +10.62% | 1.26 | 1.91 | -10.18% | 1.04 | 1.45 |
| in_sample | 2020-02-15 → 2024-12-31 | +97.84% | +15.00% | 1.56 | 2.39 | -10.18% | 1.47 | 1.87 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -1.21% | -0.69% | -0.11 | -0.16 | -10.11% | -0.07 | -0.12 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -1.30% | -1.30% | -0.22 | -0.32 | -10.11% | -0.13 | -0.23 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.06% | 46% | -4.59% | -6.91% | -1.11 | 14 | 100% |
| out_of_sample | 628 | -0.21% | 35% | -3.32% | -3.40% | -3.55 | 14 | 100% |
| in_sample | 1768 | +0.01% | 51% | -4.59% | -6.91% | 0.31 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.167% | 56% | 5.19 | +33.76% |
| bull | 687 | 28% | +0.034% | 47% | 1.80 | +25.52% |
| bear | 400 | 17% | +0.011% | 44% | 0.95 | +4.25% |
| chop | 1160 | 48% | +0.013% | 41% | 0.42 | +14.29% |

## Turnover, fees, activity

- trades: 4136 (1.71/day); active days 100%
- turnover 25.9x equity/year; fees 2.59% of equity/year ($14,843 total)
- average gross exposure 0.07; brake active 2.2% of hours
- correlation of daily returns with s3v2 baseline: 0.61
