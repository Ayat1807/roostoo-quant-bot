# Run: b4x_stop6

Strategy `xsmom`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +239.36% | +20.20% | 0.70 | 0.96 | -66.33% | 0.30 | 0.69 |
| in_sample | 2020-02-15 → 2024-12-31 | +405.86% | +39.38% | 1.07 | 1.47 | -60.27% | 0.65 | 1.10 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -33.15% | -20.48% | -0.71 | -0.99 | -46.00% | -0.45 | -0.74 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -8.22% | -8.22% | -0.23 | -0.33 | -27.54% | -0.30 | -0.29 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.37% | 39% | -19.10% | -19.58% | -2.80 | 12 | 31% |
| out_of_sample | 628 | -2.55% | 35% | -11.98% | -15.10% | -5.11 | 12 | 21% |
| in_sample | 1768 | -1.00% | 41% | -19.10% | -19.58% | -2.10 | 12 | 35% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.659% | 44% | 4.10 | +193.31% |
| bull | 687 | 28% | +0.245% | 48% | 2.21 | +362.12% |
| bear | 400 | 17% | -0.252% | 32% | -4.09 | -64.53% |
| chop | 1160 | 48% | -0.021% | 35% | -0.29 | -29.42% |

## Turnover, fees, activity

- trades: 14165 (5.84/day); active days 82%
- turnover 171.5x equity/year; fees 17.15% of equity/year ($242,036 total)
- average gross exposure 0.29; brake active 49.7% of hours
- correlation of daily returns with s3v2 baseline: 0.38
