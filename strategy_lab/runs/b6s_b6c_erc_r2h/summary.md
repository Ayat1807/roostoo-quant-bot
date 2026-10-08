# Run: b6s_b6c_erc_r2h

Strategy `s3v2x_alloc`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'alloc': 'erc'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +101.75% | +11.15% | 0.72 | 1.09 | -19.91% | 0.56 | 0.82 |
| in_sample | 2020-02-15 → 2024-12-31 | +91.07% | +14.18% | 0.87 | 1.34 | -14.00% | 1.01 | 1.10 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +5.67% | +3.19% | 0.28 | 0.40 | -19.91% | 0.16 | 0.29 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +6.86% | +6.86% | 0.45 | 0.67 | -19.91% | 0.34 | 0.50 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.37% | 42% | -8.33% | -8.43% | -2.50 | 14 | 99% |
| out_of_sample | 628 | -0.65% | 39% | -8.33% | -8.43% | -3.44 | 14 | 100% |
| in_sample | 1768 | -0.26% | 44% | -4.81% | -6.98% | -2.17 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.359% | 51% | 4.48 | +84.23% |
| bull | 687 | 28% | +0.020% | 42% | 0.54 | +12.79% |
| bear | 400 | 17% | +0.055% | 41% | 1.22 | +22.73% |
| chop | 1160 | 48% | -0.015% | 37% | -0.31 | -19.36% |

## Turnover, fees, activity

- trades: 11868 (4.90/day); active days 100%
- turnover 125.9x equity/year; fees 12.59% of equity/year ($70,556 total)
- average gross exposure 0.17; brake active 17.1% of hours
- correlation of daily returns with s3v2 baseline: 0.72
