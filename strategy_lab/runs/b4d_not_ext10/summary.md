# Run: b4d_not_ext10

Strategy `xsmom_entry`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'entry_filter': 'not_extended', 'ext': 0.1}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +116.39% | +12.33% | 0.55 | 0.75 | -69.04% | 0.18 | 0.52 |
| in_sample | 2020-02-15 → 2024-12-31 | +197.98% | +25.06% | 0.89 | 1.22 | -59.16% | 0.42 | 0.88 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -27.47% | -16.70% | -0.68 | -0.94 | -44.56% | -0.37 | -0.69 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -3.28% | -3.28% | -0.04 | -0.06 | -29.83% | -0.11 | -0.07 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.31% | 37% | -11.75% | -13.75% | -3.35 | 11 | 19% |
| out_of_sample | 628 | -1.76% | 33% | -11.75% | -13.75% | -4.97 | 11 | 12% |
| in_sample | 1768 | -1.08% | 39% | -9.65% | -12.47% | -2.93 | 11 | 21% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.345% | 45% | 3.04 | +76.00% |
| bull | 687 | 28% | +0.235% | 46% | 2.49 | +350.02% |
| bear | 400 | 17% | -0.195% | 28% | -4.09 | -54.86% |
| chop | 1160 | 48% | -0.036% | 33% | -0.54 | -39.47% |

## Turnover, fees, activity

- trades: 11460 (4.73/day); active days 75%
- turnover 133.8x equity/year; fees 13.38% of equity/year ($126,079 total)
- average gross exposure 0.26; brake active 44.5% of hours
- correlation of daily returns with s3v2 baseline: 0.41
