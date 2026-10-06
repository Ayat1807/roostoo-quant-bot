# Run: b3_s3v2e_tranched_alt10

Strategy `s3v2_tranched`; universe `{'type': 'list', 'assets': ['ZECUSDT', 'NEARUSDT', 'SUIUSDT', 'LTCUSDT', 'UNIUSDT', 'AAVEUSDT', 'TAOUSDT', 'ENAUSDT', 'HBARUSDT', 'TRXUSDT', 'BTCUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'no_trade': ['BTCUSDT'], 'n_divisor': 10, 'vol_method': 'ewma', 'ewma_halflife': 168, 'tranches': 4, 'spacing_bars': 6}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +31.91% | +4.26% | 0.50 | 0.71 | -13.35% | 0.32 | 0.53 |
| in_sample | 2020-02-15 → 2024-12-31 | +34.88% | +6.32% | 0.71 | 1.01 | -9.65% | 0.65 | 0.81 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -2.08% | -1.19% | -0.08 | -0.11 | -12.98% | -0.09 | -0.10 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +3.85% | +3.85% | 0.41 | 0.58 | -10.34% | 0.37 | 0.47 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.22% | 41% | -4.30% | -4.71% | -2.07 | 14 | 100% |
| out_of_sample | 628 | -0.41% | 35% | -4.30% | -4.71% | -4.01 | 14 | 100% |
| in_sample | 1768 | -0.15% | 44% | -4.08% | -4.59% | -1.57 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.116% | 53% | 2.09 | +21.37% |
| bull | 687 | 28% | +0.055% | 54% | 2.19 | +44.87% |
| bear | 400 | 17% | +0.004% | 48% | 0.23 | +1.44% |
| chop | 1160 | 48% | -0.025% | 44% | -1.34 | -26.04% |

## Turnover, fees, activity

- trades: 3875 (1.60/day); active days 100%
- turnover 19.4x equity/year; fees 1.94% of equity/year ($7,428 total)
- average gross exposure 0.13; brake active 0.9% of hours
- correlation of daily returns with s3v2 baseline: 0.60
