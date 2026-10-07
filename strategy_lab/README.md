# strategy_lab: compare strategies fairly

This is an offline research harness. It never touches the live bot or any API key. Every strategy runs through the **same data, costs and execution rules as the live `strategy_bot`** and gets the **same scorecard**. All variants are **declared up front** with a trial counter, so the leaderboard can flag results that are probably luck.

- Results: [leaderboard.md](leaderboard.md)
- Recommendation: [reports/recommendation.md](reports/recommendation.md)
- Analog report: [reports/analogs_2026-10-04.md](reports/analogs_2026-10-04.md)
- Per-coin trends: [reports/trend_capture.md](reports/trend_capture.md)

## Setup (once)

```bash
cd strategy_lab
python -m venv .venv && .venv/Scripts/activate      # Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python -m lab.data update        # ~10 min: all Binance USDT pairs since 2020 into .cache/ (git-ignored)
python -m lab.roostoo            # refresh data/roostoo_pairs.json (public endpoints, no key)
python -m tests.test_reproduce   # must say PASS (needs ../_reference, see below)
```

## Add a strategy in 5 minutes

1. **Copy the example:** `cp strategies/example_ma_trend.py strategies/my_idea.py`.
2. **Edit it:** rename the class, set `name = "my_idea"`, and write `target_weights(self, closes, cfg)`.
   - `closes`: hourly closes, oldest first, columns like `BTCUSDT`. The data already ends at the decision time, so there is no look-ahead.
   - `cfg`: your `params` from the run config.
   - **return** `{asset: signed weight}`. Negative means short, and `sum(|w|) <= 1`. Call `self.check(w)` to validate it.
   - `raise ValueError` if there isn't enough history yet; the backtester stays flat.
3. **Declare the run** in `variants.yaml`. Give it a new `trial` number and bump `declared_trials`:
   ```yaml
   - {name: my_idea_v1, trial: 27, group: new, strategy: my_idea, activity_guard: minimal,
      params: {ma_hours: 168}}
   ```
4. **Run, then rebuild the leaderboard:**
   ```bash
   python -m lab.runner variants.yaml --only my_idea_v1
   python -m lab.leaderboard
   python -m tests.test_strategies       # your strategy must return valid weights
   ```
5. **Read `runs/my_idea_v1/summary.md`.** Then check the flags in `leaderboard.md` before believing anything.

The strategy is discovered automatically; no registration is needed in the lab. To trade it live, copy the file into `strategy_bot/strategies/`, register it in that `__init__.py`, and set `strategy.name` in strategy_bot's config.

## What a run is

`variants.yaml` holds the `defaults` plus one entry per run. The main keys:

| key | meaning |
|---|---|
| `strategy`, `params` | strategy name and its parameters |
| `universe` | `{type: list, assets: [...]}`, `{type: roostoo_all}`, or `{type: top_volume, n, reselect: monthly, min_history_days, min_quote_volume_usd, rank_pool: all\|roostoo, trade: all\|roostoo}` |
| `band`, `activity_guard` (`off\|full\|minimal\|band_edge`), `brake`, `allow_short`, `capital_cap_usd` | the live bot's rules |
| `bar` (`1h\|30m`), `rebalance_every_h` | bar size and target cadence. For 30m runs, first download the data with `python -m lab.data update --interval 30m --symbols ...`. Results are resampled to hourly before scoring. |
| `start` / `end` | the backtest window; the strategy sees 800 bars of history before `start` |

## How it works

| module | role |
|---|---|
| `lab/data.py` | Binance monthly zips (data.binance.vision), 1h (all pairs) and 30m (on request), delisted coins included, plus a REST tail. Handles microsecond timestamps from 2025 and splits reused tickers (LUNA → LUNA~2). |
| `lab/roostoo.py` | Roostoo's crypto list, precisions and MiniOrder |
| `lab/universe.py` | point-in-time universes; 68 Binance tokenized stocks excluded |
| `lab/strategies.py` | loads the **live** `strategy_bot/strategies` package and `strategy_lab/strategies/*.py` |
| `lab/backtest.py` | hourly simulation: daily targets, the 6pp band, per-leg books, drawdown brake, activity guard, capital cap; Roostoo costs (taker 0.10% / maker 0.05% / shorts 0.10%, 2 bps slippage, $1 MiniOrder, AmountPrecision rounding) |
| `lab/scorecard.py` | full / in-sample (2020–24) / OOS (2025–26); all rolling 14-day windows; composite 0.4·Sortino + 0.3·Sharpe + 0.3·Calmar; BTC regimes (config/lab.yaml); turnover, fees, activity; correlation with s3v2 |
| `lab/analogs.py` | 8 market-state features; 30 nearest past dates; next-14-day results per run |
| `lab/trend_capture.py` | per-coin single-asset trend vs hold, and whether it persists |
| `lab/leaderboard.py` | ranks by OOS 14-day windows; flags with Deflated Sharpe, noise-vs-baseline, OOS≫IS, failed daily activity |

## Tests

```bash
python -m tests.test_reproduce    # backtester == reference research engine (0.1pp), s3v2 OOS +20.5%
python -m tests.test_strategies   # every strategy returns valid weights; s3v2x == s3v2
```

`test_reproduce` imports the reference prototype's research code from `../_reference/roostoo-bot/research`. That folder is git-ignored; unzip `roostoo-bot.zip` there.

## Honesty rules

- **Frequency sweep (standing rule, from block 3):** every strategy that becomes a candidate is also run with its target refresh at 1h, 2h, 4h, 6h, 12h and daily.
- **Stats card (required, from block 4):** no config is marked "competition" without a committed stats card (`python -m lab.stats_card <run> ...`, `reports/stats_card_<run>.md`): IS / OOS / Jul-Oct, Sharpe, Sortino, Calmar, composite (whole period and median 14d), drawdown, P(14d) metrics, fees, activity, the stress result and the luck threshold. Every recommended variant gets one.
  - Signal horizons stay fixed in calendar time; only `rebalance_every_h` changes, anchored at the strategy's own clock (`rebalance_hour_utc`).
  - Report them side by side: fees/yr, trades/day, P(14d ≥ +10%) and P(14d ≤ −10%), per half.
  - Declare the sweep runs as trials before running them (see `variants_b3_addendum.yaml`, `lab/b3_sweep.py`).
- **Real-market robustness:** the final recommended config is also reported with 100% taker fills and +5 bps extra slippage per fill. The judges discount strategies that rely on queue-free simulator fills.

- Declare a variant in `variants.yaml` **before** running it, and never delete a declared run because it looked bad.
- A result is evidence only if it beats its baseline in **both** in-sample and OOS, by more than about one standard error of Sharpe.
- Look at the 14-day windows, not just total return. The competition is scored on one 14-day window.
