# strategy_lab progress (resume here)

Live competition bot: xsmom on R1, `config_competition.yaml`, commit a379740, live on EC2 since
2026-10-06 15:30 UTC. Never touch it. All work here is offline or for the testing bot.

Rules: pre-register every trial (variants file + commit) before running; judge on data to 2026-06-30 in both
halves (IS 2020-02-15 to 2024-12-31, OOS 2025-01-01 to 2026-06-30; Jul-Oct 2026 informational only);
primary P(14d >= +10%) and P(>= +8%); constraints P(14d <= -10%) <= 10% and worst 14d >= -20%;
frequency sweep for the best 2 of each block; every recommended variant gets a stats card.

## Done
- 2026-10-06 `adf9dd5` strategy_bot: sleeve-aware status.py (display only), tests/test_status.py.
- 2026-10-07 `0c20aa8` block 4a pre-registered: data/events.csv (lab/events.py), event overlays in
  lab/backtest.py, variants_b4_events.yaml (trials 268-276).
- 2026-10-07 block 4a event runs finished (9 runs), leaderboard_b4_events.md (lab/b4e.py).
  The rule mechanically adopts b4e_fast_12h, but the margin is 1 window IS (171 vs 170 of 1139) and 2 windows OOS
  (30 vs 28 of 344, 4 events): FEW EVENTS, noise. derisk_50 fails IS by 1 window.

- 2026-10-07 `82f6d83` block 4a event results committed. `8d2d044` STEP 1: lab/stats_card.py, reports/stats_card_xsmom_r1.md
  (+ s3v2e_core10, xsmom_tm10 side by side), stats_card_xsmom_tm10_liq.md; competition configs carry `stats_card:`,
  enforced by strategy_bot/tests/test_safety.py. Stress curves cached as .cache/runs/<name>__stress.pkl.

## Running
- nothing

## Next
2. STEP 2 rest: intraday exits (trend_break_exit, stop_loss_exit 4%/6%, trailing_exit 5%) pre-registered as a
   block 4a addendum, run, report; then decide on implementing the adopted event variant behind a flag.
3. STEP 3 long/short + hysteresis; STEP 4 entry timing; STEP 5 xsmom_sz (strategies/xsmom_sz.py written,
   untested, not yet pre-registered).
