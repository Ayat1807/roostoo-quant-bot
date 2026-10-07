# Run: b4b_inv_vol

Strategy `xsmom_sz`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'sizing': 'inv_vol'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +214.75% | +18.85% | 0.68 | 0.93 | -59.09% | 0.32 | 0.67 |
| in_sample | 2020-02-15 → 2024-12-31 | +384.67% | +38.17% | 1.07 | 1.46 | -56.27% | 0.68 | 1.11 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -35.27% | -21.92% | -0.89 | -1.23 | -43.33% | -0.51 | -0.91 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -15.12% | -15.12% | -0.63 | -0.87 | -29.52% | -0.51 | -0.69 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.07% | 40% | -19.64% | -19.64% | -2.37 | 12 | 32% |
| out_of_sample | 628 | -1.94% | 34% | -9.31% | -10.89% | -4.27 | 12 | 20% |
| in_sample | 1768 | -0.78% | 42% | -19.64% | -19.64% | -1.57 | 12 | 36% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.558% | 55% | 3.51 | +146.03% |
| bull | 687 | 28% | +0.281% | 53% | 2.63 | +496.57% |
| bear | 400 | 17% | -0.228% | 40% | -3.58 | -61.08% |
| chop | 1160 | 48% | -0.043% | 41% | -0.66 | -44.90% |

## Turnover, fees, activity

- trades: 13909 (5.74/day); active days 82%
- turnover 178.9x equity/year; fees 17.89% of equity/year ($224,937 total)
- average gross exposure 0.31; brake active 46.1% of hours
- correlation of daily returns with s3v2 baseline: 0.37
