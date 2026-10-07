# Run: b4s_b4d_not_ext10_r4h

Strategy `xsmom_entry`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'entry_filter': 'not_extended', 'ext': 0.1}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +222.78% | +19.30% | 0.74 | 1.02 | -72.20% | 0.27 | 0.71 |
| in_sample | 2020-02-15 → 2024-12-31 | +368.48% | +37.21% | 1.15 | 1.58 | -56.74% | 0.66 | 1.18 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -31.10% | -19.10% | -0.80 | -1.11 | -47.90% | -0.40 | -0.80 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -8.89% | -8.89% | -0.33 | -0.47 | -29.21% | -0.30 | -0.38 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.96% | 40% | -10.46% | -11.80% | -2.74 | 12 | 28% |
| out_of_sample | 628 | -2.06% | 35% | -9.93% | -11.16% | -5.27 | 12 | 23% |
| in_sample | 1768 | -0.77% | 42% | -10.46% | -11.80% | -1.89 | 12 | 30% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.599% | 55% | 4.34 | +169.74% |
| bull | 687 | 28% | +0.232% | 50% | 2.40 | +336.97% |
| bear | 400 | 17% | -0.176% | 40% | -3.31 | -51.50% |
| chop | 1160 | 48% | -0.041% | 39% | -0.59 | -43.54% |

## Turnover, fees, activity

- trades: 41033 (16.93/day); active days 80%
- turnover 256.4x equity/year; fees 25.64% of equity/year ($392,999 total)
- average gross exposure 0.27; brake active 49.3% of hours
- correlation of daily returns with s3v2 baseline: 0.40
