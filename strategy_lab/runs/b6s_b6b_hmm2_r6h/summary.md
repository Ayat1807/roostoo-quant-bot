# Run: b6s_b6b_hmm2_r6h

Strategy `s3v2x_regime`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'regime_hmm': 2}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +274.34% | +21.99% | 1.41 | 2.13 | -13.99% | 1.57 | 1.75 |
| in_sample | 2020-02-15 → 2024-12-31 | +182.65% | +23.72% | 1.51 | 2.30 | -13.71% | 1.73 | 1.89 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +32.53% | +17.38% | 1.12 | 1.68 | -13.99% | 1.24 | 1.38 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +19.16% | +19.16% | 1.10 | 1.65 | -13.99% | 1.37 | 1.40 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.08% | 47% | -5.03% | -6.91% | -0.74 | 14 | 100% |
| out_of_sample | 628 | -0.31% | 41% | -5.03% | -5.72% | -2.17 | 14 | 100% |
| in_sample | 1768 | -0.02% | 49% | -4.59% | -6.91% | -0.13 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.340% | 55% | 4.51 | +78.62% |
| bull | 687 | 28% | +0.074% | 48% | 2.23 | +64.08% |
| bear | 400 | 17% | +0.070% | 45% | 1.88 | +30.97% |
| chop | 1160 | 48% | +0.003% | 40% | 0.07 | -0.19% |

## Turnover, fees, activity

- trades: 6514 (2.69/day); active days 100%
- turnover 61.0x equity/year; fees 6.10% of equity/year ($44,675 total)
- average gross exposure 0.17; brake active 10.2% of hours
- correlation of daily returns with s3v2 baseline: 0.80
