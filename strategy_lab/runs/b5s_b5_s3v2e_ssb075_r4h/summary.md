# Run: b5s_b5_s3v2e_ssb075_r4h

Strategy `s3v2x`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.75, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +234.23% | +19.93% | 1.27 | 1.92 | -15.68% | 1.27 | 1.53 |
| in_sample | 2020-02-15 → 2024-12-31 | +154.64% | +21.10% | 1.37 | 2.07 | -14.43% | 1.46 | 1.68 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +31.35% | +16.78% | 1.04 | 1.55 | -15.68% | 1.07 | 1.25 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +17.76% | +17.76% | 0.99 | 1.48 | -15.68% | 1.13 | 1.23 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.18% | 44% | -5.20% | -6.88% | -1.57 | 14 | 99% |
| out_of_sample | 628 | -0.43% | 38% | -4.79% | -6.54% | -2.77 | 14 | 100% |
| in_sample | 1768 | -0.12% | 46% | -5.20% | -6.88% | -1.13 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.314% | 53% | 4.15 | +70.52% |
| bull | 687 | 28% | +0.088% | 46% | 2.52 | +79.92% |
| bear | 400 | 17% | +0.067% | 42% | 1.78 | +29.32% |
| chop | 1160 | 48% | -0.009% | 39% | -0.21 | -13.74% |

## Turnover, fees, activity

- trades: 7269 (3.00/day); active days 100%
- turnover 70.2x equity/year; fees 7.02% of equity/year ($46,378 total)
- average gross exposure 0.17; brake active 11.3% of hours
- correlation of daily returns with s3v2 baseline: 0.78
