# Run: b3_regime_cons_core10

Strategy `regime_switch`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'base_tv': 0.4}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +109.33% | +11.77% | 0.57 | 0.81 | -39.27% | 0.30 | 0.58 |
| in_sample | 2020-02-15 → 2024-12-31 | +105.62% | +15.91% | 0.69 | 0.99 | -39.27% | 0.41 | 0.72 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +1.96% | +1.11% | 0.16 | 0.23 | -28.30% | 0.04 | 0.15 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +14.08% | +14.08% | 0.69 | 1.00 | -17.48% | 0.81 | 0.85 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.60% | 39% | -15.06% | -16.49% | -3.15 | 14 | 97% |
| out_of_sample | 628 | -0.93% | 34% | -11.09% | -11.96% | -3.88 | 14 | 95% |
| in_sample | 1768 | -0.48% | 42% | -15.06% | -16.49% | -2.64 | 14 | 98% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.371% | 58% | 3.26 | +84.22% |
| bull | 687 | 28% | +0.114% | 52% | 1.51 | +104.55% |
| bear | 400 | 17% | -0.001% | 43% | -0.02 | -2.61% |
| chop | 1160 | 48% | -0.039% | 42% | -0.65 | -41.32% |

## Turnover, fees, activity

- trades: 6390 (2.64/day); active days 100%
- turnover 73.4x equity/year; fees 7.34% of equity/year ($43,567 total)
- average gross exposure 0.22; brake active 25.5% of hours
- correlation of daily returns with s3v2 baseline: 0.70
