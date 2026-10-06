# Run: b3_donchian_alt10

Strategy `donchian_long`; universe `{'type': 'list', 'assets': ['ZECUSDT', 'NEARUSDT', 'SUIUSDT', 'LTCUSDT', 'UNIUSDT', 'AAVEUSDT', 'TAOUSDT', 'ENAUSDT', 'HBARUSDT', 'TRXUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_divisor': 10}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +69.54% | +8.28% | 1.05 | 1.43 | -8.06% | 1.03 | 1.19 |
| in_sample | 2020-02-15 → 2024-12-31 | +52.81% | +9.07% | 1.08 | 1.45 | -8.06% | 1.13 | 1.24 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +10.80% | +6.01% | 0.96 | 1.38 | -5.35% | 1.12 | 1.18 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +12.95% | +12.95% | 2.09 | 3.08 | -3.03% | 4.28 | 3.14 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.02% | 48% | -5.43% | -6.27% | -0.47 | 14 | 83% |
| out_of_sample | 628 | -0.04% | 46% | -2.26% | -3.30% | -1.30 | 14 | 89% |
| in_sample | 1768 | -0.01% | 49% | -5.43% | -6.27% | -0.15 | 14 | 81% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.044% | 47% | 1.23 | +7.60% |
| bull | 687 | 28% | +0.089% | 59% | 3.64 | +83.44% |
| bear | 400 | 17% | -0.015% | 42% | -1.68 | -5.79% |
| chop | 1160 | 48% | -0.008% | 47% | -0.55 | -8.82% |

## Turnover, fees, activity

- trades: 2479 (1.02/day); active days 96%
- turnover 2.3x equity/year; fees 0.23% of equity/year ($1,016 total)
- average gross exposure 0.06; brake active 1.0% of hours
- correlation of daily returns with s3v2 baseline: 0.15
