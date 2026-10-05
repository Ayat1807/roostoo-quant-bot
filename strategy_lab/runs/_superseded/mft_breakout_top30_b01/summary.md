# Run: mft_breakout_top30_b01

Strategy `breakout`; universe `{'type': 'top_volume', 'n': 30, 'reselect': 'monthly', 'min_history_days': 60, 'min_quote_volume_usd': 5000000.0}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT'}`; band 0.01; brake True; shorts False; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-05 | -32.61% | -5.77% | -0.11 | -0.15 | -66.00% | -0.09 | -0.12 |
| in_sample | 2020-02-15 → 2024-12-31 | -8.85% | -1.88% | 0.06 | 0.08 | -52.53% | -0.04 | 0.04 |
| out_of_sample | 2025-01-01 → 2026-10-05 | -26.30% | -15.92% | -0.66 | -0.91 | -42.15% | -0.38 | -0.67 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -19.36% | -19.36% | -1.00 | -1.37 | -34.34% | -0.56 | -1.02 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2411 | -1.37% | 38% | -10.25% | -10.39% | -3.64 | 14 | 79% |
| out_of_sample | 629 | -1.99% | 32% | -8.07% | -10.00% | -4.72 | 14 | 89% |
| in_sample | 1768 | -1.05% | 41% | -10.25% | -10.39% | -2.61 | 14 | 76% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.593% | 48% | 4.92 | +170.65% |
| bull | 687 | 28% | +0.057% | 43% | 0.77 | +38.00% |
| bear | 400 | 17% | -0.220% | 30% | -4.05 | -59.37% |
| chop | 1160 | 48% | -0.065% | 33% | -1.20 | -55.52% |

## Turnover, fees, activity

- trades: 54061 (22.29/day); active days 97%
- turnover 148.6x equity/year; fees 14.86% of equity/year ($51,579 total)
- average gross exposure 0.22; brake active 52.9% of hours
- correlation of daily returns with s3v2 baseline: 0.25
