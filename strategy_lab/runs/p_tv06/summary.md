# Run: p_tv06

Strategy `s3v2`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.6, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +162.45% | +15.64% | 0.69 | 1.00 | -29.56% | 0.53 | 0.77 |
| in_sample | 2020-02-15 → 2024-12-31 | +123.08% | +17.86% | 0.77 | 1.12 | -29.56% | 0.60 | 0.86 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +17.77% | +9.75% | 0.48 | 0.69 | -23.91% | 0.41 | 0.54 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +12.41% | +12.41% | 0.55 | 0.81 | -23.91% | 0.52 | 0.64 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.49% | 43% | -12.41% | -15.32% | -1.91 | 14 | 93% |
| out_of_sample | 628 | -0.67% | 43% | -12.41% | -15.32% | -2.29 | 14 | 85% |
| in_sample | 1768 | -0.44% | 43% | -9.87% | -12.20% | -1.66 | 14 | 96% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.314% | 52% | 2.61 | +66.03% |
| bull | 687 | 28% | +0.127% | 53% | 2.16 | +129.12% |
| bear | 400 | 17% | +0.051% | 46% | 0.74 | +18.64% |
| chop | 1160 | 48% | -0.034% | 44% | -0.52 | -38.66% |

## Turnover, fees, activity

- trades: 7976 (3.29/day); active days 99%
- turnover 82.5x equity/year; fees 8.25% of equity/year ($48,943 total)
- average gross exposure 0.30; brake active 38.3% of hours
- correlation of daily returns with s3v2 baseline: 0.87
