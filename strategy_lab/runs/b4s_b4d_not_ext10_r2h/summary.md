# Run: b4s_b4d_not_ext10_r2h

Strategy `xsmom_entry`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'entry_filter': 'not_extended', 'ext': 0.1}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +11.06% | +1.59% | 0.20 | 0.28 | -83.19% | 0.02 | 0.18 |
| in_sample | 2020-02-15 → 2024-12-31 | +95.17% | +14.68% | 0.59 | 0.80 | -71.04% | 0.21 | 0.56 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -43.10% | -27.44% | -1.27 | -1.76 | -56.10% | -0.49 | -1.23 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -23.32% | -23.32% | -1.14 | -1.60 | -38.86% | -0.60 | -1.16 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.52% | 37% | -11.18% | -12.69% | -3.70 | 12 | 30% |
| out_of_sample | 628 | -2.42% | 28% | -10.93% | -12.10% | -6.11 | 12 | 24% |
| in_sample | 1768 | -1.17% | 40% | -11.18% | -12.69% | -2.89 | 12 | 32% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.448% | 45% | 3.39 | +107.82% |
| bull | 687 | 28% | +0.194% | 46% | 2.03 | +237.75% |
| bear | 400 | 17% | -0.225% | 28% | -4.18 | -60.18% |
| chop | 1160 | 48% | -0.071% | 32% | -1.03 | -60.27% |

## Turnover, fees, activity

- trades: 73987 (30.52/day); active days 81%
- turnover 339.7x equity/year; fees 33.97% of equity/year ($268,536 total)
- average gross exposure 0.27; brake active 49.2% of hours
- correlation of daily returns with s3v2 baseline: 0.40
