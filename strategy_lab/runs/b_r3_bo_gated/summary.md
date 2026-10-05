# Run: b_r3_bo_gated

Strategy `sat_breakout`; universe `{'type': 'satellite', 'rule': 'R3', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'gate': 'alt_rally'}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +17.49% | +2.56% | 0.26 | 0.36 | -23.67% | 0.11 | 0.25 |
| in_sample | 2020-02-15 → 2024-12-31 | +20.91% | +3.97% | 0.35 | 0.48 | -23.67% | 0.17 | 0.35 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -2.83% | -1.90% | -0.18 | -0.25 | -12.46% | -0.15 | -0.20 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -2.27% | -3.02% | -0.87 | -1.13 | -3.17% | -0.95 | -1.00 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | +0.00% | 14% | -9.19% | -9.64% | 0.00 | 0 | 0% |
| out_of_sample | 532 | +0.00% | 7% | -4.28% | -6.25% | 0.00 | 0 | 0% |
| in_sample | 1768 | +0.00% | 17% | -9.19% | -9.64% | 0.00 | 0 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.052% | 7% | 1.25 | +8.60% |
| bull | 659 | 28% | +0.059% | 13% | 1.26 | +43.57% |
| bear | 399 | 17% | -0.005% | 3% | -1.01 | -2.04% |
| chop | 1099 | 47% | -0.023% | 4% | -1.03 | -23.07% |

## Turnover, fees, activity

- trades: 528 (0.23/day); active days 10%
- turnover 12.6x equity/year; fees 1.26% of equity/year ($948 total)
- average gross exposure 0.03; brake active 3.0% of hours
- correlation of daily returns with s3v2 baseline: 0.08
