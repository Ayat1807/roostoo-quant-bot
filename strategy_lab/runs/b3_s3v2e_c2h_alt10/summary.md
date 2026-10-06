# Run: b3_s3v2e_c2h_alt10

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['ZECUSDT', 'NEARUSDT', 'SUIUSDT', 'LTCUSDT', 'UNIUSDT', 'AAVEUSDT', 'TAOUSDT', 'ENAUSDT', 'HBARUSDT', 'TRXUSDT', 'BTCUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'no_trade': ['BTCUSDT'], 'n_divisor': 10, 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +24.56% | +3.36% | 0.42 | 0.61 | -13.95% | 0.24 | 0.44 |
| in_sample | 2020-02-15 → 2024-12-31 | +19.27% | +3.67% | 0.48 | 0.71 | -12.22% | 0.30 | 0.52 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +4.48% | +2.52% | 0.29 | 0.41 | -13.41% | 0.19 | 0.31 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +7.21% | +7.21% | 0.63 | 0.89 | -12.39% | 0.58 | 0.72 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.23% | 39% | -5.93% | -6.59% | -2.83 | 14 | 99% |
| out_of_sample | 628 | -0.30% | 38% | -5.93% | -6.59% | -3.03 | 14 | 100% |
| in_sample | 1768 | -0.19% | 40% | -4.54% | -4.99% | -2.64 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.113% | 51% | 1.99 | +20.78% |
| bull | 687 | 28% | +0.029% | 49% | 1.32 | +20.97% |
| bear | 400 | 17% | +0.003% | 45% | 0.19 | +1.08% |
| chop | 1160 | 48% | -0.014% | 44% | -0.71 | -15.66% |

## Turnover, fees, activity

- trades: 3736 (1.54/day); active days 100%
- turnover 25.6x equity/year; fees 2.56% of equity/year ($9,047 total)
- average gross exposure 0.11; brake active 2.1% of hours
- correlation of daily returns with s3v2 baseline: 0.61
