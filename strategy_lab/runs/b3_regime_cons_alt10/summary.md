# Run: b3_regime_cons_alt10

Strategy `regime_switch`; universe `{'type': 'list', 'assets': ['ZECUSDT', 'NEARUSDT', 'SUIUSDT', 'LTCUSDT', 'UNIUSDT', 'AAVEUSDT', 'TAOUSDT', 'ENAUSDT', 'HBARUSDT', 'TRXUSDT', 'BTCUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'no_trade': ['BTCUSDT'], 'n_divisor': 10, 'base_tv': 0.4}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | -14.96% | -2.41% | -0.01 | -0.01 | -38.67% | -0.06 | -0.02 |
| in_sample | 2020-02-15 → 2024-12-31 | -3.65% | -0.76% | 0.07 | 0.10 | -37.35% | -0.02 | 0.06 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -11.71% | -6.84% | -0.23 | -0.34 | -28.78% | -0.24 | -0.28 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +16.47% | +16.47% | 0.80 | 1.18 | -15.37% | 1.07 | 1.03 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.35% | 37% | -16.71% | -17.70% | -3.61 | 14 | 99% |
| out_of_sample | 628 | -0.74% | 30% | -11.17% | -12.39% | -4.54 | 14 | 100% |
| in_sample | 1768 | -0.28% | 39% | -16.71% | -17.70% | -2.99 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.237% | 51% | 2.60 | +47.96% |
| bull | 687 | 28% | -0.005% | 46% | -0.07 | -9.60% |
| bear | 400 | 17% | +0.028% | 44% | 0.79 | +10.97% |
| chop | 1160 | 48% | -0.044% | 44% | -0.98 | -42.70% |

## Turnover, fees, activity

- trades: 4988 (2.06/day); active days 100%
- turnover 59.5x equity/year; fees 5.95% of equity/year ($17,669 total)
- average gross exposure 0.16; brake active 15.3% of hours
- correlation of daily returns with s3v2 baseline: 0.43
