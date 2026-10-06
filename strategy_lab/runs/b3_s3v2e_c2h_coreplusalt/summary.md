# Run: b3_s3v2e_c2h_coreplusalt

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT', 'ZECUSDT', 'NEARUSDT', 'SUIUSDT', 'LTCUSDT', 'UNIUSDT', 'AAVEUSDT', 'TAOUSDT', 'ENAUSDT', 'HBARUSDT', 'TRXUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'n_divisor': 10, 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +119.27% | +12.55% | 0.87 | 1.24 | -16.78% | 0.75 | 0.98 |
| in_sample | 2020-02-15 → 2024-12-31 | +83.56% | +13.25% | 0.91 | 1.30 | -16.78% | 0.79 | 1.03 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +19.59% | +10.71% | 0.76 | 1.10 | -13.76% | 0.78 | 0.90 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +19.31% | +19.31% | 1.12 | 1.63 | -13.76% | 1.40 | 1.41 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.27% | 43% | -5.48% | -7.02% | -2.27 | 14 | 100% |
| out_of_sample | 628 | -0.36% | 42% | -5.48% | -7.00% | -2.24 | 14 | 100% |
| in_sample | 1768 | -0.24% | 43% | -5.31% | -7.02% | -2.24 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.242% | 54% | 3.14 | +50.30% |
| bull | 687 | 28% | +0.092% | 48% | 2.41 | +84.31% |
| bear | 400 | 17% | +0.049% | 48% | 1.38 | +20.50% |
| chop | 1160 | 48% | -0.034% | 45% | -1.02 | -34.05% |

## Turnover, fees, activity

- trades: 5713 (2.36/day); active days 100%
- turnover 50.0x equity/year; fees 5.00% of equity/year ($25,068 total)
- average gross exposure 0.22; brake active 10.4% of hours
- correlation of daily returns with s3v2 baseline: 0.84
