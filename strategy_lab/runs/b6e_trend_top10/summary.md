# Run: b6e_trend_top10

Strategy `s3v2x`; universe `{'type': 'satellite', 'rule': 'TREND', 'n_liquid': 10, 'min_history_days': 180, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False, 'always_include_btc': True}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +76.21% | +8.91% | 0.61 | 0.90 | -22.44% | 0.40 | 0.66 |
| in_sample | 2020-02-15 → 2024-12-31 | +63.87% | +10.65% | 0.68 | 1.00 | -22.44% | 0.47 | 0.74 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +7.64% | +4.28% | 0.38 | 0.56 | -12.76% | 0.34 | 0.44 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +16.67% | +16.67% | 1.09 | 1.61 | -12.76% | 1.31 | 1.36 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.32% | 44% | -7.22% | -8.74% | -2.01 | 14 | 91% |
| out_of_sample | 628 | -0.30% | 42% | -5.00% | -6.28% | -2.53 | 14 | 100% |
| in_sample | 1768 | -0.31% | 45% | -7.22% | -8.74% | -1.73 | 14 | 88% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.319% | 54% | 3.43 | +70.55% |
| bull | 687 | 28% | +0.059% | 51% | 1.48 | +47.10% |
| bear | 400 | 17% | +0.022% | 45% | 0.58 | +7.92% |
| chop | 1160 | 48% | -0.033% | 41% | -0.83 | -34.10% |

## Turnover, fees, activity

- trades: 4419 (1.82/day); active days 99%
- turnover 56.8x equity/year; fees 5.68% of equity/year ($25,389 total)
- average gross exposure 0.19; brake active 14.6% of hours
- correlation of daily returns with s3v2 baseline: 0.70
