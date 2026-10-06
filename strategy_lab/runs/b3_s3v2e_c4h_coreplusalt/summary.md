# Run: b3_s3v2e_c4h_coreplusalt

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT', 'ZECUSDT', 'NEARUSDT', 'SUIUSDT', 'LTCUSDT', 'UNIUSDT', 'AAVEUSDT', 'TAOUSDT', 'ENAUSDT', 'HBARUSDT', 'TRXUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_divisor': 10, 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +119.13% | +12.54% | 0.86 | 1.23 | -18.13% | 0.69 | 0.96 |
| in_sample | 2020-02-15 → 2024-12-31 | +81.04% | +12.93% | 0.88 | 1.26 | -18.13% | 0.71 | 0.98 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +21.18% | +11.55% | 0.81 | 1.17 | -13.15% | 0.88 | 0.97 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +20.68% | +20.68% | 1.18 | 1.72 | -13.15% | 1.57 | 1.52 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.27% | 43% | -5.83% | -7.45% | -2.27 | 14 | 100% |
| out_of_sample | 628 | -0.36% | 42% | -5.10% | -7.07% | -2.23 | 14 | 100% |
| in_sample | 1768 | -0.24% | 43% | -5.83% | -7.45% | -2.24 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.244% | 54% | 3.16 | +50.78% |
| bull | 687 | 28% | +0.090% | 49% | 2.35 | +82.35% |
| bear | 400 | 17% | +0.049% | 48% | 1.38 | +20.47% |
| chop | 1160 | 48% | -0.033% | 45% | -0.98 | -33.58% |

## Turnover, fees, activity

- trades: 5720 (2.36/day); active days 100%
- turnover 49.9x equity/year; fees 4.99% of equity/year ($24,769 total)
- average gross exposure 0.22; brake active 10.0% of hours
- correlation of daily returns with s3v2 baseline: 0.84
