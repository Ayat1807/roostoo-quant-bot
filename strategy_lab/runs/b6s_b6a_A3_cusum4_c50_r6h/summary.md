# Run: b6s_b6a_A3_cusum4_c50_r6h

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +177.44% | +16.61% | 1.23 | 1.88 | -13.29% | 1.25 | 1.49 |
| in_sample | 2020-02-15 → 2024-12-31 | +118.83% | +17.40% | 1.30 | 1.99 | -12.90% | 1.35 | 1.59 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +26.87% | +14.50% | 1.06 | 1.58 | -13.29% | 1.09 | 1.28 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +12.05% | +12.05% | 0.81 | 1.21 | -13.29% | 0.91 | 1.00 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.06% | 48% | -4.52% | -5.57% | -0.62 | 14 | 100% |
| out_of_sample | 628 | -0.21% | 44% | -4.52% | -5.22% | -1.68 | 14 | 100% |
| in_sample | 1768 | -0.01% | 49% | -4.24% | -5.57% | -0.14 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.336% | 56% | 5.14 | +78.23% |
| bull | 687 | 28% | +0.058% | 47% | 2.02 | +47.89% |
| bear | 400 | 17% | +0.053% | 44% | 1.61 | +22.63% |
| chop | 1160 | 48% | -0.008% | 39% | -0.21 | -12.16% |

## Turnover, fees, activity

- trades: 7638 (3.15/day); active days 100%
- turnover 63.1x equity/year; fees 6.31% of equity/year ($38,303 total)
- average gross exposure 0.16; brake active 6.5% of hours
- correlation of daily returns with s3v2 baseline: 0.77
