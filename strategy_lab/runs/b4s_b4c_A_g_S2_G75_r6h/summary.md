# Run: b4s_b4c_A_g_S2_G75_r6h

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 2, 'gross_cap': 0.75, 'short_gate': 'btc_below_30d'}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +20.88% | +2.90% | 0.26 | 0.37 | -85.35% | 0.03 | 0.24 |
| in_sample | 2020-02-15 → 2024-12-31 | +108.27% | +16.22% | 0.58 | 0.80 | -74.04% | 0.22 | 0.56 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -41.74% | -26.46% | -0.89 | -1.24 | -55.07% | -0.48 | -0.91 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -17.42% | -17.42% | -0.58 | -0.82 | -35.13% | -0.50 | -0.65 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.37% | 39% | -17.01% | -19.44% | -2.51 | 14 | 83% |
| out_of_sample | 628 | -2.16% | 31% | -13.85% | -14.75% | -4.60 | 14 | 83% |
| in_sample | 1768 | -0.97% | 42% | -17.01% | -19.44% | -1.75 | 14 | 83% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.776% | 56% | 4.50 | +255.32% |
| bull | 687 | 28% | +0.249% | 47% | 2.09 | +364.46% |
| bear | 400 | 17% | -0.239% | 42% | -3.25 | -63.08% |
| chop | 1160 | 48% | -0.130% | 37% | -1.79 | -80.16% |

## Turnover, fees, activity

- trades: 43964 (18.14/day); active days 96%
- turnover 359.8x equity/year; fees 35.98% of equity/year ($294,959 total)
- average gross exposure 0.36; brake active 52.0% of hours
- correlation of daily returns with s3v2 baseline: 0.51
