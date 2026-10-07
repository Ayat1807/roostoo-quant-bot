# Run: b4b_all_elig_cap10

Strategy `xsmom_sz`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'select': 'all_eligible', 'coin_cap': 0.1}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +121.62% | +12.73% | 0.54 | 0.72 | -60.63% | 0.21 | 0.51 |
| in_sample | 2020-02-15 → 2024-12-31 | +235.37% | +28.13% | 0.91 | 1.21 | -50.05% | 0.56 | 0.93 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -34.07% | -21.10% | -0.86 | -1.16 | -48.63% | -0.43 | -0.85 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -8.91% | -8.91% | -0.33 | -0.45 | -29.07% | -0.31 | -0.37 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.00% | 40% | -15.92% | -16.87% | -2.46 | 12 | 33% |
| out_of_sample | 628 | -2.17% | 29% | -12.71% | -13.01% | -5.20 | 12 | 21% |
| in_sample | 1768 | -0.55% | 44% | -15.92% | -16.87% | -1.22 | 12 | 37% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.521% | 49% | 3.56 | +133.30% |
| bull | 687 | 28% | +0.230% | 50% | 2.42 | +333.07% |
| bear | 400 | 17% | -0.215% | 29% | -3.86 | -58.69% |
| chop | 1160 | 48% | -0.048% | 34% | -0.77 | -46.90% |

## Turnover, fees, activity

- trades: 21781 (8.99/day); active days 83%
- turnover 129.3x equity/year; fees 12.93% of equity/year ($115,423 total)
- average gross exposure 0.26; brake active 46.4% of hours
- correlation of daily returns with s3v2 baseline: 0.41
