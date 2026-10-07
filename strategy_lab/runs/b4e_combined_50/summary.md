# Run: b4e_combined_50

Strategy `xsmom`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +242.92% | +20.39% | 0.69 | 0.96 | -64.12% | 0.32 | 0.69 |
| in_sample | 2020-02-15 → 2024-12-31 | +320.24% | +34.19% | 0.96 | 1.31 | -64.12% | 0.53 | 0.97 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -18.69% | -11.10% | -0.28 | -0.39 | -32.86% | -0.34 | -0.34 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -2.94% | -2.94% | 0.00 | 0.01 | -25.87% | -0.11 | -0.03 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.16% | 40% | -19.43% | -20.42% | -2.43 | 12 | 32% |
| out_of_sample | 628 | -1.96% | 36% | -11.97% | -13.23% | -4.05 | 12 | 21% |
| in_sample | 1768 | -0.93% | 42% | -19.43% | -20.42% | -1.91 | 12 | 36% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.528% | 42% | 3.19 | +132.23% |
| bull | 687 | 28% | +0.264% | 49% | 2.33 | +420.97% |
| bear | 400 | 17% | -0.224% | 29% | -3.42 | -60.43% |
| chop | 1160 | 48% | -0.019% | 35% | -0.27 | -28.36% |

## Turnover, fees, activity

- trades: 14506 (5.98/day); active days 82%
- turnover 168.8x equity/year; fees 16.88% of equity/year ($218,546 total)
- average gross exposure 0.30; brake active 46.1% of hours
- correlation of daily returns with s3v2 baseline: 0.37
