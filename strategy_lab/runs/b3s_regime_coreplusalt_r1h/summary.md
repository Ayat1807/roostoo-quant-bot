# Run: b3s_regime_coreplusalt_r1h

Strategy `regime_switch`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT', 'ZECUSDT', 'NEARUSDT', 'SUIUSDT', 'LTCUSDT', 'UNIUSDT', 'AAVEUSDT', 'TAOUSDT', 'ENAUSDT', 'HBARUSDT', 'TRXUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_divisor': 10, 'base_tv': 0.6}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +65.57% | +7.89% | 0.40 | 0.58 | -54.76% | 0.14 | 0.39 |
| in_sample | 2020-02-15 → 2024-12-31 | +61.74% | +10.35% | 0.47 | 0.68 | -54.76% | 0.19 | 0.47 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +2.37% | +1.34% | 0.19 | 0.27 | -32.70% | 0.04 | 0.18 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +17.39% | +17.39% | 0.71 | 1.04 | -21.23% | 0.82 | 0.87 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.98% | 39% | -16.18% | -18.85% | -3.14 | 14 | 98% |
| out_of_sample | 628 | -1.58% | 37% | -16.18% | -17.02% | -4.64 | 14 | 95% |
| in_sample | 1768 | -0.79% | 40% | -15.35% | -18.85% | -2.76 | 14 | 98% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.522% | 54% | 3.94 | +136.85% |
| bull | 687 | 28% | +0.082% | 43% | 0.75 | +51.83% |
| bear | 400 | 17% | +0.084% | 41% | 1.30 | +35.99% |
| chop | 1160 | 48% | -0.081% | 39% | -1.14 | -64.96% |

## Turnover, fees, activity

- trades: 20692 (8.54/day); active days 100%
- turnover 268.4x equity/year; fees 26.84% of equity/year ($138,344 total)
- average gross exposure 0.30; brake active 48.5% of hours
- correlation of daily returns with s3v2 baseline: 0.59
