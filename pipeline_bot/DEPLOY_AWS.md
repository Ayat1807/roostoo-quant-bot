# Deploying the pipeline bot to AWS EC2

This setup uses Amazon Linux 2023 in **ap-southeast-2**, with access through **Session Manager only** (no SSH, no open inbound ports). The code comes from the private repo `Ayat1807/roostoo-quant-bot`, cloned with a read-only deploy key.
For day-to-day commands (logs, kill switch, flags), see [RUNNING.md](RUNNING.md).

> ⚠️ **Run the bot with tmux OR systemd, never both.** Two bot processes on the same key would each read the position and trade against each other, and could double the exposure. Before starting one, check that the other is not running (section 9).
>
> ⚠️ **Testing key only** until the team decides otherwise. The bot refuses `competition` unless `allow_competition: true` is set in `config.yaml`. Never make manual API calls with the competition key.

---

## 0. Instance prerequisites (once, in the AWS console)

- **AMI:** Amazon Linux 2023. A small instance (t3.micro / t3.small) is enough.
- **Security group:** no inbound rules are needed. Outbound HTTPS (443) must be allowed.
- **IAM instance profile** with the `AmazonSSMManagedInstanceCore` policy, so Session Manager works.
- **Network:** a public subnet with a public IP, or a NAT. The bot needs outbound access to `mock-api.roostoo.com`, `api.binance.com` / `data-api.binance.vision` and `github.com`.

## 1. Connect

AWS console → EC2 → select the instance → **Connect** → **Session Manager** → **Connect**.

Session Manager logs you in as `ssm-user`. Switch to `ec2-user` so files, the venv and the service all belong to the same user:

```bash
sudo su - ec2-user
whoami          # ec2-user
cd ~
```

## 2. Clone with a read-only GitHub deploy key

On the instance:

```bash
ssh-keygen -t ed25519 -C "ec2-roostoo-bot" -f ~/.ssh/roostoo_deploy -N ""
cat ~/.ssh/roostoo_deploy.pub          # copy this single line
```

On GitHub, open the repo → **Settings** → **Deploy keys** → **Add deploy key**. Give it the title `ec2-ap-southeast-2`, paste the public key, and **leave "Allow write access" unticked**.

Back on the instance:

```bash
cat >> ~/.ssh/config <<'EOF'
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/roostoo_deploy
    IdentitiesOnly yes
EOF
chmod 600 ~/.ssh/config ~/.ssh/roostoo_deploy

sudo dnf -y install git                      # setup_ec2.sh also installs it
ssh -T git@github.com                        # answer "yes"; expect "...successfully authenticated..."
git clone git@github.com:Ayat1807/roostoo-quant-bot.git ~/Trading_Competition
cd ~/Trading_Competition/pipeline_bot
```

The repo must be cloned to `/home/ec2-user/Trading_Competition`, because the systemd unit uses that path.

## 3. Install (idempotent)

```bash
bash ~/Trading_Competition/pipeline_bot/deploy/setup_ec2.sh
```

This installs git, tmux and python3.11 (Amazon Linux 2023's default `python3` is 3.9, which is too old). It also enables chrony time sync, creates `.venv`, installs the pinned `requirements.txt`, and creates `logs/`, `state/` and `.env` (copied from the example, `chmod 600`). It is safe to re-run.

## 4. Create `.env` on the server

```bash
cd ~/Trading_Competition/pipeline_bot
nano .env
```

```
ROOSTOO_API_KEY=<testing key>
ROOSTOO_API_SECRET=<testing secret>
ROOSTOO_KEY_LABEL=testing
```

Save the file (Ctrl+O, Enter, Ctrl+X), then lock it down and check it:

```bash
chmod 600 .env
ls -l .env                 # -rw------- 1 ec2-user ec2-user ...
git status --short         # .env must NOT appear (it is git-ignored)
```

Never paste keys into chat, tickets or the repo. Type or paste them only in this file on the server.

## 5. Foreground dry run (first check)

```bash
cd ~/Trading_Competition/pipeline_bot
source .venv/bin/activate
python bot.py --dry-run --interval-min 1 --max-cycles 3
python status.py
```

Expect three things:
- `clock offset ... ms` and `seeded 48 hourly closes`
- `reconciled position`
- 3 cycles with `[DRY RUN] would ...` or `HOLD`, and `Errors in last 24h: 0` from `status.py`

If Binance seeding fails with HTTP 451, the region is blocked. The bot falls back to `data-api.binance.vision` automatically; check that the log says which host it used.

Optionally, run a short live test (real orders on the testing key, about 20 minutes):

```bash
python bot.py --live --interval-min 1 --force-flip-every 5 --max-cycles 20
```

## 6. Unattended run with tmux

```bash
tmux new -s bot
cd ~/Trading_Competition/pipeline_bot && source .venv/bin/activate
python bot.py --live          # or set dry_run: false in config.yaml and run: python bot.py
```

- Detach with **Ctrl+B**, then **D**. The bot keeps running after the Session Manager session ends.
- Reattach later with `sudo su - ec2-user` and then `tmux attach -t bot`.
- Stop it with Ctrl+C inside tmux. The bot finishes its cycle and exits.

tmux does **not** survive a reboot. For that, use systemd (next section) instead.

## 7. systemd install + reboot test

First make sure no tmux bot is running (section 9). Then:

```bash
cd ~/Trading_Competition/pipeline_bot
# The unit runs plain `python bot.py`, so the mode comes from config.yaml:
nano config.yaml               # dry_run: false  (when you want real orders)

sudo cp deploy/pipeline-bot.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now pipeline-bot
systemctl status pipeline-bot            # active (running)
journalctl -u pipeline-bot -n 30         # startup lines
python status.py                         # heartbeat age < 1 interval
```

**Reboot test:**

```bash
sudo reboot
# wait 1-2 minutes, reconnect via Session Manager, then:
sudo su - ec2-user
systemctl status pipeline-bot            # active (running), recent start time
cd ~/Trading_Competition/pipeline_bot && python3.11 status.py
journalctl -u pipeline-bot -b            # logs since this boot: startup + reconcile
```

**Crash-restart test (optional):**

```bash
sudo kill -9 $(systemctl show -p MainPID --value pipeline-bot)
sleep 40; systemctl status pipeline-bot  # restarted (RestartSec=30)
```

## 8. Updating (git pull + restart)

```bash
sudo su - ec2-user
cd ~/Trading_Competition && git pull
cd pipeline_bot && .venv/bin/pip install -r requirements.txt     # only if requirements changed
```

Then restart whichever runner you use:

```bash
# systemd
sudo systemctl restart pipeline-bot      # graceful stop (SIGTERM), then start
# tmux
tmux attach -t bot   # Ctrl+C, wait for "stopped cleanly", then run the start command again
```

After the restart, check it:

```bash
python3.11 status.py                     # fresh heartbeat, 0 new errors
git log -1 --oneline                     # the commit that is now running
```

On every start the bot re-reads the position from the exchange, so restarting is always safe. If you changed `deploy/pipeline-bot.service`, copy it again and run `sudo systemctl daemon-reload` before restarting.

## 9. Stopping, and checking what is running

```bash
# what is running?
systemctl is-active pipeline-bot         # active / inactive
tmux ls                                  # lists a "bot" session if tmux is in use
pgrep -af "bot.py"                       # should show at most ONE process

# stop
sudo systemctl stop pipeline-bot         # systemd (graceful, up to 120 s)
sudo systemctl disable pipeline-bot      # also stop starting on boot
tmux attach -t bot  then Ctrl+C          # tmux
```

To flatten the position but keep the process running (and the heartbeat alive), use the kill switch: `touch ~/Trading_Competition/pipeline_bot/KILL`. Remove the file with `rm` to resume trading.

## 10. Switching between tmux and systemd

- **tmux → systemd:** stop the tmux bot (Ctrl+C), run `tmux kill-session -t bot`, check that `pgrep -af bot.py` shows nothing, then `sudo systemctl enable --now pipeline-bot`.
- **systemd → tmux:** run `sudo systemctl disable --now pipeline-bot`, check that `pgrep -af bot.py` shows nothing, then start tmux.

**Never run both at the same time.**
