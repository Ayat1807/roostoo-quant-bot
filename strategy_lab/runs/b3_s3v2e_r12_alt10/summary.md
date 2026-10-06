# Run: b3_s3v2e_r12_alt10

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['ZECUSDT', 'NEARUSDT', 'SUIUSDT', 'LTCUSDT', 'UNIUSDT', 'AAVEUSDT', 'TAOUSDT', 'ENAUSDT', 'HBARUSDT', 'TRXUSDT', 'BTCUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'no_trade': ['BTCUSDT'], 'n_divisor': 10, 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +24.21% | +3.32% | 0.43 | 0.63 | -12.81% | 0.26 | 0.46 |
| in_sample | 2020-02-15 → 2024-12-31 | +24.25% | +4.55% | 0.58 | 0.87 | -10.90% | 0.42 | 0.65 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +0.00% | +0.00% | 0.05 | 0.07 | -11.70% | 0.00 | 0.04 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +1.83% | +1.83% | 0.22 | 0.32 | -9.93% | 0.18 | 0.25 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.21% | 40% | -4.04% | -5.60% | -2.89 | 14 | 99% |
| out_of_sample | 628 | -0.43% | 34% | -4.04% | -5.60% | -4.29 | 14 | 100% |
| in_sample | 1768 | -0.15% | 42% | -3.54% | -4.42% | -2.23 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.143% | 45% | 2.82 | +27.51% |
| bull | 687 | 28% | +0.026% | 45% | 1.21 | +19.20% |
| bear | 400 | 17% | +0.021% | 46% | 1.22 | +8.48% |
| chop | 1160 | 48% | -0.024% | 43% | -1.27 | -24.67% |

## Turnover, fees, activity

- trades: 4129 (1.70/day); active days 100%
- turnover 32.9x equity/year; fees 3.29% of equity/year ($12,015 total)
- average gross exposure 0.11; brake active 1.0% of hours
- correlation of daily returns with s3v2 baseline: 0.60
