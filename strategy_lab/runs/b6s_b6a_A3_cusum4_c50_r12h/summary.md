# Run: b6s_b6a_A3_cusum4_c50_r12h

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +207.04% | +18.41% | 1.33 | 1.99 | -12.42% | 1.48 | 1.64 |
| in_sample | 2020-02-15 → 2024-12-31 | +130.41% | +18.65% | 1.35 | 2.03 | -12.42% | 1.50 | 1.67 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +33.29% | +17.76% | 1.26 | 1.88 | -11.57% | 1.54 | 1.59 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +18.64% | +18.64% | 1.20 | 1.79 | -11.57% | 1.61 | 1.56 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.13% | 46% | -6.75% | -8.49% | -1.23 | 14 | 100% |
| out_of_sample | 628 | -0.26% | 43% | -5.55% | -6.01% | -1.74 | 14 | 100% |
| in_sample | 1768 | -0.09% | 47% | -6.75% | -8.49% | -0.85 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.295% | 58% | 4.30 | +65.51% |
| bull | 687 | 28% | +0.088% | 51% | 2.74 | +80.16% |
| bear | 400 | 17% | +0.045% | 47% | 1.45 | +18.93% |
| chop | 1160 | 48% | -0.008% | 42% | -0.19 | -11.36% |

## Turnover, fees, activity

- trades: 6503 (2.68/day); active days 100%
- turnover 50.9x equity/year; fees 5.09% of equity/year ($31,919 total)
- average gross exposure 0.16; brake active 5.9% of hours
- correlation of daily returns with s3v2 baseline: 0.79
