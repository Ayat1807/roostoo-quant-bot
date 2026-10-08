# Run: b8_s_U3

Strategy `s3v2x`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 30, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False, 'always_include_btc': True}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'vol_method': 'ewma', 'ewma_halflife': 168, 'n_divisor': 10}`; band 0.06; brake True; shorts True; guard minimal

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +172.91% | +16.32% | 1.20 | 1.77 | -17.42% | 0.94 | 1.35 |
| in_sample | 2020-02-15 → 2024-12-31 | +119.38% | +17.46% | 1.22 | 1.81 | -17.42% | 1.00 | 1.39 |
| out_of_sample | 2025-01-01 → 2026-10-04 | +24.55% | +13.30% | 1.14 | 1.64 | -9.95% | 1.34 | 1.40 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | +20.23% | +20.23% | 1.43 | 2.04 | -9.95% | 2.03 | 1.86 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -0.15% | 46% | -5.66% | -6.49% | -1.51 | 14 | 99% |
| out_of_sample | 628 | -0.05% | 49% | -4.87% | -6.49% | -0.28 | 14 | 100% |
| in_sample | 1768 | -0.16% | 45% | -5.66% | -6.49% | -1.69 | 14 | 99% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.271% | 53% | 3.74 | +58.35% |
| bull | 687 | 28% | +0.094% | 51% | 2.69 | +88.41% |
| bear | 400 | 17% | +0.035% | 48% | 1.30 | +14.48% |
| chop | 1160 | 48% | -0.017% | 46% | -0.61 | -19.78% |

## Turnover, fees, activity

- trades: 5483 (2.26/day); active days 100%
- turnover 50.7x equity/year; fees 5.07% of equity/year ($27,381 total)
- average gross exposure 0.21; brake active 6.3% of hours
- correlation of daily returns with s3v2 baseline: 0.71
