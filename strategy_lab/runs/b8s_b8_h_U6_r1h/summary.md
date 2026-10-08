# Run: b8s_b8_h_U6_r1h

Strategy `s3v2x_regime`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'regime_hmm': 2, 'floor_breadth': 7, 'floor_gross': 0.5}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +117.60% | +12.42% | 0.65 | 0.94 | -25.74% | 0.48 | 0.71 |
| in_sample | 2020-02-15 → 2024-12-31 | +104.05% | +15.73% | 0.77 | 1.11 | -25.74% | 0.61 | 0.86 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +6.64% | +3.73% | 0.28 | 0.42 | -19.25% | 0.19 | 0.31 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +5.14% | +5.14% | 0.35 | 0.52 | -17.51% | 0.29 | 0.40 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.71% | 41% | -14.69% | -17.24% | -2.61 | 14 | 99% |
| out_of_sample | 628 | -1.04% | 36% | -5.62% | -6.30% | -3.57 | 14 | 100% |
| in_sample | 1768 | -0.50% | 44% | -14.69% | -17.24% | -1.89 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.523% | 51% | 4.53 | +140.22% |
| bull | 687 | 28% | +0.072% | 46% | 1.37 | +58.66% |
| bear | 400 | 17% | +0.016% | 41% | 0.28 | +4.17% |
| chop | 1160 | 48% | -0.044% | 37% | -0.78 | -43.64% |

## Turnover, fees, activity

- trades: 15906 (6.56/day); active days 100%
- turnover 161.0x equity/year; fees 16.10% of equity/year ($90,101 total)
- average gross exposure 0.23; brake active 38.7% of hours
- correlation of daily returns with s3v2 baseline: 0.79
