# Run: b_r1_bo_near

Strategy `sat_breakout`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'near_high': 0.15}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +140.37% | +14.74% | 0.75 | 1.04 | -37.60% | 0.39 | 0.76 |
| in_sample | 2020-02-15 → 2024-12-31 | +172.08% | +22.76% | 1.02 | 1.41 | -37.60% | 0.61 | 1.05 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -11.66% | -7.95% | -0.40 | -0.56 | -20.41% | -0.39 | -0.46 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +1.21% | +1.62% | 0.18 | 0.26 | -11.69% | 0.14 | 0.20 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | +0.00% | 39% | -10.50% | -11.69% | 0.00 | 4 | 0% |
| out_of_sample | 532 | -0.38% | 35% | -8.06% | -8.35% | -5.10 | 4 | 0% |
| in_sample | 1768 | +0.00% | 40% | -10.50% | -11.69% | 0.00 | 4 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.187% | 31% | 1.90 | +33.34% |
| bull | 659 | 28% | +0.153% | 28% | 1.79 | +151.93% |
| bear | 399 | 17% | +0.002% | 21% | 0.06 | +0.12% |
| chop | 1099 | 47% | -0.028% | 28% | -0.69 | -28.53% |

## Turnover, fees, activity

- trades: 1578 (0.68/day); active days 33%
- turnover 43.6x equity/year; fees 4.36% of equity/year ($4,982 total)
- average gross exposure 0.11; brake active 8.4% of hours
- correlation of daily returns with s3v2 baseline: 0.13
