# Run: b4b_top3

Strategy `xsmom_sz`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'top_n': 3}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +200.33% | +18.01% | 0.60 | 0.85 | -75.44% | 0.24 | 0.59 |
| in_sample | 2020-02-15 → 2024-12-31 | +350.14% | +36.09% | 0.90 | 1.26 | -64.15% | 0.56 | 0.94 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -33.68% | -20.84% | -0.56 | -0.80 | -48.30% | -0.43 | -0.62 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +2.41% | +2.41% | 0.23 | 0.33 | -27.97% | 0.09 | 0.23 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.04% | 44% | -18.53% | -19.91% | -1.84 | 12 | 31% |
| out_of_sample | 628 | -2.69% | 38% | -13.06% | -18.66% | -5.12 | 12 | 21% |
| in_sample | 1768 | -0.47% | 46% | -18.53% | -19.91% | -0.72 | 12 | 35% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.714% | 47% | 3.52 | +208.44% |
| bull | 687 | 28% | +0.257% | 47% | 1.92 | +367.57% |
| bear | 400 | 17% | -0.229% | 31% | -2.97 | -61.80% |
| chop | 1160 | 48% | -0.037% | 34% | -0.41 | -45.49% |

## Turnover, fees, activity

- trades: 10607 (4.38/day); active days 82%
- turnover 222.3x equity/year; fees 22.23% of equity/year ($334,163 total)
- average gross exposure 0.33; brake active 48.7% of hours
- correlation of daily returns with s3v2 baseline: 0.32
