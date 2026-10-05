# Run: b_r1_tr_rvb

Strategy `sat_trend`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'riskoff': 'vol_breadth'}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | -34.70% | -6.46% | -0.10 | -0.13 | -69.13% | -0.09 | -0.11 |
| in_sample | 2020-02-15 → 2024-12-31 | -2.35% | -0.49% | 0.13 | 0.17 | -47.32% | -0.01 | 0.10 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -33.13% | -23.59% | -0.96 | -1.30 | -42.54% | -0.55 | -0.98 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -14.38% | -18.75% | -0.77 | -1.07 | -28.25% | -0.66 | -0.86 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | +0.00% | 26% | -9.22% | -11.45% | 0.00 | 4 | 3% |
| out_of_sample | 532 | -0.02% | 27% | -8.18% | -9.38% | -1.31 | 3 | 0% |
| in_sample | 1768 | +0.00% | 26% | -9.22% | -11.45% | 0.00 | 4 | 3% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.399% | 15% | 4.04 | +91.23% |
| bull | 659 | 28% | +0.062% | 26% | 0.68 | +36.27% |
| bear | 399 | 17% | -0.126% | 15% | -2.25 | -40.87% |
| chop | 1099 | 47% | -0.071% | 15% | -1.13 | -57.62% |

## Turnover, fees, activity

- trades: 4265 (1.83/day); active days 31%
- turnover 61.6x equity/year; fees 6.16% of equity/year ($4,510 total)
- average gross exposure 0.16; brake active 27.0% of hours
- correlation of daily returns with s3v2 baseline: 0.25
