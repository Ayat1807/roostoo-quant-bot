# Run: b_r4_bo_gated_rfng

Strategy `sat_breakout`; universe `{'type': 'satellite', 'rule': 'R4', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'gate': 'alt_rally', 'riskoff': 'fng'}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +15.13% | +2.23% | 0.25 | 0.34 | -21.41% | 0.10 | 0.24 |
| in_sample | 2020-02-15 → 2024-12-31 | +8.99% | +1.78% | 0.21 | 0.28 | -21.41% | 0.08 | 0.20 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +5.63% | +3.73% | 0.38 | 0.54 | -10.11% | 0.37 | 0.44 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +1.11% | +1.49% | 0.24 | 0.35 | -4.85% | 0.31 | 0.30 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | +0.00% | 13% | -8.33% | -8.51% | 0.00 | 0 | 0% |
| out_of_sample | 532 | +0.00% | 12% | -4.94% | -6.80% | 0.00 | 0 | 0% |
| in_sample | 1768 | +0.00% | 14% | -8.33% | -8.51% | 0.00 | 0 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.013% | 2% | 0.88 | +2.21% |
| bull | 659 | 28% | +0.053% | 10% | 1.09 | +38.22% |
| bear | 399 | 17% | -0.003% | 0% | -0.70 | -1.37% |
| chop | 1099 | 47% | -0.017% | 3% | -0.78 | -17.37% |

## Turnover, fees, activity

- trades: 483 (0.21/day); active days 8%
- turnover 13.2x equity/year; fees 1.32% of equity/year ($863 total)
- average gross exposure 0.03; brake active 3.6% of hours
- correlation of daily returns with s3v2 baseline: 0.11
