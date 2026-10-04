# Run: p_brake_off

Strategy `s3v2`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.06; brake False; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +219.78% | +19.13% | 1.11 | 1.62 | -18.17% | 1.05 | 1.29 |
| in_sample | 2020-02-15 → 2024-12-31 | +132.38% | +18.85% | 1.12 | 1.64 | -17.47% | 1.08 | 1.31 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +37.75% | +19.99% | 1.09 | 1.57 | -18.17% | 1.10 | 1.29 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +18.15% | +18.15% | 0.93 | 1.35 | -18.17% | 1.00 | 1.12 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.13% | 47% | -9.65% | -10.37% | -0.93 | 14 | 100% |
| out_of_sample | 628 | -0.17% | 46% | -9.65% | -10.37% | -1.03 | 14 | 100% |
| in_sample | 1768 | -0.12% | 47% | -6.76% | -8.30% | -0.77 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.275% | 57% | 3.36 | +58.85% |
| bull | 687 | 28% | +0.104% | 53% | 2.77 | +100.69% |
| bear | 400 | 17% | +0.033% | 46% | 0.78 | +12.45% |
| chop | 1160 | 48% | -0.004% | 44% | -0.08 | -8.17% |

## Turnover, fees, activity

- trades: 5423 (2.24/day); active days 100%
- turnover 48.0x equity/year; fees 4.80% of equity/year ($29,834 total)
- average gross exposure 0.21; brake active 0.0% of hours
- correlation of daily returns with s3v2 baseline: 0.88
