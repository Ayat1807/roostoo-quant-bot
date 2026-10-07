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

- Block 4c COMPLETE (291-343): NOT ADOPTED. Final candidate b4c_B_c4_w05_m125 (4h checks, w 0.5, m 1.25) fails IS
  P(>=10%) (12% vs live 15%), ties OOS (9%); 0 of 7 neighbours beat live. leaderboard_b4c_lsx.md,
  reports/stats_card_b4c_B_c4_w05_m125.md (vs live and stage A winner). Every frequency-sweep run worse.
- `04b8018` strategy_bot: event_refresh option (off) + test fixes; all bot suites pass.
- hourly lows downloaded (.cache/klines_hl, 65 coins).

- 2026-10-07 NEW TEAM OBJECTIVE (risk-adjusted composite + down markets): block 5 pre-registered `88b5606`
  (variants_b5_shorts.yaml, 394-408; judging in lab/b5.py). References re-run with positions (lab/b5_refs.py, b5ref__*).
- Block 4d runs 344-348 done (report not yet written; to be judged under the NEW objective too).

## Running
- block 5: `.cache/b5_run.log` (394-401), `.cache/b5_refs.log`.

## Next (in order)
1. Block 5: `python -m lab.b5 --resolve-f` -> commit -> `python -m lab.runner variants_b5_shorts.yaml --group F`;
   `--resolve-sweep` -> commit -> `--group sweep`; `python -m lab.b5` -> leaderboard_b5.md; stats cards
   (`python -m lab.stats_card <run> b3_s3v2e_core10 b3_xsmom_r1`) for finalists. If adopted: strategy_bot flags + tests +
   testing config (cap 10000, own paths) + EC2 commands; no competition config.
2. Block 4d: `python -m lab.b4gen 4d` (old objective) + `python -m lab.b5 <4d runs>` (new objective); sweep resolution.
3. Block 4b: run, report under both objectives.
