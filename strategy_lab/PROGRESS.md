# strategy_lab progress (resume here)

Live competition bot: xsmom on R1, `config_competition.yaml`, commit a379740, live on EC2 since 2026-10-06 15:30 UTC.
Never touch it. All work here is offline or for the testing bot.

Rules: pre-register every trial (variants file + commit) before running; judge on data to 2026-06-30 in both halves
(IS 2020-02-15 to 2024-12-31, OOS 2025-01-01 to 2026-06-30; Jul-Oct 2026 informational only); primary P(14d >= +10%) and
P(>= +8%); constraints P(14d <= -10%) <= 10% and worst 14d >= -20%; frequency sweep for the best 2 of each block; every
recommended variant gets a stats card (`python -m lab.stats_card <run> [others]`). Global declared trials: 393.

## Done
- `adf9dd5` strategy_bot: sleeve-aware status.py (display only).
- Block 4a (events + exits + sweep, trials 268-290): leaderboard_b4_events.md, leaderboard_b4_exits.md. Event rule
  mechanically adopted b4e_fast_12h (margin 1 window IS / 2 OOS, 4 events = noise); no exit adopted; every faster refresh worse.
- `8d2d044` stats cards: lab/stats_card.py, reports/stats_card_xsmom_r1.md (+ s3v2e_core10, xsmom_tm10),
  stats_card_xsmom_tm10_liq.md; competition configs need `stats_card:` (strategy_bot/tests/test_safety.py).
- `e646b79` block 4c pre-registered per team spec (variants_b4c_lsx.yaml, 291-343; earlier draft superseded before any run,
  reports/superseded/). Stage A (291-299) done: every long/short variant far worse than live (OOS -49% to -63% vs -32%).
  Stage A winner (rule) = b4c_A1_minpos. Stage B (300-326) resolved.
- `d3eb3a1` blocks 4d (entry timing, 344-358) and 4b (sizing/exposure/coins, 359-393) pre-registered.

## Running (started 2026-10-07 ~07:00 UTC; slow machine, ~2-8 min per run)
- block 4c stage B: `.cache/b4c_B1.log` (2h-check runs), `.cache/b4c_B2.log` (4h/6h). Ledger repaired after a parallel race.
- `python -m lab.lows` (hourly lows for patient_limit, .cache/klines_hl/), log .cache/lows.log.

## Next (in order)
1. Block 4c: `python -m lab.b4c --resolve-c` -> commit -> run group C; `--resolve-sweep` -> commit -> run group sweep;
   `python -m lab.b4c` (report, leaderboard_b4c_lsx.md); stats card final candidate + control. Implement in strategy_bot ONLY
   if the adopt rule incl. the plateau test passes (config_testing_xsmom_ls.yaml, testing key, cap 10000).
2. strategy_bot (uncommitted): event_refresh sleeve option (bot.py, sleeves.py, data/events.csv, README,
   tests/test_event_refresh.py PASS) + test fixes for the new partial day of data (tests/test_replay.py, tests/test_sleeves.py:
   same failures on HEAD, data artifacts). Re-run test_replay, test_sleeves, test_competition, then commit.
3. Block 4d: run b4d__control (b3_xsmom_r1 with record_positions, not a trial) + 344-348; `python -m lab.b4gen 4d`.
4. Block 4b: run 359-371, 376-383; `python -m lab.b4gen 4b --resolve-best-sizing`; run 372-375; sweep; report.
