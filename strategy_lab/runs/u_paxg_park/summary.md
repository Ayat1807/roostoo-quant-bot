# Run: u_paxg_park

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT', 'PAXGUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'parking_asset': 'PAXGUSDT'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +154.73% | +15.12% | 0.80 | 1.15 | -30.45% | 0.50 | 0.85 |
| in_sample | 2020-02-15 → 2024-12-31 | +46.45% | +8.13% | 0.49 | 0.71 | -30.45% | 0.27 | 0.51 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +74.08% | +37.08% | 1.63 | 2.30 | -27.69% | 1.34 | 1.81 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +11.83% | +11.83% | 0.62 | 0.87 | -27.69% | 0.43 | 0.66 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | +0.10% | 52% | -12.14% | -12.66% | 0.50 | 14 | 91% |
| out_of_sample | 628 | +0.69% | 60% | -12.14% | -12.66% | 3.60 | 14 | 86% |
| in_sample | 1768 | -0.13% | 49% | -9.14% | -12.27% | -0.40 | 14 | 93% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.282% | 59% | 3.58 | +60.98% |
| bull | 687 | 28% | +0.076% | 53% | 1.78 | +65.02% |
| bear | 400 | 17% | -0.006% | 46% | -0.12 | -4.00% |
| chop | 1160 | 48% | +0.007% | 47% | 0.14 | +2.84% |

## Turnover, fees, activity

- trades: 6392 (2.64/day); active days 99%
- turnover 110.7x equity/year; fees 11.07% of equity/year ($52,964 total)
- average gross exposure 0.71; brake active 24.5% of hours
- correlation of daily returns with s3v2 baseline: 0.67
