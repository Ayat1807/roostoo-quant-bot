# Run: b6a_A3_cusum8_c0

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +146.93% | +14.58% | 1.01 | 1.49 | -17.76% | 0.82 | 1.15 |
| in_sample | 2020-02-15 → 2024-12-31 | +81.76% | +13.02% | 0.93 | 1.38 | -17.76% | 0.73 | 1.05 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +36.00% | +19.12% | 1.23 | 1.79 | -13.03% | 1.47 | 1.52 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +20.35% | +20.35% | 1.19 | 1.74 | -13.03% | 1.56 | 1.52 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.22% | 43% | -7.19% | -8.18% | -2.05 | 14 | 100% |
| out_of_sample | 628 | -0.20% | 45% | -6.04% | -6.45% | -1.35 | 14 | 100% |
| in_sample | 1768 | -0.22% | 43% | -7.19% | -8.18% | -2.40 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.231% | 57% | 3.10 | +47.56% |
| bull | 687 | 28% | +0.087% | 52% | 2.60 | +78.98% |
| bear | 400 | 17% | +0.042% | 48% | 1.27 | +17.53% |
| chop | 1160 | 48% | -0.014% | 43% | -0.35 | -17.95% |

## Turnover, fees, activity

- trades: 5072 (2.09/day); active days 100%
- turnover 41.0x equity/year; fees 4.10% of equity/year ($21,216 total)
- average gross exposure 0.17; brake active 8.9% of hours
- correlation of daily returns with s3v2 baseline: 0.84
