# Run: b8_s_U5

Strategy `s3v2x`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 20, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False, 'always_include_btc': True}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'n_divisor': 10, 'max_gross': 0.8}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +107.00% | +11.58% | 0.97 | 1.40 | -16.65% | 0.70 | 1.06 |
| in_sample | 2020-02-15 → 2024-12-31 | +96.61% | +14.85% | 1.16 | 1.67 | -16.65% | 0.89 | 1.28 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +5.39% | +3.03% | 0.35 | 0.49 | -9.20% | 0.33 | 0.40 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +4.15% | +4.15% | 0.43 | 0.60 | -9.20% | 0.45 | 0.50 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.18% | 44% | -5.53% | -6.53% | -1.66 | 14 | 99% |
| out_of_sample | 628 | -0.26% | 44% | -4.47% | -4.58% | -2.09 | 14 | 100% |
| in_sample | 1768 | -0.14% | 45% | -5.53% | -6.53% | -1.51 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.206% | 53% | 3.17 | +41.82% |
| bull | 687 | 28% | +0.076% | 50% | 2.52 | +66.80% |
| bear | 400 | 17% | +0.039% | 50% | 1.43 | +16.23% |
| chop | 1160 | 48% | -0.023% | 44% | -0.93 | -24.42% |

## Turnover, fees, activity

- trades: 5036 (2.08/day); active days 100%
- turnover 43.5x equity/year; fees 4.35% of equity/year ($22,445 total)
- average gross exposure 0.19; brake active 4.5% of hours
- correlation of daily returns with s3v2 baseline: 0.76
