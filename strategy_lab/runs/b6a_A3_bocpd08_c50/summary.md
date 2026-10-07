# Run: b6a_A3_bocpd08_c50

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +103.56% | +11.30% | 0.88 | 1.29 | -16.99% | 0.67 | 0.98 |
| in_sample | 2020-02-15 → 2024-12-31 | +63.23% | +10.56% | 0.84 | 1.24 | -16.99% | 0.62 | 0.93 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +24.84% | +13.45% | 0.99 | 1.43 | -11.48% | 1.17 | 1.22 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +10.98% | +10.98% | 0.78 | 1.13 | -11.48% | 0.96 | 0.97 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.20% | 43% | -6.59% | -7.07% | -1.96 | 14 | 100% |
| out_of_sample | 628 | -0.17% | 46% | -5.69% | -6.11% | -0.90 | 14 | 100% |
| in_sample | 1768 | -0.21% | 43% | -6.59% | -7.07% | -2.26 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.209% | 59% | 3.20 | +42.59% |
| bull | 687 | 28% | +0.079% | 54% | 2.66 | +70.06% |
| bear | 400 | 17% | +0.039% | 46% | 1.27 | +16.11% |
| chop | 1160 | 48% | -0.023% | 43% | -0.62 | -25.69% |

## Turnover, fees, activity

- trades: 5550 (2.29/day); active days 100%
- turnover 41.0x equity/year; fees 4.10% of equity/year ($19,694 total)
- average gross exposure 0.17; brake active 7.0% of hours
- correlation of daily returns with s3v2 baseline: 0.82
