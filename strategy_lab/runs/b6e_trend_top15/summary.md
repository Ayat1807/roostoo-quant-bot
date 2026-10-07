# Run: b6e_trend_top15

Strategy `s3v2x`; universe `{'type': 'satellite', 'rule': 'TREND', 'n_liquid': 15, 'min_history_days': 180, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False, 'always_include_btc': True}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +78.08% | +9.08% | 0.62 | 0.91 | -22.44% | 0.40 | 0.67 |
| in_sample | 2020-02-15 → 2024-12-31 | +65.23% | +10.83% | 0.69 | 1.02 | -22.44% | 0.48 | 0.76 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +7.83% | +4.38% | 0.40 | 0.58 | -12.76% | 0.34 | 0.45 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +17.69% | +17.69% | 1.16 | 1.71 | -12.76% | 1.39 | 1.45 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.32% | 43% | -7.22% | -8.74% | -2.35 | 14 | 91% |
| out_of_sample | 628 | -0.33% | 39% | -5.00% | -6.28% | -3.47 | 14 | 100% |
| in_sample | 1768 | -0.31% | 45% | -7.22% | -8.74% | -1.79 | 14 | 88% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.329% | 53% | 3.55 | +73.53% |
| bull | 687 | 28% | +0.057% | 50% | 1.44 | +44.87% |
| bear | 400 | 17% | +0.019% | 44% | 0.52 | +6.98% |
| chop | 1160 | 48% | -0.032% | 40% | -0.80 | -32.95% |

## Turnover, fees, activity

- trades: 4383 (1.81/day); active days 99%
- turnover 55.7x equity/year; fees 5.57% of equity/year ($24,848 total)
- average gross exposure 0.19; brake active 14.6% of hours
- correlation of daily returns with s3v2 baseline: 0.69
