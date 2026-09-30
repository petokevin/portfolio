#!/bin/zsh
set -eu
cd "$(dirname "$0")"
if [[ -x .venv/bin/python ]]; then
  PYTHON=.venv/bin/python
elif [[ -x ../.venv/bin/python ]]; then
  PYTHON=../.venv/bin/python
else
  echo 'Először hozd létre a virtuális környezetet a README.md szerint.'
  exit 1
fi
exec "$PYTHON" manage.py runserver 127.0.0.1:8001
