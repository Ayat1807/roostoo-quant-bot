# Run: b3s_xsmom_r1_r2h

Strategy `xsmom`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +18.82% | +2.63% | 0.25 | 0.35 | -87.00% | 0.03 | 0.23 |
| in_sample | 2020-02-15 → 2024-12-31 | +129.77% | +18.58% | 0.63 | 0.87 | -79.55% | 0.23 | 0.61 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -48.41% | -31.38% | -1.17 | -1.62 | -60.21% | -0.52 | -1.16 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -27.28% | -27.28% | -1.09 | -1.52 | -42.68% | -0.64 | -1.13 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.76% | 37% | -18.70% | -19.63% | -3.40 | 13 | 37% |
| out_of_sample | 628 | -2.65% | 29% | -12.92% | -13.65% | -5.17 | 13 | 28% |
| in_sample | 1768 | -1.38% | 40% | -18.70% | -19.63% | -2.60 | 13 | 40% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.815% | 53% | 4.64 | +279.28% |
| bull | 687 | 28% | +0.243% | 46% | 2.04 | +344.34% |
| bear | 400 | 17% | -0.278% | 32% | -4.11 | -68.20% |
| chop | 1160 | 48% | -0.120% | 34% | -1.68 | -77.83% |

## Turnover, fees, activity

- trades: 83468 (34.43/day); active days 85%
- turnover 409.5x equity/year; fees 40.95% of equity/year ($330,816 total)
- average gross exposure 0.30; brake active 51.6% of hours
- correlation of daily returns with s3v2 baseline: 0.34
