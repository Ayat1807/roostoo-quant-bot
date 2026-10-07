# strategy_bot

The live trading bot for the Roostoo hackathon. It runs plug-in strategies (`strategies/`) on one Roostoo account, from one polling loop. Deployment and operation are covered in [DEPLOY.md](DEPLOY.md). Research and backtests live in [../strategy_lab](../strategy_lab).

## Current configuration (testing key, from 2026-10-06)

Two strategies run as sleeves of one account (`config.yaml`, `sleeves.py`), each on its own book:

| sleeve | weight | strategy | universe | trades |
|---|---|---|---|---|
| s3v2 | 0.5 | multi-horizon trend, EWMA vol (halflife 7 days), shorts allowed | 10 core coins | hourly band checks (6pp), new targets daily at 00:00 UTC |
| xsmom | 0.5 | teammate's 24h cross-sectional momentum, long only | ZEC PAXG POL ICP TRX LISTA STO CAKE TUT SOL | once a day, at the 14:00 UTC bar |

- **Account-wide rules:** the capital cap ($10,000), drawdown brake, KILL switch, minimal activity guard and liquidity guard apply to the whole account.
- **Netting:** orders are netted per coin, and every order records which sleeve caused it.

## Real-market robustness

The organisers noted that judges discount strategies that rely on queue-free simulator fills. How the bot and its backtests handle execution:

- **Backtests charge taker fees on every fill.** strategy_lab assumes 100% taker fills (0.10%) plus 2 bps slippage per fill, never maker rebates or queue priority. The live bot first rests a limit order at its side of the book (maker, 0.05%), then sends a market order for whatever hasn't filled after 5 minutes. Live fills therefore cost at most what the backtests assume.
- **Stress test:** 100% taker plus **5 bps extra slippage** per fill (7 bps total). The 14-day results barely change ([../strategy_lab/reports/robustness.md](../strategy_lab/reports/robustness.md)):

| config | costs | OOS P(14d >= +10%) | OOS P(14d <= -10%) | OOS worst 14d | meets constraints (both halves) |
|---|---|---|---|---|---|
| xsmom on tm10 (block-3 winner) | taker + 2 bps | 9% | 0% | -14.4% | yes |
| xsmom on tm10 | taker + 7 bps | 9% | 1% | -14.5% | yes |
| s3v2 + xsmom 50/50 (current config) | taker + 2 bps | 2% | 0% | -6.0% | yes |
| s3v2 + xsmom 50/50 | taker + 7 bps | 2% | 0% | -5.8% | yes |
| s3v2 EWMA alone | taker + 2 bps | 4% | 0% | -5.2% | yes |
| s3v2 EWMA alone | taker + 7 bps | 3% | 0% | -4.2% | yes |

  OOS is 2025-01 to 2026-06; P is over all rolling 14-day windows.

- **Low turnover:** about 2–4 trades a day and 4–9% of equity a year in fees. Strategies with high turnover (re-ranking every bar, 15–30 minute bars) were tested and rejected in strategy_lab, partly because of fees.
- **Liquidity guard:** at each decision the bot skips coins whose Roostoo spread is wider than 15 bps or whose 24h volume is under $1M. It never builds a position the real book couldn't absorb.
- **No dependence on fill timing:** a rested limit order that fills late is logged (`LIMIT_LATE_FILL`). The bot never resends an order after a timeout, and it re-reads the account before every decision.

## Optional: event_refresh (OFF in every shipped config)

A scheduled sleeve can make extra decisions on macro-event days. This is strategy_lab block 4a `b4e_fast_12h`. It passed the pre-registered adopt rule, but only by 1 window in-sample and 2 windows OOS (4 events), so treat the result as noise. Do not enable it without a team decision.

```yaml
sleeves:
  - name: xsmom
    ...
    event_refresh: {calendar: data/events.csv, every_h: 12, days_after: 2,
                    types: [CPI, FOMC_DECISION, FOMC_MINUTES]}
```

With `every_h: 12` the sleeve also decides at 03:00 UTC on the UTC date of each CPI release, FOMC decision or FOMC minutes and on the 2 days after. That decision uses the 02:00 UTC bar and trades fully, like the daily 15:00 decision. `data/events.csv` is a copy of `strategy_lab/data/events.csv`, built from the official BLS and Fed calendars by `python -m lab.events`. A missing calendar stops the bot at start. Tests: `python -m tests.test_event_refresh`.

## Tests

```bash
python -m tests.test_safety        # timeouts never resend, key-label gate, strategy contract
python -m tests.test_parity        # s3v2 == reference research code
python -m tests.test_parity_ewma   # s3v2 EWMA == strategy_lab e_ewma_vol
python -m tests.test_xsmom_parity  # xsmom == teammate's target_at_signal_time
python -m tests.test_restart       # mid-day restart keeps targets, late-fill logging
python -m tests.test_replay        # 30-day single-strategy replay incl. KILL
python -m tests.test_sleeves       # sleeves: migration, 30-day replay, parity, restart, xsmom-only
python -m tests.test_competition   # competition config: R1 parity, target parity, replay, restart
python -m tests.test_status        # status.py (display only) vs the mock account
python -m tests.test_event_refresh # optional event_refresh sleeve option
```
