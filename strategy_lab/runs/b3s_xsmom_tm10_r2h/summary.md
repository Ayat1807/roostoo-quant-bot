# Run: b3s_xsmom_tm10_r2h

Strategy `xsmom`; universe `{'type': 'list', 'assets': ['ZECUSDT', 'PAXGUSDT', 'POLUSDT', 'ICPUSDT', 'TRXUSDT', 'LISTAUSDT', 'STOUSDT', 'CAKEUSDT', 'TUTUSDT', 'SOLUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +12.30% | +1.76% | 0.20 | 0.29 | -55.43% | 0.03 | 0.18 |
| in_sample | 2020-02-15 → 2024-12-31 | -16.15% | -3.54% | -0.02 | -0.02 | -53.88% | -0.07 | -0.03 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +33.94% | +18.08% | 0.67 | 1.00 | -31.91% | 0.57 | 0.77 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +60.78% | +60.78% | 1.50 | 2.32 | -31.91% | 1.90 | 1.95 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.10% | 36% | -11.17% | -13.76% | -3.33 | 12 | 33% |
| out_of_sample | 628 | -1.33% | 38% | -11.17% | -13.76% | -2.78 | 14 | 57% |
| in_sample | 1768 | -1.09% | 35% | -10.81% | -12.52% | -3.55 | 12 | 25% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.149% | 44% | 1.69 | +26.85% |
| bull | 687 | 28% | +0.139% | 41% | 1.64 | +137.16% |
| bear | 400 | 17% | -0.123% | 24% | -2.26 | -40.07% |
| chop | 1160 | 48% | -0.030% | 33% | -0.42 | -36.92% |

## Turnover, fees, activity

- trades: 54547 (22.50/day); active days 83%
- turnover 194.9x equity/year; fees 19.49% of equity/year ($62,968 total)
- average gross exposure 0.21; brake active 43.3% of hours
- correlation of daily returns with s3v2 baseline: 0.21
