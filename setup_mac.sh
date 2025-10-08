#!/usr/bin/env bash
set -e

python3 -m venv .venv
source .venv/bin/activate

python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install --only-binary ":all:" -r requirements_macos.txt

python3 ml_model/generate_synthetic.py || true
python3 ml_model/train_model.py || true

streamlit run dashboard/app_3d.py
