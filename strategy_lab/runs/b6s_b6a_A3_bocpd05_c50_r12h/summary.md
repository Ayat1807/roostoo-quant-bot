# Run: b6s_b6a_A3_bocpd05_c50_r12h

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +191.00% | +17.45% | 1.30 | 1.94 | -12.18% | 1.43 | 1.60 |
| in_sample | 2020-02-15 → 2024-12-31 | +119.62% | +17.49% | 1.31 | 1.96 | -12.18% | 1.44 | 1.61 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +32.53% | +17.38% | 1.26 | 1.89 | -11.72% | 1.48 | 1.58 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +20.27% | +20.27% | 1.32 | 1.97 | -11.72% | 1.73 | 1.70 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.15% | 46% | -6.57% | -8.17% | -1.33 | 14 | 100% |
| out_of_sample | 628 | -0.21% | 46% | -5.58% | -6.04% | -1.30 | 14 | 100% |
| in_sample | 1768 | -0.14% | 47% | -6.57% | -8.17% | -1.30 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.277% | 57% | 4.09 | +60.49% |
| bull | 687 | 28% | +0.088% | 52% | 2.83 | +81.14% |
| bear | 400 | 17% | +0.051% | 47% | 1.63 | +21.69% |
| chop | 1160 | 48% | -0.012% | 42% | -0.34 | -15.79% |

## Turnover, fees, activity

- trades: 6433 (2.65/day); active days 100%
- turnover 51.4x equity/year; fees 5.14% of equity/year ($31,014 total)
- average gross exposure 0.16; brake active 5.1% of hours
- correlation of daily returns with s3v2 baseline: 0.78
