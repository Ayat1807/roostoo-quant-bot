# Run: b5s_b5_s3v2e_ssb075_r12h

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.75, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +303.47% | +23.38% | 1.44 | 2.15 | -14.79% | 1.58 | 1.76 |
| in_sample | 2020-02-15 → 2024-12-31 | +176.22% | +23.14% | 1.44 | 2.15 | -14.79% | 1.56 | 1.76 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +46.11% | +24.08% | 1.43 | 2.13 | -13.30% | 1.81 | 1.83 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +30.85% | +30.85% | 1.59 | 2.39 | -13.30% | 2.32 | 2.13 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.16% | 46% | -6.53% | -8.27% | -1.22 | 14 | 100% |
| out_of_sample | 628 | -0.22% | 44% | -4.80% | -5.94% | -1.29 | 14 | 100% |
| in_sample | 1768 | -0.13% | 47% | -6.53% | -8.27% | -1.09 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.321% | 55% | 3.96 | +72.17% |
| bull | 687 | 28% | +0.101% | 52% | 2.79 | +96.84% |
| bear | 400 | 17% | +0.065% | 47% | 1.81 | +28.66% |
| chop | 1160 | 48% | -0.001% | 43% | -0.03 | -5.21% |

## Turnover, fees, activity

- trades: 5806 (2.40/day); active days 100%
- turnover 51.8x equity/year; fees 5.18% of equity/year ($37,563 total)
- average gross exposure 0.18; brake active 11.3% of hours
- correlation of daily returns with s3v2 baseline: 0.83
