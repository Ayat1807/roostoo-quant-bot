# Run: b8_s_U4

Strategy `s3v2x`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 20, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False, 'always_include_btc': True}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'n_divisor': None}`; band 0.04; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +66.12% | +7.94% | 0.80 | 1.16 | -21.76% | 0.37 | 0.81 |
| in_sample | 2020-02-15 → 2024-12-31 | +47.41% | +8.27% | 0.77 | 1.11 | -21.76% | 0.38 | 0.79 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +12.75% | +7.07% | 1.05 | 1.51 | -6.21% | 1.14 | 1.26 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +11.35% | +11.35% | 1.36 | 1.97 | -6.21% | 1.83 | 1.75 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.12% | 43% | -6.99% | -9.11% | -1.78 | 14 | 99% |
| out_of_sample | 628 | -0.07% | 46% | -3.69% | -4.65% | -1.16 | 14 | 100% |
| in_sample | 1768 | -0.13% | 43% | -6.99% | -9.11% | -1.85 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.172% | 52% | 3.37 | +34.14% |
| bull | 687 | 28% | +0.046% | 52% | 1.81 | +36.34% |
| bear | 400 | 17% | +0.023% | 47% | 1.48 | +9.35% |
| chop | 1160 | 48% | -0.013% | 43% | -0.46 | -15.88% |

## Turnover, fees, activity

- trades: 4915 (2.03/day); active days 100%
- turnover 27.3x equity/year; fees 2.73% of equity/year ($11,669 total)
- average gross exposure 0.12; brake active 3.2% of hours
- correlation of daily returns with s3v2 baseline: 0.74
