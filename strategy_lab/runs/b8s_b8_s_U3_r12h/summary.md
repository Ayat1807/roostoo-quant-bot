# Run: b8s_b8_s_U3_r12h

Strategy `s3v2x`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 30, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False, 'always_include_btc': True}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'n_divisor': 10}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +180.37% | +16.80% | 1.20 | 1.78 | -13.93% | 1.21 | 1.44 |
| in_sample | 2020-02-15 → 2024-12-31 | +159.17% | +21.54% | 1.41 | 2.10 | -13.93% | 1.55 | 1.73 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +8.21% | +4.59% | 0.47 | 0.68 | -11.79% | 0.39 | 0.53 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +14.13% | +14.13% | 1.12 | 1.64 | -11.79% | 1.20 | 1.35 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.15% | 46% | -5.16% | -6.12% | -1.16 | 14 | 98% |
| out_of_sample | 628 | -0.31% | 43% | -4.81% | -5.32% | -2.46 | 14 | 100% |
| in_sample | 1768 | -0.09% | 48% | -5.16% | -6.12% | -0.76 | 14 | 98% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.335% | 56% | 4.72 | +77.24% |
| bull | 687 | 28% | +0.093% | 48% | 2.58 | +86.56% |
| bear | 400 | 17% | +0.042% | 46% | 1.52 | +17.71% |
| chop | 1160 | 48% | -0.027% | 42% | -0.90 | -27.90% |

## Turnover, fees, activity

- trades: 6538 (2.70/day); active days 100%
- turnover 65.7x equity/year; fees 6.57% of equity/year ($40,524 total)
- average gross exposure 0.20; brake active 7.0% of hours
- correlation of daily returns with s3v2 baseline: 0.69
