# Run: b3_xsmom_alt10

Strategy `xsmom`; universe `{'type': 'list', 'assets': ['ZECUSDT', 'NEARUSDT', 'SUIUSDT', 'LTCUSDT', 'UNIUSDT', 'AAVEUSDT', 'TAOUSDT', 'ENAUSDT', 'HBARUSDT', 'TRXUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | -29.16% | -5.06% | -0.00 | -0.00 | -65.40% | -0.08 | -0.02 |
| in_sample | 2020-02-15 → 2024-12-31 | -21.59% | -4.86% | 0.01 | 0.01 | -65.40% | -0.07 | -0.01 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -9.65% | -5.61% | -0.03 | -0.05 | -37.34% | -0.15 | -0.07 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +8.10% | +8.10% | 0.41 | 0.57 | -31.89% | 0.25 | 0.43 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.28% | 38% | -14.16% | -17.01% | -2.93 | 12 | 28% |
| out_of_sample | 628 | -1.85% | 36% | -13.38% | -15.50% | -3.80 | 12 | 32% |
| in_sample | 1768 | -1.10% | 39% | -14.16% | -17.01% | -2.65 | 12 | 26% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.281% | 45% | 2.24 | +55.96% |
| bull | 687 | 28% | +0.130% | 45% | 1.32 | +116.32% |
| bear | 400 | 17% | -0.127% | 32% | -2.07 | -41.50% |
| chop | 1160 | 48% | -0.076% | 35% | -1.11 | -62.63% |

## Turnover, fees, activity

- trades: 11924 (4.92/day); active days 82%
- turnover 128.8x equity/year; fees 12.88% of equity/year ($30,268 total)
- average gross exposure 0.25; brake active 47.9% of hours
- correlation of daily returns with s3v2 baseline: 0.27
