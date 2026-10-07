# Run: b7_erc_cusum

Strategy `s3v2x_alloc`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'alloc': 'erc'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +96.07% | +10.67% | 0.79 | 1.18 | -19.67% | 0.54 | 0.87 |
| in_sample | 2020-02-15 → 2024-12-31 | +65.45% | +10.86% | 0.78 | 1.18 | -19.67% | 0.55 | 0.87 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +18.67% | +10.23% | 0.81 | 1.18 | -11.33% | 0.90 | 0.98 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +11.03% | +11.03% | 0.78 | 1.15 | -11.33% | 0.97 | 0.98 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.19% | 44% | -6.74% | -7.04% | -1.40 | 14 | 100% |
| out_of_sample | 628 | -0.08% | 49% | -5.20% | -6.49% | -0.32 | 14 | 100% |
| in_sample | 1768 | -0.20% | 43% | -6.74% | -7.04% | -1.72 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.232% | 55% | 3.47 | +48.37% |
| bull | 687 | 28% | +0.052% | 50% | 1.62 | +41.26% |
| bear | 400 | 17% | +0.021% | 45% | 0.65 | +7.94% |
| chop | 1160 | 48% | -0.007% | 44% | -0.17 | -10.70% |

## Turnover, fees, activity

- trades: 6165 (2.54/day); active days 100%
- turnover 47.8x equity/year; fees 4.78% of equity/year ($21,955 total)
- average gross exposure 0.17; brake active 8.3% of hours
- correlation of daily returns with s3v2 baseline: 0.79
