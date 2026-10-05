# Run: b_r3_tr

Strategy `sat_trend`; universe `{'type': 'satellite', 'rule': 'R3', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'vol_band': [0.5, 1.3], 'crash_guard': True, 'core_run': 'b2_core'}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.02; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +113.44% | +12.62% | 0.60 | 0.83 | -36.60% | 0.34 | 0.62 |
| in_sample | 2020-02-15 → 2024-12-31 | +119.57% | +17.48% | 0.75 | 1.02 | -36.60% | 0.48 | 0.78 |
| out_of_sample | 2025-01-01 → 2026-06-30 | -2.79% | -1.87% | 0.01 | 0.01 | -18.71% | -0.10 | -0.02 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +6.95% | +9.40% | 0.57 | 0.84 | -11.13% | 0.84 | 0.76 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.48% | 41% | -10.60% | -11.45% | -2.14 | 10 | 13% |
| out_of_sample | 532 | -0.66% | 38% | -7.67% | -8.56% | -2.63 | 11 | 14% |
| in_sample | 1768 | -0.43% | 42% | -10.60% | -11.45% | -1.86 | 10 | 13% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.087% | 29% | 1.06 | +13.55% |
| bull | 659 | 28% | +0.212% | 42% | 2.52 | +270.55% |
| bear | 399 | 17% | -0.106% | 29% | -2.39 | -35.36% |
| chop | 1099 | 47% | -0.018% | 34% | -0.36 | -21.52% |

## Turnover, fees, activity

- trades: 3612 (1.55/day); active days 66%
- turnover 62.3x equity/year; fees 6.23% of equity/year ($6,659 total)
- average gross exposure 0.19; brake active 12.6% of hours
- correlation of daily returns with s3v2 baseline: 0.28
