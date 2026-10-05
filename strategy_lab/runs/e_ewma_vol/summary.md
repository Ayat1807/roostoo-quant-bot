# Run: e_ewma_vol

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +165.82% | +16.57% | 1.09 | 1.60 | -16.85% | 0.98 | 1.26 |
| in_sample | 2020-02-15 → 2024-12-31 | +97.81% | +15.00% | 1.00 | 1.48 | -16.85% | 0.89 | 1.16 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +34.52% | +21.93% | 1.38 | 2.00 | -11.95% | 1.83 | 1.77 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +18.12% | +24.94% | 1.38 | 2.02 | -11.95% | 2.09 | 1.85 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.16% | 46% | -5.29% | -6.87% | -1.38 | 14 | 100% |
| out_of_sample | 532 | -0.06% | 48% | -5.16% | -6.44% | -0.28 | 14 | 100% |
| in_sample | 1768 | -0.17% | 46% | -5.29% | -6.87% | -1.61 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.198% | 58% | 2.77 | +37.81% |
| bull | 659 | 28% | +0.107% | 53% | 3.19 | +99.41% |
| bear | 399 | 17% | +0.046% | 47% | 1.34 | +19.03% |
| chop | 1099 | 47% | -0.013% | 44% | -0.32 | -16.39% |

## Turnover, fees, activity

- trades: 4812 (2.07/day); active days 100%
- turnover 38.9x equity/year; fees 3.89% of equity/year ($20,841 total)
- average gross exposure 0.18; brake active 8.7% of hours
- correlation of daily returns with s3v2 baseline: 0.92
