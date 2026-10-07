# Run: b4b_score_x_invvol

Strategy `xsmom_sz`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'sizing': 'score_x_invvol'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +344.34% | +25.18% | 0.81 | 1.13 | -61.26% | 0.41 | 0.82 |
| in_sample | 2020-02-15 → 2024-12-31 | +582.69% | +48.21% | 1.22 | 1.69 | -59.14% | 0.82 | 1.29 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -35.37% | -21.99% | -0.87 | -1.20 | -46.31% | -0.47 | -0.88 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -5.43% | -5.43% | -0.12 | -0.18 | -24.52% | -0.22 | -0.17 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.99% | 41% | -18.16% | -19.35% | -2.29 | 12 | 31% |
| out_of_sample | 628 | -1.68% | 35% | -11.43% | -11.93% | -3.93 | 12 | 19% |
| in_sample | 1768 | -0.61% | 43% | -18.16% | -19.35% | -1.29 | 12 | 36% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.731% | 47% | 4.12 | +227.41% |
| bull | 687 | 28% | +0.275% | 50% | 2.43 | +465.12% |
| bear | 400 | 17% | -0.239% | 34% | -3.85 | -62.72% |
| chop | 1160 | 48% | -0.029% | 35% | -0.42 | -35.58% |

## Turnover, fees, activity

- trades: 14082 (5.81/day); active days 82%
- turnover 183.0x equity/year; fees 18.30% of equity/year ($315,970 total)
- average gross exposure 0.31; brake active 45.9% of hours
- correlation of daily returns with s3v2 baseline: 0.37
