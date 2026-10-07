# Run: b6a_A3_bocpd05_c50

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +122.04% | +12.76% | 1.01 | 1.50 | -18.47% | 0.69 | 1.11 |
| in_sample | 2020-02-15 → 2024-12-31 | +76.60% | +12.35% | 0.99 | 1.47 | -18.47% | 0.67 | 1.09 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +25.86% | +13.98% | 1.08 | 1.57 | -11.42% | 1.22 | 1.32 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +11.57% | +11.57% | 0.84 | 1.23 | -11.42% | 1.01 | 1.05 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.16% | 45% | -6.96% | -7.22% | -1.45 | 14 | 100% |
| out_of_sample | 628 | -0.14% | 48% | -5.57% | -5.99% | -0.98 | 14 | 100% |
| in_sample | 1768 | -0.15% | 45% | -6.96% | -7.22% | -1.55 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.216% | 60% | 3.47 | +44.54% |
| bull | 687 | 28% | +0.082% | 53% | 2.82 | +73.55% |
| bear | 400 | 17% | +0.040% | 48% | 1.35 | +16.58% |
| chop | 1160 | 48% | -0.019% | 43% | -0.53 | -21.97% |

## Turnover, fees, activity

- trades: 5757 (2.38/day); active days 100%
- turnover 41.9x equity/year; fees 4.19% of equity/year ($20,713 total)
- average gross exposure 0.16; brake active 5.3% of hours
- correlation of daily returns with s3v2 baseline: 0.82
