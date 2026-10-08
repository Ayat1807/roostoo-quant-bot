# Run: b8s_b8_h_U6_r12h

Strategy `s3v2x_regime`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'regime_hmm': 2, 'floor_breadth': 7, 'floor_gross': 0.5}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +131.33% | +13.46% | 0.79 | 1.15 | -25.82% | 0.52 | 0.85 |
| in_sample | 2020-02-15 → 2024-12-31 | +107.08% | +16.08% | 0.89 | 1.30 | -25.82% | 0.62 | 0.98 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +12.28% | +6.81% | 0.48 | 0.70 | -16.34% | 0.42 | 0.55 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +4.67% | +4.67% | 0.35 | 0.52 | -16.34% | 0.29 | 0.40 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.37% | 45% | -7.54% | -8.10% | -1.59 | 14 | 100% |
| out_of_sample | 628 | -0.48% | 42% | -6.20% | -6.36% | -2.22 | 14 | 100% |
| in_sample | 1768 | -0.30% | 47% | -7.54% | -8.10% | -1.10 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.490% | 54% | 5.40 | +130.29% |
| bull | 687 | 28% | +0.076% | 48% | 1.69 | +64.34% |
| bear | 400 | 17% | +0.001% | 46% | 0.02 | -1.01% |
| chop | 1160 | 48% | -0.035% | 41% | -0.71 | -36.78% |

## Turnover, fees, activity

- trades: 9137 (3.77/day); active days 100%
- turnover 76.9x equity/year; fees 7.69% of equity/year ($46,927 total)
- average gross exposure 0.22; brake active 22.6% of hours
- correlation of daily returns with s3v2 baseline: 0.80
