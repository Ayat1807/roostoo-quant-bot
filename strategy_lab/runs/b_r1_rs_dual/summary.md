# Run: b_r1_rs_dual

Strategy `sat_rs`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'dual': True}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +11.37% | +1.70% | 0.20 | 0.28 | -50.27% | 0.03 | 0.18 |
| in_sample | 2020-02-15 → 2024-12-31 | +44.93% | +7.90% | 0.41 | 0.56 | -50.27% | 0.16 | 0.40 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -23.16% | -16.15% | -0.55 | -0.77 | -33.36% | -0.48 | -0.62 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -12.71% | -16.62% | -0.62 | -0.88 | -22.85% | -0.73 | -0.76 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.76% | 38% | -10.12% | -11.61% | -2.69 | 7 | 2% |
| out_of_sample | 532 | -1.56% | 37% | -8.07% | -8.40% | -3.79 | 8 | 1% |
| in_sample | 1768 | -0.50% | 39% | -10.12% | -11.61% | -1.83 | 7 | 2% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.133% | 22% | 1.47 | +22.30% |
| bull | 659 | 28% | +0.179% | 37% | 1.95 | +193.45% |
| bear | 399 | 17% | -0.211% | 18% | -3.72 | -57.94% |
| chop | 1099 | 47% | -0.021% | 28% | -0.33 | -26.22% |

## Turnover, fees, activity

- trades: 2350 (1.01/day); active days 50%
- turnover 62.7x equity/year; fees 6.27% of equity/year ($5,168 total)
- average gross exposure 0.21; brake active 30.0% of hours
- correlation of daily returns with s3v2 baseline: 0.26
