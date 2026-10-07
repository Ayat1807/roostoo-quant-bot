# Run: b4d_resistance

Strategy `xsmom_entry`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'entry_filter': 'resistance'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +273.12% | +21.93% | 0.73 | 1.00 | -62.74% | 0.35 | 0.72 |
| in_sample | 2020-02-15 → 2024-12-31 | +397.36% | +38.90% | 1.04 | 1.43 | -60.65% | 0.64 | 1.08 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -25.25% | -15.26% | -0.44 | -0.61 | -37.32% | -0.41 | -0.50 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -8.18% | -8.18% | -0.22 | -0.31 | -26.56% | -0.31 | -0.28 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.16% | 40% | -19.13% | -19.84% | -2.24 | 12 | 31% |
| out_of_sample | 628 | -1.91% | 37% | -11.96% | -14.81% | -4.30 | 12 | 19% |
| in_sample | 1768 | -0.90% | 42% | -19.13% | -19.84% | -1.80 | 12 | 36% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.628% | 45% | 3.72 | +175.53% |
| bull | 687 | 28% | +0.251% | 49% | 2.23 | +380.03% |
| bear | 400 | 17% | -0.220% | 33% | -3.35 | -59.81% |
| chop | 1160 | 48% | -0.021% | 36% | -0.28 | -29.80% |

## Turnover, fees, activity

- trades: 13989 (5.77/day); active days 82%
- turnover 168.5x equity/year; fees 16.85% of equity/year ($246,840 total)
- average gross exposure 0.30; brake active 47.2% of hours
- correlation of daily returns with s3v2 baseline: 0.38
