# Run: b6s_b6c_erc_r12h

Strategy `s3v2x_alloc`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'alloc': 'erc'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +280.01% | +22.27% | 1.27 | 1.90 | -18.62% | 1.20 | 1.50 |
| in_sample | 2020-02-15 → 2024-12-31 | +190.71% | +24.43% | 1.36 | 2.05 | -12.66% | 1.93 | 1.81 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +30.86% | +16.53% | 1.01 | 1.48 | -18.62% | 0.89 | 1.16 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +22.19% | +22.19% | 1.13 | 1.67 | -18.62% | 1.19 | 1.37 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.08% | 48% | -7.13% | -8.50% | -0.58 | 14 | 100% |
| out_of_sample | 628 | -0.24% | 46% | -5.37% | -6.65% | -1.49 | 14 | 100% |
| in_sample | 1768 | -0.03% | 49% | -7.13% | -8.50% | -0.19 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.361% | 56% | 4.15 | +84.27% |
| bull | 687 | 28% | +0.081% | 49% | 2.01 | +71.29% |
| bear | 400 | 17% | +0.069% | 47% | 1.68 | +30.19% |
| chop | 1160 | 48% | -0.001% | 43% | -0.01 | -5.09% |

## Turnover, fees, activity

- trades: 6449 (2.66/day); active days 100%
- turnover 62.1x equity/year; fees 6.21% of equity/year ($46,152 total)
- average gross exposure 0.18; brake active 13.4% of hours
- correlation of daily returns with s3v2 baseline: 0.78
