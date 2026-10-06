# Run: b3_s3v2e_core10

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +182.82% | +16.95% | 1.10 | 1.62 | -16.85% | 1.01 | 1.28 |
| in_sample | 2020-02-15 → 2024-12-31 | +97.81% | +15.00% | 1.00 | 1.48 | -16.85% | 0.89 | 1.16 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +43.13% | +22.63% | 1.37 | 2.01 | -12.92% | 1.75 | 1.74 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +25.45% | +25.45% | 1.37 | 2.02 | -12.92% | 1.97 | 1.81 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.17% | 46% | -6.02% | -6.87% | -1.44 | 14 | 100% |
| out_of_sample | 628 | -0.14% | 47% | -6.02% | -6.46% | -0.68 | 14 | 100% |
| in_sample | 1768 | -0.17% | 46% | -5.29% | -6.87% | -1.61 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.255% | 58% | 3.28 | +53.51% |
| bull | 687 | 28% | +0.104% | 53% | 3.14 | +101.83% |
| bear | 400 | 17% | +0.044% | 47% | 1.29 | +18.33% |
| chop | 1160 | 48% | -0.017% | 43% | -0.41 | -20.63% |

## Turnover, fees, activity

- trades: 5109 (2.11/day); active days 100%
- turnover 41.0x equity/year; fees 4.10% of equity/year ($23,380 total)
- average gross exposure 0.18; brake active 9.5% of hours
