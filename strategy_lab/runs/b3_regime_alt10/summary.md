# Run: b3_regime_alt10

Strategy `regime_switch`; universe `{'type': 'list', 'assets': ['ZECUSDT', 'NEARUSDT', 'SUIUSDT', 'LTCUSDT', 'UNIUSDT', 'AAVEUSDT', 'TAOUSDT', 'ENAUSDT', 'HBARUSDT', 'TRXUSDT', 'BTCUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'no_trade': ['BTCUSDT'], 'n_divisor': 10, 'base_tv': 0.6}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +8.06% | +1.17% | 0.17 | 0.24 | -36.45% | 0.03 | 0.16 |
| in_sample | 2020-02-15 → 2024-12-31 | -3.93% | -0.82% | 0.09 | 0.12 | -35.02% | -0.02 | 0.07 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +12.52% | +6.94% | 0.40 | 0.56 | -24.04% | 0.29 | 0.43 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +38.24% | +38.24% | 1.41 | 2.06 | -13.12% | 2.91 | 2.12 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.54% | 40% | -17.50% | -18.61% | -2.65 | 14 | 99% |
| out_of_sample | 628 | -0.78% | 39% | -11.28% | -12.50% | -2.65 | 14 | 98% |
| in_sample | 1768 | -0.45% | 40% | -17.50% | -18.61% | -2.50 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.226% | 49% | 2.29 | +44.36% |
| bull | 687 | 28% | +0.023% | 46% | 0.30 | +8.75% |
| bear | 400 | 17% | +0.032% | 48% | 0.82 | +12.56% |
| chop | 1160 | 48% | -0.036% | 44% | -0.65 | -38.51% |

## Turnover, fees, activity

- trades: 6144 (2.53/day); active days 100%
- turnover 78.3x equity/year; fees 7.83% of equity/year ($24,086 total)
- average gross exposure 0.24; brake active 21.6% of hours
- correlation of daily returns with s3v2 baseline: 0.51
