# Run: b4c_B_c2_w05_m150

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d', 'min_positions': 1, 'check_h': 2, 'w': 0.5, 'swap_m': 1.5, 'min_hold_h': 6}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +234.29% | +19.93% | 0.72 | 1.00 | -46.58% | 0.43 | 0.75 |
| in_sample | 2020-02-15 → 2024-12-31 | +295.77% | +32.55% | 0.97 | 1.36 | -46.58% | 0.70 | 1.05 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -15.43% | -9.09% | -0.26 | -0.36 | -30.10% | -0.30 | -0.31 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +1.82% | +1.82% | 0.19 | 0.28 | -27.84% | 0.07 | 0.19 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.85% | 41% | -18.59% | -22.52% | -2.05 | 14 | 67% |
| out_of_sample | 628 | -1.68% | 38% | -11.32% | -11.46% | -4.36 | 14 | 72% |
| in_sample | 1768 | -0.61% | 43% | -18.59% | -22.52% | -1.17 | 14 | 65% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.714% | 53% | 4.77 | +226.25% |
| bull | 687 | 28% | +0.226% | 48% | 2.23 | +315.22% |
| bear | 400 | 17% | -0.071% | 41% | -1.02 | -27.19% |
| chop | 1160 | 48% | -0.086% | 37% | -1.37 | -66.11% |

## Turnover, fees, activity

- trades: 17238 (7.11/day); active days 95%
- turnover 233.0x equity/year; fees 23.30% of equity/year ($255,211 total)
- average gross exposure 0.26; brake active 51.5% of hours
- correlation of daily returns with s3v2 baseline: 0.50
