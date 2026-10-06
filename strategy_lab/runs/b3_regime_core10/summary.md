# Run: b3_regime_core10

Strategy `regime_switch`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'base_tv': 0.6}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +150.14% | +14.81% | 0.61 | 0.88 | -39.30% | 0.38 | 0.65 |
| in_sample | 2020-02-15 → 2024-12-31 | +139.64% | +19.60% | 0.73 | 1.05 | -39.30% | 0.50 | 0.79 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +4.57% | +2.57% | 0.23 | 0.33 | -24.92% | 0.10 | 0.23 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +8.92% | +8.92% | 0.44 | 0.65 | -21.93% | 0.41 | 0.52 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.74% | 41% | -14.80% | -16.49% | -2.53 | 14 | 92% |
| out_of_sample | 628 | -1.03% | 38% | -12.99% | -16.02% | -2.98 | 14 | 85% |
| in_sample | 1768 | -0.58% | 42% | -14.80% | -16.49% | -2.25 | 14 | 95% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.426% | 53% | 3.35 | +101.05% |
| bull | 687 | 28% | +0.129% | 54% | 1.48 | +121.11% |
| bear | 400 | 17% | +0.043% | 45% | 0.66 | +15.12% |
| chop | 1160 | 48% | -0.047% | 42% | -0.63 | -48.49% |

## Turnover, fees, activity

- trades: 8387 (3.46/day); active days 99%
- turnover 103.1x equity/year; fees 10.31% of equity/year ($76,989 total)
- average gross exposure 0.31; brake active 37.6% of hours
- correlation of daily returns with s3v2 baseline: 0.72
