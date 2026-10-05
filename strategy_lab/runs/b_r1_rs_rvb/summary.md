# Run: b_r1_rs_rvb

Strategy `sat_rs`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'riskoff': 'vol_breadth'}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | -44.62% | -8.85% | -0.19 | -0.26 | -66.75% | -0.13 | -0.20 |
| in_sample | 2020-02-15 → 2024-12-31 | -22.92% | -5.19% | -0.04 | -0.05 | -57.14% | -0.09 | -0.06 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -28.15% | -19.83% | -0.79 | -1.09 | -30.84% | -0.64 | -0.87 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -24.64% | -31.50% | -1.56 | -2.15 | -25.70% | -1.23 | -1.70 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | +0.00% | 34% | -11.69% | -13.25% | 0.00 | 2 | 0% |
| out_of_sample | 532 | -0.00% | 33% | -9.11% | -9.42% | -0.21 | 2 | 0% |
| in_sample | 1768 | +0.00% | 34% | -11.69% | -13.25% | 0.00 | 3 | 0% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.215% | 17% | 2.94 | +41.74% |
| bull | 659 | 28% | +0.110% | 26% | 1.28 | +88.89% |
| bear | 399 | 17% | -0.171% | 15% | -3.49 | -50.27% |
| chop | 1099 | 47% | -0.072% | 22% | -1.09 | -58.41% |

## Turnover, fees, activity

- trades: 1368 (0.59/day); active days 22%
- turnover 34.8x equity/year; fees 3.48% of equity/year ($2,191 total)
- average gross exposure 0.16; brake active 30.9% of hours
- correlation of daily returns with s3v2 baseline: 0.21
