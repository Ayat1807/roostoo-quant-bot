# Public-readiness checklist (repo Ayat1807/roostoo-quant-bot)

_Checked 2026-10-08 over the full git history: 79 commits, all branches, 1,717 distinct paths ever committed. Nothing was changed in history._

## Secrets: clean
| check | result |
|---|---|
| `.env*` files ever committed | only the 4 templates (`initial_testing/`, `pipeline_bot/`, `strategy_bot/.env.example`, `strategy_bot/.env.competition.example`); every version holds placeholders (`your_..._here`) |
| the real testing key / secret values (from the local `.env` files) in any file version or commit message | 0 occurrences (searched literally, values never printed) |
| competition key | never stored on this machine; it lives only in `.env.competition` on EC2 (git-ignored) |
| key / secret / token / password assignments, AWS / GitHub / Slack token formats, private-key blocks | none (after excluding the template placeholders) |
| long random strings (40+ characters) | only `initial_testing/test_signature.py`: `DOC_SECRET` / `DOC_SIGNATURE`, the public example values from the official Roostoo API documentation, used as a signing test vector. Not a credential |

## Never committed (confirmed over the full history)
`logs*/`, `state*/`, `KILL*`, `.venv/`, `strategy_lab/.cache/` (price caches, hourly curves), `_reference/`, `roostoo-bot.zip`, `*.pkl`, `api_log`, `heartbeat`, `orders` / `equity` logs. All of them are git-ignored now (checked with `git check-ignore`), including the new `logs_testing_hmm/`, `state_testing_hmm/` and `KILL_testing_hmm`.

## Committed data (public market data, fine to publish)
- `strategy_lab/data/`: the Roostoo pair list, the event calendar (BLS / Fed), regime probabilities, meta-label predictions.
- `strategy_lab/runs/`: per-run results and daily equity curves.
- `teammate_xsmom/final_momentum_backtest.csv`: a backtest output.

## Decisions for the team before making the repo public
1. **Author email:** every commit's author email is the owner's personal Gmail address, so it becomes public with the history. To hide it, GitHub's noreply address would have to be set and the history rewritten. **Not done.** It needs your decision, and rewriting history affects every clone.
2. **Teammate's code:** `teammate_xsmom/` (3 files) is a teammate's work. Get their OK, or credit them in the README (it is credited as "a teammate's cross-sectional momentum strategy").
3. **`initial_testing/test_signature.py` test vector:** it is public documentation material. Keep it, or replace it with a self-generated test vector if you prefer no secret-looking strings at all.

## README coverage
The root `README.md` (new) covers the live strategy, strategy history, research summary (520 trials, what was rejected), real-market robustness, and how to run the lab and the bot.
- **Operation:** `strategy_bot/DEPLOY.md` (sections 12–14).
- **Research detail:** `strategy_lab/README.md` and `strategy_lab/reports/block6_summary.md`.
