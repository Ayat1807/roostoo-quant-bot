# Run: b_r1_bo_rvb

Strategy `sat_breakout`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'riskoff': 'vol_breadth'}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +22.85% | +3.28% | 0.26 | 0.35 | -54.61% | 0.06 | 0.23 |
| in_sample | 2020-02-15 → 2024-12-31 | +62.34% | +10.43% | 0.49 | 0.67 | -54.61% | 0.19 | 0.47 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -24.33% | -17.00% | -0.75 | -1.05 | -35.13% | -0.48 | -0.79 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -11.02% | -14.46% | -0.60 | -0.84 | -24.35% | -0.59 | -0.69 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | +0.00% | 30% | -13.10% | -13.10% | 0.00 | 4 | 1% |
| out_of_sample | 532 | -0.09% | 21% | -8.23% | -8.79% | -1.30 | 3 | 0% |
| in_sample | 1768 | +0.00% | 33% | -13.10% | -13.10% | 0.00 | 4 | 1% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.460% | 24% | 4.78 | +112.26% |
| bull | 659 | 28% | +0.150% | 24% | 1.57 | +140.99% |
| bear | 399 | 17% | -0.111% | 20% | -2.68 | -36.63% |
| chop | 1099 | 47% | -0.082% | 17% | -1.41 | -62.11% |

## Turnover, fees, activity

- trades: 1918 (0.82/day); active days 30%
- turnover 51.1x equity/year; fees 5.11% of equity/year ($4,127 total)
- average gross exposure 0.15; brake active 20.4% of hours
- correlation of daily returns with s3v2 baseline: 0.17
