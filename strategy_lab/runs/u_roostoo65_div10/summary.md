# Run: u_roostoo65_div10

Strategy `s3v2x`; universe `{'type': 'roostoo_all'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_divisor': 10}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +60.18% | +7.35% | 0.73 | 1.02 | -22.97% | 0.32 | 0.72 |
| in_sample | 2020-02-15 → 2024-12-31 | +45.65% | +8.01% | 0.71 | 0.99 | -22.97% | 0.35 | 0.71 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +10.07% | +5.61% | 1.12 | 1.65 | -4.71% | 1.19 | 1.35 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +4.59% | +4.59% | 1.08 | 1.64 | -4.61% | 0.99 | 1.28 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.08% | 47% | -7.22% | -7.28% | -0.93 | 14 | 100% |
| out_of_sample | 628 | -0.04% | 47% | -4.19% | -4.71% | -0.70 | 14 | 100% |
| in_sample | 1768 | -0.12% | 47% | -7.22% | -7.28% | -1.08 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.223% | 51% | 4.28 | +46.66% |
| bull | 687 | 28% | +0.070% | 51% | 2.04 | +59.70% |
| bear | 400 | 17% | +0.001% | 43% | 0.05 | +0.15% |
| chop | 1160 | 48% | -0.032% | 43% | -1.42 | -31.43% |

## Turnover, fees, activity

- trades: 5297 (2.19/day); active days 100%
- turnover 53.9x equity/year; fees 5.39% of equity/year ($22,647 total)
- average gross exposure 0.23; brake active 3.1% of hours
- correlation of daily returns with s3v2 baseline: 0.59
