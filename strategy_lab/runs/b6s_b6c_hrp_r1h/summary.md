# Run: b6s_b6c_hrp_r1h

Strategy `s3v2x_alloc`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'alloc': 'hrp'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | -27.88% | -4.80% | -0.23 | -0.34 | -61.89% | -0.08 | -0.23 |
| in_sample | 2020-02-15 → 2024-12-31 | -6.06% | -1.27% | -0.00 | -0.00 | -49.57% | -0.03 | -0.01 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -23.11% | -13.88% | -0.85 | -1.26 | -32.06% | -0.43 | -0.89 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -6.95% | -6.95% | -0.31 | -0.47 | -21.11% | -0.33 | -0.38 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.90% | 35% | -5.74% | -6.67% | -4.44 | 14 | 100% |
| out_of_sample | 628 | -1.38% | 31% | -4.77% | -5.64% | -5.49 | 14 | 100% |
| in_sample | 1768 | -0.74% | 36% | -5.74% | -6.67% | -4.09 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.386% | 53% | 4.91 | +93.40% |
| bull | 687 | 28% | +0.007% | 44% | 0.19 | +3.21% |
| bear | 400 | 17% | -0.025% | 36% | -0.62 | -10.55% |
| chop | 1160 | 48% | -0.072% | 32% | -1.61 | -58.50% |

## Turnover, fees, activity

- trades: 19864 (8.19/day); active days 100%
- turnover 208.7x equity/year; fees 20.87% of equity/year ($79,063 total)
- average gross exposure 0.19; brake active 21.3% of hours
- correlation of daily returns with s3v2 baseline: 0.74
