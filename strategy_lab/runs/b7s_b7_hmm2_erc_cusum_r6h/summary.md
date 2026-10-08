# Run: b7s_b7_hmm2_erc_cusum_r6h

Strategy `s3v2x_regime`; universe `{'type': 'list', 'assets': ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'AVAXUSDT', 'LINKUSDT', 'DOTUSDT']}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'regime_hmm': 2, 'inner': 's3v2x_alloc', 'alloc': 'erc'}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +111.65% | +11.95% | 0.86 | 1.29 | -17.24% | 0.69 | 0.98 |
| in_sample | 2020-02-15 → 2024-12-31 | +96.40% | +14.83% | 1.02 | 1.55 | -11.67% | 1.27 | 1.31 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +7.89% | +4.42% | 0.39 | 0.57 | -17.24% | 0.26 | 0.42 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +3.22% | +3.22% | 0.28 | 0.42 | -17.24% | 0.19 | 0.31 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.17% | 45% | -5.31% | -6.39% | -1.43 | 14 | 100% |
| out_of_sample | 628 | -0.35% | 42% | -4.98% | -5.35% | -2.01 | 14 | 100% |
| in_sample | 1768 | -0.11% | 47% | -5.31% | -6.39% | -1.02 | 14 | 100% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.321% | 59% | 4.75 | +73.31% |
| bull | 687 | 28% | +0.044% | 46% | 1.31 | +33.27% |
| bear | 400 | 17% | +0.029% | 44% | 0.77 | +11.05% |
| chop | 1160 | 48% | -0.011% | 39% | -0.26 | -15.24% |

## Turnover, fees, activity

- trades: 8987 (3.71/day); active days 100%
- turnover 82.1x equity/year; fees 8.21% of equity/year ($45,487 total)
- average gross exposure 0.16; brake active 10.6% of hours
- correlation of daily returns with s3v2 baseline: 0.73
