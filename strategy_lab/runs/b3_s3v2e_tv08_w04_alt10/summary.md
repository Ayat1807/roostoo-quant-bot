# Run: b3_s3v2e_tv08_w04_alt10

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['ZECUSDT', 'NEARUSDT', 'SUIUSDT', 'LTCUSDT', 'UNIUSDT', 'AAVEUSDT', 'TAOUSDT', 'ENAUSDT', 'HBARUSDT', 'TRXUSDT', 'BTCUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.8, 'short_scale_bull': 0.5, 'max_w': 0.4, 'btc_pair': 'BTCUSDT', 'no_trade': ['BTCUSDT'], 'n_divisor': 10, 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +58.09% | +7.14% | 0.41 | 0.58 | -32.51% | 0.22 | 0.42 |
| in_sample | 2020-02-15 → 2024-12-31 | +61.09% | +10.26% | 0.54 | 0.78 | -31.85% | 0.32 | 0.57 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -1.22% | -0.69% | 0.10 | 0.14 | -32.51% | -0.02 | 0.08 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +29.04% | +29.04% | 1.15 | 1.64 | -18.69% | 1.55 | 1.47 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.53% | 43% | -12.78% | -16.30% | -1.93 | 14 | 100% |
| out_of_sample | 628 | -0.83% | 42% | -12.78% | -16.30% | -1.99 | 14 | 100% |
| in_sample | 1768 | -0.42% | 44% | -9.06% | -14.50% | -1.77 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.172% | 47% | 1.51 | +29.88% |
| bull | 687 | 28% | +0.085% | 50% | 1.43 | +71.97% |
| bear | 400 | 17% | +0.050% | 48% | 0.81 | +18.81% |
| chop | 1160 | 48% | -0.038% | 45% | -0.69 | -39.53% |

## Turnover, fees, activity

- trades: 7182 (2.96/day); active days 100%
- turnover 81.2x equity/year; fees 8.12% of equity/year ($33,056 total)
- average gross exposure 0.28; brake active 32.9% of hours
- correlation of daily returns with s3v2 baseline: 0.60
