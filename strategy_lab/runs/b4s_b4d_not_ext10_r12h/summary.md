# Run: b4s_b4d_not_ext10_r12h

Strategy `xsmom_entry`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'entry_filter': 'not_extended', 'ext': 0.1}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +93.74% | +10.47% | 0.49 | 0.67 | -70.66% | 0.15 | 0.46 |
| in_sample | 2020-02-15 → 2024-12-31 | +102.51% | +15.55% | 0.63 | 0.85 | -59.44% | 0.26 | 0.61 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -4.45% | -2.55% | 0.01 | 0.01 | -35.20% | -0.07 | -0.01 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +13.28% | +13.28% | 0.67 | 0.97 | -24.07% | 0.55 | 0.75 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.25% | 39% | -17.05% | -17.89% | -3.06 | 12 | 21% |
| out_of_sample | 628 | -1.49% | 40% | -9.98% | -12.27% | -4.10 | 12 | 17% |
| in_sample | 1768 | -1.19% | 38% | -17.05% | -17.89% | -2.97 | 11 | 23% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.342% | 42% | 2.77 | +73.88% |
| bull | 687 | 28% | +0.215% | 47% | 2.26 | +291.27% |
| bear | 400 | 17% | -0.191% | 25% | -3.49 | -54.38% |
| chop | 1160 | 48% | -0.032% | 33% | -0.47 | -37.58% |

## Turnover, fees, activity

- trades: 17671 (7.29/day); active days 77%
- turnover 169.7x equity/year; fees 16.97% of equity/year ($139,385 total)
- average gross exposure 0.27; brake active 46.0% of hours
- correlation of daily returns with s3v2 baseline: 0.41
