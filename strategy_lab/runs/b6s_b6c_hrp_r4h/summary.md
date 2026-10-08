# Run: b6s_b6c_hrp_r4h

Strategy `s3v2x_alloc`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'alloc': 'hrp'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +88.93% | +10.06% | 0.68 | 1.01 | -25.61% | 0.39 | 0.72 |
| in_sample | 2020-02-15 → 2024-12-31 | +80.07% | +12.80% | 0.83 | 1.24 | -25.61% | 0.50 | 0.90 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +5.06% | +2.85% | 0.25 | 0.38 | -15.30% | 0.19 | 0.28 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +12.36% | +12.36% | 0.71 | 1.07 | -15.03% | 0.82 | 0.89 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.43% | 42% | -5.04% | -6.47% | -2.41 | 14 | 100% |
| out_of_sample | 628 | -0.81% | 38% | -4.69% | -5.91% | -3.64 | 14 | 100% |
| in_sample | 1768 | -0.30% | 44% | -5.04% | -6.47% | -1.90 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.392% | 57% | 4.86 | +95.04% |
| bull | 687 | 28% | +0.050% | 46% | 1.37 | +38.83% |
| bear | 400 | 17% | +0.020% | 39% | 0.48 | +7.02% |
| chop | 1160 | 48% | -0.031% | 36% | -0.72 | -33.09% |

## Turnover, fees, activity

- trades: 11347 (4.68/day); active days 100%
- turnover 125.3x equity/year; fees 12.53% of equity/year ($68,739 total)
- average gross exposure 0.20; brake active 15.1% of hours
- correlation of daily returns with s3v2 baseline: 0.77
