# Run: b6s_b6c_erc_r6h

Strategy `s3v2x_alloc`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'alloc': 'erc'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +179.83% | +16.76% | 1.01 | 1.52 | -18.96% | 0.88 | 1.18 |
| in_sample | 2020-02-15 → 2024-12-31 | +147.38% | +20.39% | 1.19 | 1.80 | -12.66% | 1.61 | 1.56 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +13.26% | +7.34% | 0.51 | 0.75 | -18.96% | 0.39 | 0.57 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +10.06% | +10.06% | 0.60 | 0.87 | -18.96% | 0.53 | 0.69 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.22% | 46% | -5.63% | -7.46% | -1.58 | 14 | 99% |
| out_of_sample | 628 | -0.56% | 40% | -5.63% | -6.93% | -2.90 | 14 | 100% |
| in_sample | 1768 | -0.10% | 48% | -5.38% | -7.46% | -0.60 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.394% | 56% | 4.68 | +95.58% |
| bull | 687 | 28% | +0.059% | 47% | 1.57 | +47.78% |
| bear | 400 | 17% | +0.046% | 45% | 1.06 | +18.70% |
| chop | 1160 | 48% | -0.012% | 38% | -0.25 | -16.24% |

## Turnover, fees, activity

- trades: 8101 (3.34/day); active days 100%
- turnover 82.3x equity/year; fees 8.23% of equity/year ($54,002 total)
- average gross exposure 0.17; brake active 14.7% of hours
- correlation of daily returns with s3v2 baseline: 0.76
