# Run: b_r4_bo_gated_near

Strategy `sat_breakout`; universe `{'type': 'satellite', 'rule': 'R4', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'gate': 'alt_rally', 'near_high': 0.15}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +24.38% | +3.48% | 0.43 | 0.60 | -11.56% | 0.30 | 0.46 |
| in_sample | 2020-02-15 → 2024-12-31 | +21.04% | +3.99% | 0.46 | 0.65 | -11.56% | 0.34 | 0.50 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +2.76% | +1.84% | 0.28 | 0.40 | -7.09% | 0.26 | 0.32 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +3.38% | +4.54% | 0.76 | 1.09 | -4.83% | 0.94 | 0.95 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | +0.00% | 17% | -7.23% | -7.60% | 0.00 | 0 | 0% |
| out_of_sample | 532 | +0.00% | 10% | -4.59% | -4.83% | 0.00 | 0 | 0% |
| in_sample | 1768 | +0.00% | 19% | -7.23% | -7.60% | 0.00 | 0 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.024% | 5% | 1.16 | +4.09% |
| bull | 659 | 28% | +0.042% | 15% | 1.01 | +29.33% |
| bear | 399 | 17% | +0.001% | 3% | 0.96 | +0.49% |
| chop | 1099 | 47% | -0.007% | 8% | -0.55 | -8.05% |

## Turnover, fees, activity

- trades: 384 (0.16/day); active days 8%
- turnover 10.2x equity/year; fees 1.02% of equity/year ($766 total)
- average gross exposure 0.02; brake active 0.6% of hours
- correlation of daily returns with s3v2 baseline: 0.07
