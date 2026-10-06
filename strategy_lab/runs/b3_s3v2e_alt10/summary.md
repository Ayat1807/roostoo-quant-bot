# Run: b3_s3v2e_alt10

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['ZECUSDT', 'NEARUSDT', 'SUIUSDT', 'LTCUSDT', 'UNIUSDT', 'AAVEUSDT', 'TAOUSDT', 'ENAUSDT', 'HBARUSDT', 'TRXUSDT', 'BTCUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'no_trade': ['BTCUSDT'], 'n_divisor': 10, 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +24.59% | +3.37% | 0.42 | 0.61 | -13.89% | 0.24 | 0.44 |
| in_sample | 2020-02-15 → 2024-12-31 | +19.05% | +3.64% | 0.48 | 0.70 | -12.26% | 0.30 | 0.51 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +4.70% | +2.65% | 0.31 | 0.43 | -13.35% | 0.20 | 0.32 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +7.44% | +7.44% | 0.65 | 0.92 | -12.33% | 0.60 | 0.75 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.23% | 40% | -5.92% | -6.57% | -2.83 | 14 | 99% |
| out_of_sample | 628 | -0.30% | 38% | -5.92% | -6.57% | -3.03 | 14 | 100% |
| in_sample | 1768 | -0.19% | 40% | -4.54% | -4.99% | -2.64 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.114% | 51% | 2.01 | +20.99% |
| bull | 687 | 28% | +0.029% | 49% | 1.31 | +20.92% |
| bear | 400 | 17% | +0.003% | 45% | 0.17 | +0.95% |
| chop | 1160 | 48% | -0.014% | 44% | -0.71 | -15.64% |

## Turnover, fees, activity

- trades: 3737 (1.54/day); active days 100%
- turnover 25.6x equity/year; fees 2.56% of equity/year ($9,030 total)
- average gross exposure 0.11; brake active 2.2% of hours
- correlation of daily returns with s3v2 baseline: 0.61
