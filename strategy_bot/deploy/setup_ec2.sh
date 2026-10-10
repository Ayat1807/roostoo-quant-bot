#!/usr/bin/env bash
# One-time (idempotent) setup of strategy_bot on Amazon Linux 2023 (ap-southeast-2).
# Safe to re-run: dnf skips installed packages, the venv is reused, pip is pinned.
#
# Usage (as ec2-user, from anywhere inside the cloned repo):
#   bash strategy_bot/deploy/setup_ec2.sh
set -euo pipefail

BOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PY=python3.11   # AL2023's default python3 is 3.9; we need 3.10+

echo "==> Bot directory: ${BOT_DIR}"

echo "==> System packages"
sudo dnf -y update
sudo dnf -y install git tmux "${PY}" "${PY}-pip"

echo "==> Timezone stays UTC; ensure time sync (chrony) is running"
sudo systemctl enable --now chronyd || true

echo "==> Virtual environment"
if [ ! -x "${BOT_DIR}/.venv/bin/python" ]; then
    "${PY}" -m venv "${BOT_DIR}/.venv"
fi
"${BOT_DIR}/.venv/bin/python" -m pip install --upgrade pip
# requirements-forward-test.txt = requirements.txt + the HMM packages (hmmlearn, scikit-learn, scipy) pinned for Python 3.11
"${BOT_DIR}/.venv/bin/python" -m pip install -r "${BOT_DIR}/requirements-forward-test.txt"

echo "==> Runtime folders"
mkdir -p "${BOT_DIR}/logs" "${BOT_DIR}/state"

if [ ! -f "${BOT_DIR}/.env" ]; then
    cp "${BOT_DIR}/.env.example" "${BOT_DIR}/.env"
    chmod 600 "${BOT_DIR}/.env"
    echo "!!  Created ${BOT_DIR}/.env from the example: edit it with the key pair (nano .env)."
else
    chmod 600 "${BOT_DIR}/.env"
fi

echo "==> Sanity check"
"${BOT_DIR}/.venv/bin/python" -c "import requests, yaml, dotenv, pandas, numpy, scipy, sklearn, hmmlearn; print('imports OK: pandas', pandas.__version__, 'scipy', scipy.__version__, 'hmmlearn', hmmlearn.__version__)"
echo "HMM parity vs the lab (needs Binance access, ~1-2 min): ${BOT_DIR}/.venv/bin/python ${BOT_DIR}/check_hmm_parity.py"
echo "Done. Next: see RUNNING.md (tmux or systemd)."
