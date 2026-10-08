# Run: b7s_b7_hmm2_erc_r2h

Strategy `s3v2x_regime`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'regime_hmm': 2, 'inner': 's3v2x_alloc', 'alloc': 'erc'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +92.45% | +10.36% | 0.69 | 1.05 | -19.73% | 0.53 | 0.78 |
| in_sample | 2020-02-15 → 2024-12-31 | +82.98% | +13.17% | 0.83 | 1.28 | -14.00% | 0.94 | 1.05 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +5.25% | +2.96% | 0.26 | 0.39 | -19.73% | 0.15 | 0.28 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +5.65% | +5.65% | 0.40 | 0.59 | -19.73% | 0.29 | 0.44 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.30% | 42% | -8.28% | -8.39% | -2.38 | 14 | 99% |
| out_of_sample | 628 | -0.55% | 39% | -8.28% | -8.39% | -3.22 | 14 | 100% |
| in_sample | 1768 | -0.22% | 43% | -4.79% | -6.65% | -2.00 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.326% | 53% | 4.35 | +74.19% |
| bull | 687 | 28% | +0.021% | 42% | 0.57 | +13.56% |
| bear | 400 | 17% | +0.065% | 42% | 1.46 | +27.85% |
| chop | 1160 | 48% | -0.018% | 36% | -0.39 | -22.43% |

## Turnover, fees, activity

- trades: 11686 (4.82/day); active days 100%
- turnover 123.4x equity/year; fees 12.34% of equity/year ($66,705 total)
- average gross exposure 0.17; brake active 16.6% of hours
- correlation of daily returns with s3v2 baseline: 0.71
