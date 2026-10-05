# Run: b_r1_tr_dual

Strategy `sat_trend`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'dual': True}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | -13.56% | -2.26% | 0.03 | 0.04 | -61.24% | -0.04 | 0.01 |
| in_sample | 2020-02-15 → 2024-12-31 | +6.87% | +1.37% | 0.18 | 0.25 | -50.69% | 0.03 | 0.16 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -19.11% | -13.22% | -0.59 | -0.84 | -29.89% | -0.44 | -0.64 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | -11.95% | -15.65% | -0.74 | -1.05 | -23.76% | -0.66 | -0.84 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.88% | 37% | -8.80% | -11.45% | -2.82 | 10 | 20% |
| out_of_sample | 532 | -0.99% | 38% | -8.12% | -8.77% | -2.92 | 12 | 22% |
| in_sample | 1768 | -0.81% | 37% | -8.80% | -11.45% | -2.75 | 10 | 19% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.174% | 34% | 1.96 | +31.20% |
| bull | 659 | 28% | +0.130% | 39% | 1.63 | +118.32% |
| bear | 399 | 17% | -0.212% | 23% | -4.29 | -57.86% |
| chop | 1099 | 47% | -0.025% | 33% | -0.49 | -28.39% |

## Turnover, fees, activity

- trades: 4518 (1.94/day); active days 66%
- turnover 72.7x equity/year; fees 7.27% of equity/year ($5,675 total)
- average gross exposure 0.19; brake active 21.6% of hours
- correlation of daily returns with s3v2 baseline: 0.24
