# Run: b4b_score_cap25

Strategy `xsmom_sz`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'sizing': 'score', 'coin_cap': 0.25}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +608.59% | +34.30% | 0.96 | 1.35 | -58.85% | 0.58 | 1.00 |
| in_sample | 2020-02-15 → 2024-12-31 | +880.37% | +59.61% | 1.34 | 1.88 | -58.85% | 1.01 | 1.46 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -28.27% | -17.22% | -0.52 | -0.73 | -42.22% | -0.41 | -0.57 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -8.22% | -8.22% | -0.20 | -0.29 | -27.66% | -0.30 | -0.26 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.06% | 42% | -17.12% | -18.65% | -2.21 | 12 | 32% |
| out_of_sample | 628 | -1.93% | 37% | -11.10% | -14.80% | -4.63 | 12 | 21% |
| in_sample | 1768 | -0.72% | 44% | -17.12% | -18.65% | -1.46 | 12 | 37% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.731% | 47% | 4.01 | +225.81% |
| bull | 687 | 28% | +0.283% | 49% | 2.36 | +482.78% |
| bear | 400 | 17% | -0.245% | 33% | -3.72 | -63.68% |
| chop | 1160 | 48% | +0.013% | 34% | 0.17 | +2.76% |

## Turnover, fees, activity

- trades: 14260 (5.88/day); active days 82%
- turnover 176.0x equity/year; fees 17.60% of equity/year ($401,941 total)
- average gross exposure 0.30; brake active 45.7% of hours
- correlation of daily returns with s3v2 baseline: 0.37
