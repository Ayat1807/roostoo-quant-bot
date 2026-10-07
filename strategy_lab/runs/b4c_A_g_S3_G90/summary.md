# Run: b4c_A_g_S3_G90

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 3, 'gross_cap': 0.9, 'short_gate': 'btc_below_30d'}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +129.70% | +13.34% | 0.52 | 0.72 | -78.38% | 0.17 | 0.49 |
| in_sample | 2020-02-15 → 2024-12-31 | +433.78% | +40.92% | 1.04 | 1.45 | -59.72% | 0.69 | 1.10 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -56.97% | -38.10% | -1.44 | -1.98 | -62.31% | -0.61 | -1.41 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -25.85% | -25.85% | -0.98 | -1.36 | -39.78% | -0.65 | -1.03 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.19% | 40% | -21.58% | -23.41% | -2.05 | 14 | 76% |
| out_of_sample | 628 | -2.74% | 30% | -13.43% | -14.96% | -5.00 | 14 | 68% |
| in_sample | 1768 | -0.53% | 44% | -21.58% | -23.41% | -0.90 | 14 | 79% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.719% | 52% | 3.79 | +215.88% |
| bull | 687 | 28% | +0.261% | 48% | 2.28 | +410.02% |
| bear | 400 | 17% | -0.144% | 43% | -1.84 | -46.16% |
| chop | 1160 | 48% | -0.104% | 38% | -1.39 | -73.52% |

## Turnover, fees, activity

- trades: 19316 (7.97/day); active days 95%
- turnover 237.3x equity/year; fees 23.73% of equity/year ($352,825 total)
- average gross exposure 0.39; brake active 51.7% of hours
- correlation of daily returns with s3v2 baseline: 0.53
