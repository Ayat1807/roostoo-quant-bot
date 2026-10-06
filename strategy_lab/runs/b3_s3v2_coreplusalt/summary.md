# Run: b3_s3v2_coreplusalt

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT', 'ZECUSDT', 'NEARUSDT', 'SUIUSDT', 'LTCUSDT', 'UNIUSDT', 'AAVEUSDT', 'TAOUSDT', 'ENAUSDT', 'HBARUSDT', 'TRXUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_divisor': 10}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +96.57% | +10.71% | 0.71 | 1.01 | -22.27% | 0.48 | 0.76 |
| in_sample | 2020-02-15 → 2024-12-31 | +62.86% | +10.51% | 0.71 | 1.00 | -22.27% | 0.47 | 0.75 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +20.81% | +11.36% | 0.74 | 1.06 | -13.89% | 0.82 | 0.89 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +14.69% | +14.69% | 0.85 | 1.24 | -13.89% | 1.06 | 1.07 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.28% | 43% | -6.41% | -8.32% | -1.92 | 14 | 99% |
| out_of_sample | 628 | -0.26% | 44% | -4.94% | -6.35% | -1.24 | 14 | 100% |
| in_sample | 1768 | -0.27% | 42% | -6.41% | -8.32% | -2.00 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.238% | 50% | 2.95 | +48.99% |
| bull | 687 | 28% | +0.083% | 51% | 2.14 | +74.06% |
| bear | 400 | 17% | +0.042% | 46% | 1.16 | +17.34% |
| chop | 1160 | 48% | -0.035% | 45% | -0.92 | -35.13% |

## Turnover, fees, activity

- trades: 6091 (2.51/day); active days 100%
- turnover 53.8x equity/year; fees 5.38% of equity/year ($25,458 total)
- average gross exposure 0.23; brake active 14.1% of hours
- correlation of daily returns with s3v2 baseline: 0.80
