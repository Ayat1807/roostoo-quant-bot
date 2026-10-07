# Run: b4e_fast_4h

Strategy `xsmom`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +246.00% | +20.56% | 0.69 | 0.96 | -66.87% | 0.31 | 0.68 |
| in_sample | 2020-02-15 → 2024-12-31 | +447.97% | +41.68% | 1.09 | 1.50 | -57.90% | 0.72 | 1.14 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -37.31% | -23.33% | -0.80 | -1.10 | -48.15% | -0.48 | -0.83 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -18.08% | -18.08% | -0.68 | -0.94 | -32.35% | -0.56 | -0.75 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.22% | 40% | -18.04% | -20.22% | -2.44 | 12 | 30% |
| out_of_sample | 628 | -2.22% | 34% | -12.20% | -14.87% | -4.41 | 12 | 21% |
| in_sample | 1768 | -0.73% | 42% | -18.04% | -20.22% | -1.66 | 12 | 34% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.595% | 48% | 3.60 | +160.92% |
| bull | 687 | 28% | +0.270% | 48% | 2.32 | +440.88% |
| bear | 400 | 17% | -0.248% | 31% | -3.75 | -64.10% |
| chop | 1160 | 48% | -0.023% | 35% | -0.32 | -31.72% |

## Turnover, fees, activity

- trades: 21222 (8.75/day); active days 83%
- turnover 199.1x equity/year; fees 19.91% of equity/year ($307,908 total)
- average gross exposure 0.30; brake active 48.2% of hours
- correlation of daily returns with s3v2 baseline: 0.37
