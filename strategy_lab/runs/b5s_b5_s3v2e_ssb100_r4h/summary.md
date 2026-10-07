# Run: b5s_b5_s3v2e_ssb100_r4h

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 1.0, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +182.32% | +16.92% | 1.10 | 1.65 | -16.27% | 1.04 | 1.30 |
| in_sample | 2020-02-15 → 2024-12-31 | +115.07% | +16.98% | 1.13 | 1.70 | -15.58% | 1.09 | 1.35 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +31.36% | +16.79% | 1.04 | 1.55 | -16.27% | 1.03 | 1.24 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +19.96% | +19.96% | 1.09 | 1.63 | -16.27% | 1.23 | 1.35 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.20% | 44% | -6.83% | -7.20% | -1.85 | 14 | 99% |
| out_of_sample | 628 | -0.55% | 39% | -4.81% | -6.56% | -2.95 | 14 | 100% |
| in_sample | 1768 | -0.13% | 46% | -6.83% | -7.20% | -1.29 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.312% | 51% | 4.12 | +70.02% |
| bull | 687 | 28% | +0.073% | 46% | 2.14 | +63.00% |
| bear | 400 | 17% | +0.073% | 43% | 1.94 | +32.70% |
| chop | 1160 | 48% | -0.017% | 38% | -0.39 | -21.39% |

## Turnover, fees, activity

- trades: 7684 (3.17/day); active days 100%
- turnover 75.2x equity/year; fees 7.52% of equity/year ($44,870 total)
- average gross exposure 0.18; brake active 11.3% of hours
- correlation of daily returns with s3v2 baseline: 0.77
