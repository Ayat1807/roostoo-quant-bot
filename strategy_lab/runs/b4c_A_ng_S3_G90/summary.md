# Run: b4c_A_ng_S3_G90

Strategy `xsmom_lsx`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_short': 3, 'gross_cap': 0.9, 'short_gate': 'none'}`; band 0.06; brake True; shorts True; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +32.96% | +4.38% | 0.30 | 0.42 | -81.37% | 0.05 | 0.28 |
| in_sample | 2020-02-15 → 2024-12-31 | +263.80% | +30.28% | 0.86 | 1.20 | -61.48% | 0.49 | 0.88 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -63.48% | -43.62% | -1.68 | -2.34 | -67.39% | -0.65 | -1.64 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -27.36% | -27.36% | -1.04 | -1.46 | -42.84% | -0.64 | -1.08 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.97% | 43% | -21.58% | -23.41% | -1.73 | 14 | 98% |
| out_of_sample | 628 | -2.90% | 32% | -14.69% | -18.96% | -4.93 | 14 | 100% |
| in_sample | 1768 | -0.25% | 47% | -21.58% | -23.41% | -0.30 | 14 | 97% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.618% | 50% | 3.31 | +165.59% |
| bull | 687 | 28% | +0.153% | 49% | 1.33 | +142.92% |
| bear | 400 | 17% | -0.146% | 42% | -1.83 | -46.91% |
| chop | 1160 | 48% | -0.071% | 40% | -0.93 | -61.18% |

## Turnover, fees, activity

- trades: 22872 (9.44/day); active days 98%
- turnover 272.3x equity/year; fees 27.23% of equity/year ($270,028 total)
- average gross exposure 0.45; brake active 50.9% of hours
- correlation of daily returns with s3v2 baseline: 0.49
