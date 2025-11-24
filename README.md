# Jarvic — Starter (English-only) — Single-file ZIP

This repository is a starter kit for **Jarvic**, a minimal, from-scratch English conversational AI.
It includes:
- `prepare_seed_jsonl.py`: creates `jarvic_seed.jsonl` with 25 seed prompt-response pairs.
- `train_jarvic.py`: trains a small GPT-style model on the seed data using HuggingFace Trainer.
- `infer_and_export.py`: runs a test generation and attempts a TorchScript export.
- `requirements.txt`

## Quick setup
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python prepare_seed_jsonl.py
python train_jarvic.py --seed_file jarvic_seed.jsonl --output_dir ./jarvic_model --epochs 3
python infer_and_export.py --model_dir ./jarvic_model --prompt "Hi Jarvic." --out_ts jarvic_ts.pt
```

Notes:
- This is a small, educational starter. For production you need much more data, longer training, quantization, and mobile conversion steps.
- The scripts are intentionally compact and readable so you can iterate quickly.
