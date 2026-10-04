# Run: u_roostoo65

Strategy `s3v2`; universe `{'type': 'roostoo_all'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +36.85% | +4.84% | 1.11 | 1.59 | -4.95% | 0.98 | 1.26 |
| in_sample | 2020-02-15 → 2024-12-31 | +36.70% | +6.61% | 1.30 | 1.87 | -4.95% | 1.33 | 1.54 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +0.13% | +0.07% | 0.07 | 0.09 | -1.35% | 0.05 | 0.07 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +0.29% | +0.29% | 0.26 | 0.37 | -1.35% | 0.21 | 0.29 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.04% | 44% | -2.23% | -4.95% | -1.84 | 14 | 100% |
| out_of_sample | 628 | -0.02% | 44% | -0.42% | -0.67% | -1.80 | 14 | 100% |
| in_sample | 1768 | -0.05% | 45% | -2.23% | -4.95% | -1.76 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.073% | 50% | 3.57 | +13.59% |
| bull | 687 | 28% | +0.024% | 46% | 1.83 | +17.45% |
| bear | 400 | 17% | -0.001% | 42% | -0.26 | -0.50% |
| chop | 1160 | 48% | +0.003% | 44% | 0.28 | +3.42% |

## Turnover, fees, activity

- trades: 3038 (1.25/day); active days 100%
- turnover 12.3x equity/year; fees 1.23% of equity/year ($5,180 total)
- average gross exposure 0.06; brake active 0.0% of hours
- correlation of daily returns with s3v2 baseline: 0.51
