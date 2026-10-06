# Run: b3s_regime_coreplusalt_r12h

Strategy `regime_switch`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT', 'ZECUSDT', 'NEARUSDT', 'SUIUSDT', 'LTCUSDT', 'UNIUSDT', 'AAVEUSDT', 'TAOUSDT', 'ENAUSDT', 'HBARUSDT', 'TRXUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_divisor': 10, 'base_tv': 0.6}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +265.97% | +21.58% | 0.78 | 1.13 | -41.18% | 0.52 | 0.84 |
| in_sample | 2020-02-15 → 2024-12-31 | +281.00% | +31.52% | 1.00 | 1.45 | -38.48% | 0.82 | 1.12 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -3.94% | -2.26% | 0.05 | 0.07 | -25.43% | -0.09 | 0.02 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +6.15% | +6.15% | 0.36 | 0.52 | -25.43% | 0.24 | 0.39 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.56% | 44% | -16.95% | -19.25% | -1.89 | 14 | 98% |
| out_of_sample | 628 | -0.99% | 40% | -13.69% | -15.35% | -3.08 | 14 | 100% |
| in_sample | 1768 | -0.35% | 46% | -16.95% | -19.25% | -1.29 | 14 | 97% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.624% | 55% | 4.48 | +181.58% |
| bull | 687 | 28% | +0.079% | 47% | 0.78 | +51.65% |
| bear | 400 | 17% | +0.058% | 44% | 0.88 | +22.22% |
| chop | 1160 | 48% | -0.017% | 43% | -0.22 | -27.31% |

## Turnover, fees, activity

- trades: 11493 (4.74/day); active days 100%
- turnover 145.3x equity/year; fees 14.53% of equity/year ($152,015 total)
- average gross exposure 0.35; brake active 40.5% of hours
- correlation of daily returns with s3v2 baseline: 0.61
