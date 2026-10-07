# Run: b6a_A3_bocpd08_c0

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +77.76% | +9.05% | 0.76 | 1.12 | -17.78% | 0.51 | 0.83 |
| in_sample | 2020-02-15 → 2024-12-31 | +42.75% | +7.56% | 0.66 | 0.99 | -17.78% | 0.43 | 0.72 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +24.66% | +13.36% | 1.01 | 1.47 | -11.45% | 1.17 | 1.24 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +12.77% | +12.77% | 0.89 | 1.31 | -11.45% | 1.11 | 1.12 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.22% | 43% | -6.83% | -8.16% | -2.16 | 14 | 100% |
| out_of_sample | 628 | -0.14% | 46% | -5.55% | -6.36% | -0.99 | 14 | 100% |
| in_sample | 1768 | -0.23% | 42% | -6.83% | -8.16% | -2.58 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.232% | 55% | 3.63 | +48.41% |
| bull | 687 | 28% | +0.058% | 52% | 2.01 | +46.97% |
| bear | 400 | 17% | +0.049% | 46% | 1.57 | +20.64% |
| chop | 1160 | 48% | -0.030% | 42% | -0.90 | -30.64% |

## Turnover, fees, activity

- trades: 5213 (2.15/day); active days 100%
- turnover 44.0x equity/year; fees 4.40% of equity/year ($18,676 total)
- average gross exposure 0.16; brake active 6.2% of hours
- correlation of daily returns with s3v2 baseline: 0.77
