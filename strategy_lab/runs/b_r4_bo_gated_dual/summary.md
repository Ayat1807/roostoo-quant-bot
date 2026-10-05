# Run: b_r4_bo_gated_dual

Strategy `sat_breakout`; universe `{'type': 'satellite', 'rule': 'R4', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'gate': 'alt_rally', 'dual': True}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +14.83% | +2.19% | 0.24 | 0.34 | -18.25% | 0.12 | 0.25 |
| in_sample | 2020-02-15 → 2024-12-31 | +8.06% | +1.60% | 0.19 | 0.27 | -18.25% | 0.09 | 0.19 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +6.26% | +4.15% | 0.44 | 0.63 | -9.72% | 0.43 | 0.51 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +0.37% | +0.49% | 0.11 | 0.16 | -4.77% | 0.10 | 0.13 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | +0.00% | 15% | -6.97% | -8.06% | 0.00 | 0 | 0% |
| out_of_sample | 532 | +0.00% | 12% | -4.57% | -6.80% | 0.00 | 0 | 0% |
| in_sample | 1768 | +0.00% | 16% | -6.97% | -8.06% | 0.00 | 0 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.042% | 4% | 1.84 | +7.27% |
| bull | 659 | 28% | +0.045% | 11% | 0.90 | +30.82% |
| bear | 399 | 17% | -0.002% | 0% | -0.62 | -0.95% |
| chop | 1099 | 47% | -0.017% | 3% | -0.89 | -17.38% |

## Turnover, fees, activity

- trades: 616 (0.26/day); active days 10%
- turnover 16.5x equity/year; fees 1.65% of equity/year ($1,100 total)
- average gross exposure 0.03; brake active 1.8% of hours
- correlation of daily returns with s3v2 baseline: 0.11
