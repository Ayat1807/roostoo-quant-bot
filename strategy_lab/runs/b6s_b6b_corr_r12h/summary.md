# Run: b6s_b6b_corr_r12h

Strategy `s3v2x_regime`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'corr_filter': True}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +207.26% | +18.42% | 1.26 | 1.88 | -14.73% | 1.25 | 1.50 |
| in_sample | 2020-02-15 → 2024-12-31 | +131.80% | +18.79% | 1.24 | 1.86 | -14.73% | 1.28 | 1.50 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +32.59% | +17.41% | 1.31 | 1.95 | -11.84% | 1.47 | 1.61 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +35.69% | +35.69% | 1.99 | 3.00 | -11.84% | 3.02 | 2.70 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.17% | 45% | -6.53% | -8.27% | -1.67 | 14 | 100% |
| out_of_sample | 628 | -0.24% | 41% | -4.29% | -5.94% | -2.56 | 14 | 100% |
| in_sample | 1768 | -0.13% | 47% | -6.53% | -8.27% | -1.24 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.290% | 55% | 3.84 | +63.66% |
| bull | 687 | 28% | +0.070% | 52% | 2.20 | +59.41% |
| bear | 400 | 17% | +0.070% | 49% | 2.05 | +31.11% |
| chop | 1160 | 48% | -0.004% | 42% | -0.11 | -7.98% |

## Turnover, fees, activity

- trades: 5359 (2.21/day); active days 100%
- turnover 44.2x equity/year; fees 4.42% of equity/year ($28,039 total)
- average gross exposure 0.16; brake active 8.8% of hours
- correlation of daily returns with s3v2 baseline: 0.78
