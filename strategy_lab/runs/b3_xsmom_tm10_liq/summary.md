# Run: b3_xsmom_tm10_liq

Strategy `xsmom`; universe `{'type': 'list', 'assets': ['ZECUSDT', 'PAXGUSDT', 'POLUSDT', 'ICPUSDT', 'TRXUSDT', 'CAKEUSDT', 'TUTUSDT', 'SOLUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +145.15% | +14.46% | 0.64 | 0.88 | -34.85% | 0.41 | 0.67 |
| in_sample | 2020-02-15 → 2024-12-31 | +61.03% | +10.25% | 0.51 | 0.68 | -34.85% | 0.29 | 0.51 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +52.05% | +26.92% | 0.98 | 1.43 | -22.94% | 1.17 | 1.22 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +64.27% | +64.27% | 1.80 | 2.67 | -22.94% | 2.80 | 2.45 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.41% | 44% | -11.27% | -13.41% | -1.37 | 12 | 24% |
| out_of_sample | 628 | -0.72% | 45% | -11.27% | -13.41% | -1.82 | 13 | 38% |
| in_sample | 1768 | -0.34% | 44% | -11.26% | -13.16% | -1.23 | 11 | 20% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.081% | 38% | 0.78 | +11.35% |
| bull | 687 | 28% | +0.178% | 45% | 2.23 | +214.60% |
| bear | 400 | 17% | -0.076% | 28% | -1.33 | -27.91% |
| chop | 1160 | 48% | +0.007% | 35% | 0.10 | -1.08% |

## Turnover, fees, activity

- trades: 7956 (3.28/day); active days 78%
- turnover 87.5x equity/year; fees 8.75% of equity/year ($37,305 total)
- average gross exposure 0.21; brake active 35.3% of hours
- correlation of daily returns with s3v2 baseline: 0.23
