# Run: b_r1_rs_gated

Strategy `sat_rs`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'gate': 'alt_rally'}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | -42.50% | -8.31% | -0.44 | -0.59 | -53.35% | -0.16 | -0.41 |
| in_sample | 2020-02-15 → 2024-12-31 | -25.10% | -5.75% | -0.27 | -0.35 | -43.19% | -0.13 | -0.26 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -23.23% | -16.20% | -1.09 | -1.42 | -28.48% | -0.57 | -1.07 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -16.35% | -21.23% | -3.03 | -3.45 | -16.35% | -1.30 | -2.68 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | +0.00% | 12% | -10.35% | -10.73% | 0.00 | 0 | 0% |
| out_of_sample | 532 | +0.00% | 6% | -10.35% | -10.35% | 0.00 | 0 | 0% |
| in_sample | 1768 | +0.00% | 14% | -9.91% | -10.73% | 0.00 | 0 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.058% | 4% | 1.53 | +9.92% |
| bull | 659 | 28% | +0.006% | 11% | 0.10 | -0.46% |
| bear | 399 | 17% | -0.005% | 0% | -1.09 | -1.87% |
| chop | 1099 | 47% | -0.055% | 3% | -1.76 | -46.45% |

## Turnover, fees, activity

- trades: 618 (0.27/day); active days 8%
- turnover 16.4x equity/year; fees 1.64% of equity/year ($924 total)
- average gross exposure 0.05; brake active 11.4% of hours
- correlation of daily returns with s3v2 baseline: 0.16
