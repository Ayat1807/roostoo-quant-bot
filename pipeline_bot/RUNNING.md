# Running the pipeline bot

This is a toy strategy for testing the infrastructure: hold LONG $300 of BTC when the price is above its 24h SMA, otherwise stay FLAT. All commands run from `Trading_Competition/pipeline_bot/`.

> **Keys:** `pipeline_bot/.env` (copy `.env.example`, `chmod 600` on Linux). Use the **testing** key only. The bot refuses to start with any other label. `competition` additionally needs `allow_competition: true` in `config.yaml` and shows a 10 s warning before starting.
>
> **Dry run is the default** (`dry_run: true` in `config.yaml`). It decides and logs, but never sends orders. Real orders need `--live` or `dry_run: false`.

## 1. Local run

```bash
# setup (Windows: py -3 -m venv .venv ; .\.venv\Scripts\Activate.ps1)
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env            # then edit it

python bot.py                                          # config.yaml as-is (dry run, 15 min)
python bot.py --interval-min 1 --max-cycles 3          # quick dry-run smoke test
python bot.py --live --interval-min 1 --force-flip-every 5 --max-cycles 20
                                                       # TEST MODE: real orders, LONG/FLAT every 5 min
python status.py                                       # health check (no API calls)
```

| Flag | Meaning |
|---|---|
| `--live` / `--dry-run` | override `dry_run` from config |
| `--interval-min N` | override the cycle interval |
| `--force-flip-every N` | test mode: alternate LONG/FLAT every N minutes, ignoring the SMA |
| `--max-cycles N` | exit cleanly after N cycles |
| `--config PATH` | use another config file |

Stop with **Ctrl+C** (or SIGTERM). The bot finishes the current cycle, writes `status: stopped` to the heartbeat, and exits. Press Ctrl+C a second time to stop immediately.

## 2. EC2 setup (Amazon Linux 2023, Session Manager)

Short version below. The full step-by-step guide (deploy key, reboot test, updates) is in [DEPLOY_AWS.md](DEPLOY_AWS.md).

```bash
# connect: AWS console -> EC2 -> instance -> Connect -> Session Manager, then:
sudo su - ec2-user
git clone <repo-url> Trading_Competition
cd Trading_Competition/pipeline_bot
bash deploy/setup_ec2.sh        # idempotent: python3.11, git, tmux, venv, pinned deps
nano .env                       # paste the TESTING key pair; label=testing
```

## 3. Run inside tmux

```bash
tmux new -s bot                                  # new session called "bot"
cd ~/Trading_Competition/pipeline_bot && source .venv/bin/activate
python bot.py --live                             # or edit config.yaml: dry_run: false
# detach (leave running):   Ctrl+B, then D
tmux ls                                          # list sessions
tmux attach -t bot                               # reattach
# inside tmux: Ctrl+C stops the bot gracefully; `exit` closes the session
```

Session Manager sessions time out, but tmux keeps the bot running after you disconnect.

## 4. Run as a systemd service (alternative to tmux)

This restarts automatically after a crash or a reboot.

```bash
sudo cp deploy/pipeline-bot.service /etc/systemd/system/
# For real orders, set dry_run: false in config.yaml (the unit runs plain `python bot.py`).
sudo systemctl daemon-reload
sudo systemctl enable --now pipeline-bot      # start now + on boot
systemctl status pipeline-bot
journalctl -u pipeline-bot -f                 # live console output
sudo systemctl stop pipeline-bot              # graceful (SIGTERM, up to 120 s)
sudo systemctl disable pipeline-bot           # stop starting on boot
```

Use tmux **or** systemd, never both. Two bots on the same key would fight over the position.

## 5. Tail logs

```bash
python status.py                         # summary: heartbeat age, equity, last decisions/orders, errors
tail -f logs/bot.log                     # human-readable (rotates at 5 MB, 5 backups)
tail -f logs/decisions.jsonl             # price, sma, current, target, action
tail -f logs/orders.jsonl                # each order request + full response
tail -f logs/equity.jsonl                # per-cycle USD / coin / short / total equity
tail -f logs/errors.jsonl                # exceptions with tracebacks
tail -f logs/api_log.jsonl               # every raw API call (key masked)
cat state/heartbeat.json
```

Windows equivalent: `Get-Content logs\bot.log -Wait -Tail 20`.

## 6. Kill switch

```bash
touch KILL        # Windows: New-Item KILL
```

On its next cycle the bot **closes any position** (sells BTC, closes any short) and then idles. It keeps cycling, logging equity and updating the heartbeat, but places no trades. Decisions show `IDLE (KILL)`.

```bash
rm KILL           # resume normal trading on the next cycle
```

The kill switch survives restarts: a KILL file present at startup also means flatten and idle. To stop the process itself, use Ctrl+C or `systemctl stop`.

## 7. Restart after a code update

```bash
cd ~/Trading_Competition && git pull
cd pipeline_bot && .venv/bin/pip install -r requirements.txt   # if requirements changed
# tmux:    tmux attach -t bot, Ctrl+C, wait for "stopped cleanly", then start again
# systemd: sudo systemctl restart pipeline-bot
python status.py                                               # confirm a fresh heartbeat
```

On every start the bot re-syncs the clock, re-checks exchangeInfo, and re-reads balances and positions from the exchange. It never assumes the previous position, so restarting is always safe.

## Files

| Path | What |
|---|---|
| `bot.py` | main loop, strategy, execution, logging |
| `roostoo_client.py` | API client (copied from initial_testing, with configurable key-label guard) |
| `status.py` | read-only health check |
| `config.yaml` | settings |
| `state/heartbeat.json`, `state/prices.json` | heartbeat; hourly price history (survives restarts) |
| `logs/*.jsonl`, `logs/bot.log` | logs (git-ignored) |
| `deploy/setup_ec2.sh`, `deploy/pipeline-bot.service` | AWS setup |
