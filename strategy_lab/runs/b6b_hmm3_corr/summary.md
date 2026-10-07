# Run: b6b_hmm3_corr

Strategy `s3v2x_regime`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'regime_hmm': 3, 'corr_filter': True}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +162.59% | +15.65% | 1.03 | 1.51 | -19.15% | 0.82 | 1.16 |
| in_sample | 2020-02-15 → 2024-12-31 | +103.11% | +15.62% | 1.00 | 1.46 | -19.15% | 0.82 | 1.13 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +29.40% | +15.79% | 1.13 | 1.67 | -10.65% | 1.48 | 1.45 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +30.28% | +30.28% | 1.65 | 2.47 | -10.65% | 2.84 | 2.33 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.21% | 43% | -5.34% | -7.48% | -1.81 | 14 | 99% |
| out_of_sample | 628 | -0.17% | 43% | -5.14% | -6.10% | -1.47 | 14 | 98% |
| in_sample | 1768 | -0.22% | 43% | -5.34% | -7.48% | -2.02 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.269% | 57% | 3.10 | +56.76% |
| bull | 687 | 28% | +0.088% | 53% | 2.57 | +80.58% |
| bear | 400 | 17% | +0.053% | 46% | 1.57 | +22.82% |
| chop | 1160 | 48% | -0.019% | 43% | -0.48 | -22.30% |

## Turnover, fees, activity

- trades: 5046 (2.08/day); active days 100%
- turnover 39.3x equity/year; fees 3.93% of equity/year ($21,283 total)
- average gross exposure 0.18; brake active 8.8% of hours
- correlation of daily returns with s3v2 baseline: 0.82
