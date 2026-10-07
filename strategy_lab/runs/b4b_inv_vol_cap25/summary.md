# Run: b4b_inv_vol_cap25

Strategy `xsmom_sz`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'sizing': 'inv_vol', 'coin_cap': 0.25}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +189.55% | +17.36% | 0.64 | 0.88 | -60.75% | 0.29 | 0.63 |
| in_sample | 2020-02-15 → 2024-12-31 | +412.50% | +39.76% | 1.10 | 1.50 | -53.09% | 0.75 | 1.16 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -43.68% | -27.87% | -1.20 | -1.64 | -50.55% | -0.55 | -1.18 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -13.37% | -13.37% | -0.53 | -0.73 | -28.36% | -0.47 | -0.59 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.08% | 40% | -15.92% | -18.39% | -2.36 | 12 | 31% |
| out_of_sample | 628 | -2.19% | 31% | -11.35% | -12.66% | -4.89 | 12 | 20% |
| in_sample | 1768 | -0.62% | 44% | -15.92% | -18.39% | -1.16 | 12 | 36% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.566% | 47% | 3.64 | +150.42% |
| bull | 687 | 28% | +0.260% | 52% | 2.41 | +414.55% |
| bear | 400 | 17% | -0.227% | 32% | -3.48 | -60.99% |
| chop | 1160 | 48% | -0.040% | 34% | -0.61 | -42.40% |

## Turnover, fees, activity

- trades: 13991 (5.77/day); active days 82%
- turnover 177.4x equity/year; fees 17.74% of equity/year ($223,131 total)
- average gross exposure 0.30; brake active 45.9% of hours
- correlation of daily returns with s3v2 baseline: 0.37
