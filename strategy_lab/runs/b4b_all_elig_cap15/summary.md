# Run: b4b_all_elig_cap15

Strategy `xsmom_sz`; universe `{'type': 'satellite', 'rule': 'R1', 'n_liquid': 15, 'k': 5, 'min_history_days': 90, 'min_quote_volume_usd': 10000000.0, 'crash_guard': False, 'exclude_core': False}`; params `{'horizons': [24, 72, 168, 336], 'vol_win': 336, 'regime_win': 336, 'target_vol': 0.4, 'short_scale_bull': 0.5, 'max_w': 0.3, 'btc_pair': 'BTCUSDT', 'select': 'all_eligible', 'coin_cap': 0.15}`; band 0.06; brake True; shorts False; guard off

## Periods

| period | window | return | ann | Sharpe | Sortino | max DD | Calmar | composite |
|---|---|---|---|---|---|---|---|---|
| full | 2020-02-15 → 2026-10-04 | +87.45% | +9.92% | 0.45 | 0.60 | -71.58% | 0.14 | 0.42 |
| in_sample | 2020-02-15 → 2024-12-31 | +217.73% | +26.72% | 0.83 | 1.11 | -56.40% | 0.47 | 0.83 |
| out_of_sample | 2025-01-01 → 2026-10-04 | -41.21% | -26.08% | -0.99 | -1.34 | -56.02% | -0.47 | -0.97 |
| oos_12m_ref | 2025-10-01 → 2026-10-01 | -14.37% | -14.37% | -0.50 | -0.69 | -35.63% | -0.40 | -0.55 |

## Rolling 14-day windows (competition horizon)

| period | windows | median ret | % positive | worst ret | worst DD | median composite | median active days /14 | % windows 14/14 active |
|---|---|---|---|---|---|---|---|---|
| full | 2410 | -1.20% | 40% | -18.85% | -20.53% | -2.28 | 12 | 33% |
| out_of_sample | 628 | -2.70% | 32% | -11.70% | -13.19% | -5.19 | 12 | 21% |
| in_sample | 1768 | -0.84% | 42% | -18.85% | -20.53% | -1.67 | 12 | 37% |

## By BTC regime (daily returns, full period)

| regime | days | share | mean daily | hit rate | ann. Sharpe | cum. return |
|---|---|---|---|---|---|---|
| shock | 176 | 7% | +0.496% | 47% | 2.97 | +118.54% |
| bull | 687 | 28% | +0.254% | 50% | 2.45 | +398.96% |
| bear | 400 | 17% | -0.241% | 30% | -3.88 | -62.91% |
| chop | 1160 | 48% | -0.058% | 34% | -0.83 | -53.65% |

## Turnover, fees, activity

- trades: 21640 (8.93/day); active days 82%
- turnover 157.4x equity/year; fees 15.74% of equity/year ($143,495 total)
- average gross exposure 0.30; brake active 46.8% of hours
- correlation of daily returns with s3v2 baseline: 0.40
