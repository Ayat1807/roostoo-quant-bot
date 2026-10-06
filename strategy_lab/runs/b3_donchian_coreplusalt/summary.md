# Run: b3_donchian_coreplusalt

Strategy `donchian_long`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT', 'ZECUSDT', 'NEARUSDT', 'SUIUSDT', 'LTCUSDT', 'UNIUSDT', 'AAVEUSDT', 'TAOUSDT', 'ENAUSDT', 'HBARUSDT', 'TRXUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_divisor': 10}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +186.15% | +17.16% | 1.18 | 1.57 | -17.62% | 0.97 | 1.27 |
| in_sample | 2020-02-15 → 2024-12-31 | +165.82% | +22.17% | 1.37 | 1.81 | -17.62% | 1.26 | 1.51 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +7.34% | +4.11% | 0.45 | 0.62 | -9.91% | 0.41 | 0.51 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +10.59% | +10.59% | 1.26 | 1.78 | -6.25% | 1.69 | 1.60 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.05% | 47% | -9.55% | -11.74% | -0.85 | 14 | 90% |
| out_of_sample | 628 | -0.07% | 44% | -6.92% | -7.25% | -1.59 | 14 | 94% |
| in_sample | 1768 | -0.04% | 48% | -9.55% | -11.74% | -0.58 | 14 | 88% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.061% | 50% | 0.77 | +9.14% |
| bull | 687 | 28% | +0.191% | 60% | 4.21 | +260.42% |
| bear | 400 | 17% | -0.034% | 41% | -1.95 | -13.05% |
| chop | 1160 | 48% | -0.014% | 49% | -0.54 | -16.33% |

## Turnover, fees, activity

- trades: 2801 (1.16/day); active days 98%
- turnover 3.9x equity/year; fees 0.39% of equity/year ($2,610 total)
- average gross exposure 0.13; brake active 2.4% of hours
- correlation of daily returns with s3v2 baseline: 0.21
