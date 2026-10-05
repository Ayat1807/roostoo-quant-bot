# Run: d_30m_r6h

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [48, 144, 336, 672], 'vol_win': 672, 'regime_win': 672, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'bars_per_year': 17520}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-06-30 | +287.16% | +23.64% | 1.40 | 2.10 | -17.22% | 1.37 | 1.67 |
| in_sample | 2020-02-15 → 2024-12-31 | +199.47% | +25.19% | 1.51 | 2.26 | -10.83% | 2.33 | 2.06 |
| out_of_sample | 2025-01-01 → 2026-06-30 | +29.37% | +18.79% | 1.08 | 1.62 | -17.22% | 1.09 | 1.30 |
| oos_12m_ref | 2025-10-01 → 2026-06-30 | +14.39% | +19.69% | 1.00 | 1.51 | -17.22% | 1.14 | 1.25 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2314 | -0.01% | 50% | -6.12% | -7.52% | -0.05 | 14 | 99% |
| out_of_sample | 532 | -0.37% | 42% | -6.12% | -6.28% | -2.64 | 14 | 100% |
| in_sample | 1768 | +0.06% | 52% | -6.03% | -7.52% | 0.74 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 170 | 7% | +0.313% | 59% | 4.17 | +67.14% |
| bull | 659 | 28% | +0.088% | 47% | 2.35 | +75.87% |
| bear | 399 | 17% | +0.074% | 45% | 1.76 | +32.82% |
| chop | 1099 | 47% | +0.005% | 41% | 0.11 | +1.51% |

## Turnover, fees, activity

- trades: 6371 (2.74/day); active days 100%
- turnover 61.6x equity/year; fees 6.16% of equity/year ($44,544 total)
- average gross exposure 0.18; brake active 13.4% of hours
- correlation of daily returns with s3v2 baseline: 0.85
