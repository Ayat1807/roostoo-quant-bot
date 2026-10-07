# Run: b4x_trail5

Strategy `xsmom`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +27.80% | +3.76% | 0.27 | 0.38 | -68.41% | 0.06 | 0.25 |
| in_sample | 2020-02-15 → 2024-12-31 | +63.16% | +10.55% | 0.49 | 0.67 | -67.13% | 0.16 | 0.46 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -21.77% | -13.04% | -0.54 | -0.77 | -32.27% | -0.40 | -0.59 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -3.15% | -3.15% | -0.05 | -0.08 | -22.21% | -0.14 | -0.09 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.35% | 38% | -11.95% | -14.62% | -3.40 | 12 | 26% |
| out_of_sample | 628 | -1.48% | 34% | -10.93% | -11.91% | -4.64 | 11 | 14% |
| in_sample | 1768 | -1.21% | 39% | -11.95% | -14.62% | -3.11 | 12 | 31% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.403% | 45% | 3.56 | +94.86% |
| bull | 687 | 28% | +0.131% | 46% | 1.48 | +123.59% |
| bear | 400 | 17% | -0.212% | 28% | -4.50 | -57.86% |
| chop | 1160 | 48% | -0.025% | 36% | -0.41 | -30.40% |

## Turnover, fees, activity

- trades: 13422 (5.54/day); active days 79%
- turnover 194.6x equity/year; fees 19.46% of equity/year ($111,625 total)
- average gross exposure 0.22; brake active 46.3% of hours
- correlation of daily returns with s3v2 baseline: 0.36
