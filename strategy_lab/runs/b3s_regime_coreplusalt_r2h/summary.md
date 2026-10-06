# Run: b3s_regime_coreplusalt_r2h

Strategy `regime_switch`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT', 'ZECUSDT', 'NEARUSDT', 'SUIUSDT', 'LTCUSDT', 'UNIUSDT', 'AAVEUSDT', 'TAOUSDT', 'ENAUSDT', 'HBARUSDT', 'TRXUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_divisor': 10, 'base_tv': 0.6}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +71.10% | +8.42% | 0.42 | 0.60 | -60.03% | 0.14 | 0.41 |
| in_sample | 2020-02-15 → 2024-12-31 | +63.31% | +10.57% | 0.47 | 0.68 | -60.03% | 0.18 | 0.47 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +5.08% | +2.86% | 0.24 | 0.35 | -24.49% | 0.12 | 0.25 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +3.26% | +3.26% | 0.25 | 0.37 | -22.40% | 0.15 | 0.27 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.03% | 40% | -16.69% | -19.14% | -3.04 | 14 | 96% |
| out_of_sample | 628 | -1.11% | 42% | -14.45% | -15.68% | -3.22 | 14 | 93% |
| in_sample | 1768 | -0.98% | 39% | -16.69% | -19.14% | -2.96 | 14 | 98% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.521% | 51% | 3.87 | +136.16% |
| bull | 687 | 28% | +0.103% | 47% | 0.97 | +76.69% |
| bear | 400 | 17% | +0.026% | 37% | 0.43 | +8.10% |
| chop | 1160 | 48% | -0.071% | 38% | -0.99 | -60.74% |

## Turnover, fees, activity

- trades: 17780 (7.33/day); active days 100%
- turnover 220.5x equity/year; fees 22.05% of equity/year ($117,046 total)
- average gross exposure 0.32; brake active 45.9% of hours
- correlation of daily returns with s3v2 baseline: 0.58
