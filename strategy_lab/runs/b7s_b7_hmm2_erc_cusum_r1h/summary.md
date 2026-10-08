# Run: b7s_b7_hmm2_erc_cusum_r1h

Strategy `s3v2x_regime`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'regime_hmm': 2, 'inner': 's3v2x_alloc', 'alloc': 'erc'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +34.13% | +4.52% | 0.35 | 0.54 | -22.50% | 0.20 | 0.38 |
| in_sample | 2020-02-15 → 2024-12-31 | +35.93% | +6.49% | 0.47 | 0.71 | -20.08% | 0.32 | 0.52 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -1.25% | -0.71% | 0.03 | 0.05 | -17.54% | -0.04 | 0.02 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +6.94% | +6.94% | 0.46 | 0.68 | -17.54% | 0.40 | 0.53 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.38% | 41% | -5.95% | -6.50% | -2.63 | 14 | 99% |
| out_of_sample | 628 | -0.59% | 36% | -5.95% | -5.98% | -3.15 | 14 | 100% |
| in_sample | 1768 | -0.28% | 43% | -4.91% | -6.50% | -2.39 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.348% | 52% | 4.34 | +80.69% |
| bull | 687 | 28% | -0.005% | 42% | -0.13 | -4.71% |
| bear | 400 | 17% | +0.060% | 42% | 1.35 | +25.48% |
| chop | 1160 | 48% | -0.036% | 35% | -0.78 | -36.60% |

## Turnover, fees, activity

- trades: 14769 (6.09/day); active days 100%
- turnover 159.7x equity/year; fees 15.97% of equity/year ($67,390 total)
- average gross exposure 0.16; brake active 19.4% of hours
- correlation of daily returns with s3v2 baseline: 0.70
