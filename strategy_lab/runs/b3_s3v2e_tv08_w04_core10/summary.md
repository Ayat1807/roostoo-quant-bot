# Run: b3_s3v2e_tv08_w04_core10

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.4, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +129.64% | +13.34% | 0.55 | 0.79 | -46.11% | 0.29 | 0.57 |
| in_sample | 2020-02-15 → 2024-12-31 | +124.72% | +18.04% | 0.68 | 0.97 | -46.11% | 0.39 | 0.71 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +2.30% | +1.30% | 0.20 | 0.29 | -26.66% | 0.05 | 0.19 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +4.02% | +4.02% | 0.28 | 0.41 | -26.66% | 0.15 | 0.29 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.79% | 43% | -17.12% | -17.61% | -1.90 | 14 | 89% |
| out_of_sample | 628 | -0.90% | 44% | -15.88% | -17.61% | -1.84 | 14 | 82% |
| in_sample | 1768 | -0.72% | 43% | -17.12% | -17.28% | -1.84 | 14 | 91% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.336% | 48% | 2.18 | +67.45% |
| bull | 687 | 28% | +0.176% | 52% | 2.31 | +211.46% |
| bear | 400 | 17% | +0.019% | 44% | 0.22 | +2.33% |
| chop | 1160 | 48% | -0.054% | 43% | -0.65 | -53.39% |

## Turnover, fees, activity

- trades: 10183 (4.20/day); active days 99%
- turnover 111.4x equity/year; fees 11.14% of equity/year ($71,883 total)
- average gross exposure 0.37; brake active 45.9% of hours
- correlation of daily returns with s3v2 baseline: 0.79
