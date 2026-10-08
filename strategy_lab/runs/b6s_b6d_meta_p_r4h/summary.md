# Run: b6s_b6d_meta_p_r4h

Strategy `s3v2x_meta`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'size_map': 'p'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +70.87% | +8.40% | 1.01 | 1.54 | -16.29% | 0.52 | 1.08 |
| in_sample | 2020-02-15 → 2024-12-31 | +79.99% | +12.79% | 1.35 | 2.06 | -16.29% | 0.79 | 1.46 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -5.07% | -2.92% | -0.61 | -0.87 | -11.06% | -0.26 | -0.61 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -3.03% | -3.03% | -0.58 | -0.82 | -11.06% | -0.27 | -0.58 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.09% | 45% | -6.98% | -7.50% | -1.55 | 14 | 100% |
| out_of_sample | 628 | -0.23% | 30% | -3.00% | -3.19% | -4.70 | 14 | 100% |
| in_sample | 1768 | -0.00% | 50% | -6.98% | -7.50% | -0.01 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.139% | 54% | 4.63 | +27.33% |
| bull | 687 | 28% | +0.035% | 46% | 1.86 | +26.20% |
| bear | 400 | 17% | +0.003% | 38% | 0.28 | +1.20% |
| chop | 1160 | 48% | +0.008% | 39% | 0.25 | +7.59% |

## Turnover, fees, activity

- trades: 4436 (1.83/day); active days 100%
- turnover 30.0x equity/year; fees 3.00% of equity/year ($15,367 total)
- average gross exposure 0.07; brake active 2.4% of hours
- correlation of daily returns with s3v2 baseline: 0.59
