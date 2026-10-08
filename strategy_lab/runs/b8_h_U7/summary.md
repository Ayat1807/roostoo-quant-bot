# Run: b8_h_U7

Strategy `s3v2x_regime`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'regime_hmm': 2}`; band 0.04; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +100.71% | +11.06% | 0.72 | 1.05 | -18.82% | 0.59 | 0.81 |
| in_sample | 2020-02-15 → 2024-12-31 | +72.99% | +11.88% | 0.78 | 1.15 | -18.82% | 0.63 | 0.88 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +16.15% | +8.89% | 0.56 | 0.81 | -16.87% | 0.53 | 0.65 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +0.18% | +0.18% | 0.10 | 0.14 | -16.87% | 0.01 | 0.09 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.21% | 46% | -6.63% | -7.59% | -1.25 | 14 | 100% |
| out_of_sample | 628 | -0.37% | 44% | -6.63% | -7.59% | -1.32 | 14 | 100% |
| in_sample | 1768 | -0.18% | 46% | -5.84% | -6.18% | -1.10 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.289% | 51% | 4.03 | +63.61% |
| bull | 687 | 28% | +0.064% | 53% | 1.71 | +52.65% |
| bear | 400 | 17% | +0.029% | 48% | 0.68 | +10.79% |
| chop | 1160 | 48% | -0.021% | 45% | -0.46 | -24.91% |

## Turnover, fees, activity

- trades: 9463 (3.90/day); active days 100%
- turnover 61.6x equity/year; fees 6.16% of equity/year ($30,890 total)
- average gross exposure 0.21; brake active 17.3% of hours
- correlation of daily returns with s3v2 baseline: 0.84
