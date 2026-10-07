# Run: b4e_fast_2h

Strategy `xsmom`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +253.08% | +20.92% | 0.70 | 0.97 | -66.65% | 0.31 | 0.69 |
| in_sample | 2020-02-15 → 2024-12-31 | +458.90% | +42.26% | 1.10 | 1.52 | -59.69% | 0.71 | 1.15 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -37.28% | -23.31% | -0.80 | -1.11 | -48.45% | -0.48 | -0.83 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -13.50% | -13.50% | -0.45 | -0.62 | -31.68% | -0.43 | -0.51 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.21% | 40% | -17.30% | -18.66% | -2.45 | 12 | 31% |
| out_of_sample | 628 | -2.13% | 32% | -11.79% | -13.89% | -4.29 | 12 | 21% |
| in_sample | 1768 | -0.73% | 43% | -17.30% | -18.66% | -1.51 | 12 | 34% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.684% | 47% | 4.15 | +205.45% |
| bull | 687 | 28% | +0.271% | 48% | 2.31 | +441.73% |
| bear | 400 | 17% | -0.245% | 30% | -3.81 | -63.71% |
| chop | 1160 | 48% | -0.037% | 35% | -0.52 | -41.20% |

## Turnover, fees, activity

- trades: 28852 (11.90/day); active days 83%
- turnover 219.6x equity/year; fees 21.96% of equity/year ($329,920 total)
- average gross exposure 0.30; brake active 49.0% of hours
- correlation of daily returns with s3v2 baseline: 0.37
