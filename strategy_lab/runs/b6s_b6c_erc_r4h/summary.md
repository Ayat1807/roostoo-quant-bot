# Run: b6s_b6c_erc_r4h

Strategy `s3v2x_alloc`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'alloc': 'erc'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +158.51% | +15.38% | 0.93 | 1.42 | -17.94% | 0.86 | 1.10 |
| in_sample | 2020-02-15 → 2024-12-31 | +117.77% | +17.28% | 1.03 | 1.59 | -14.61% | 1.18 | 1.30 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +18.82% | +10.31% | 0.66 | 0.97 | -17.94% | 0.57 | 0.76 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +14.34% | +14.34% | 0.79 | 1.17 | -17.94% | 0.80 | 0.94 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.20% | 46% | -5.60% | -7.37% | -1.47 | 14 | 99% |
| out_of_sample | 628 | -0.55% | 41% | -5.60% | -6.64% | -2.62 | 14 | 100% |
| in_sample | 1768 | -0.11% | 48% | -5.59% | -7.37% | -0.71 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.305% | 48% | 3.76 | +67.33% |
| bull | 687 | 28% | +0.058% | 43% | 1.55 | +46.48% |
| bear | 400 | 17% | +0.053% | 44% | 1.20 | +21.82% |
| chop | 1160 | 48% | -0.006% | 37% | -0.13 | -11.10% |

## Turnover, fees, activity

- trades: 9323 (3.85/day); active days 100%
- turnover 95.7x equity/year; fees 9.57% of equity/year ($56,806 total)
- average gross exposure 0.17; brake active 15.3% of hours
- correlation of daily returns with s3v2 baseline: 0.74
