# Run: b4b_inv_vol_cap20

Strategy `xsmom_sz`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'sizing': 'inv_vol', 'coin_cap': 0.2}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +232.45% | +19.83% | 0.70 | 0.95 | -57.70% | 0.34 | 0.69 |
| in_sample | 2020-02-15 → 2024-12-31 | +425.42% | +40.47% | 1.10 | 1.50 | -55.99% | 0.72 | 1.15 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -36.93% | -23.06% | -0.89 | -1.21 | -45.69% | -0.50 | -0.90 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -11.87% | -11.87% | -0.43 | -0.60 | -27.88% | -0.43 | -0.50 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.15% | 41% | -19.75% | -19.75% | -2.34 | 12 | 32% |
| out_of_sample | 628 | -2.15% | 34% | -11.39% | -12.90% | -4.46 | 12 | 20% |
| in_sample | 1768 | -0.65% | 44% | -19.75% | -19.75% | -1.23 | 12 | 36% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.576% | 51% | 3.61 | +153.73% |
| bull | 687 | 28% | +0.276% | 51% | 2.50 | +471.21% |
| bear | 400 | 17% | -0.239% | 35% | -3.74 | -62.71% |
| chop | 1160 | 48% | -0.034% | 38% | -0.50 | -38.48% |

## Turnover, fees, activity

- trades: 13791 (5.69/day); active days 82%
- turnover 172.9x equity/year; fees 17.29% of equity/year ($229,741 total)
- average gross exposure 0.31; brake active 45.3% of hours
- correlation of daily returns with s3v2 baseline: 0.38
