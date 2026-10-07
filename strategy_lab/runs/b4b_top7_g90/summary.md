# Run: b4b_top7_g90

Strategy `xsmom_sz`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'top_n': 7, 'gross': 0.9}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +43.24% | +5.56% | 0.33 | 0.45 | -77.77% | 0.07 | 0.30 |
| in_sample | 2020-02-15 → 2024-12-31 | +127.20% | +18.31% | 0.62 | 0.84 | -60.74% | 0.30 | 0.61 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -37.34% | -23.35% | -0.73 | -1.00 | -51.84% | -0.45 | -0.75 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -16.60% | -16.60% | -0.55 | -0.77 | -35.98% | -0.46 | -0.61 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.45% | 38% | -17.11% | -19.69% | -2.91 | 12 | 33% |
| out_of_sample | 628 | -2.60% | 32% | -13.19% | -17.13% | -4.97 | 12 | 21% |
| in_sample | 1768 | -1.10% | 40% | -17.11% | -19.69% | -2.12 | 12 | 37% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.624% | 47% | 3.79 | +174.76% |
| bull | 687 | 28% | +0.199% | 47% | 1.67 | +229.69% |
| bear | 400 | 17% | -0.222% | 32% | -3.23 | -60.28% |
| chop | 1160 | 48% | -0.069% | 36% | -0.88 | -60.19% |

## Turnover, fees, activity

- trades: 18541 (7.65/day); active days 82%
- turnover 185.8x equity/year; fees 18.58% of equity/year ($149,028 total)
- average gross exposure 0.31; brake active 46.7% of hours
- correlation of daily returns with s3v2 baseline: 0.38
