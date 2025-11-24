# infer_and_export.py
# Load saved model and tokenizer; run a test generation and export TorchScript model.
import torch
from transformers import GPT2LMHeadModel, GPT2TokenizerFast
import argparse
import os

def generate_text(model, tokenizer, prompt, max_new_tokens=60):
    inputs = tokenizer(prompt, return_tensors="pt")
    input_ids = inputs["input_ids"]
    output_ids = model.generate(input_ids.to(model.device), max_new_tokens=max_new_tokens, do_sample=False)
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)

def export_torchscript(model, tokenizer, output_path):
    model.eval()
    dummy_input = torch.randint(0, len(tokenizer), (1, 8)).long()
    model_cpu = model.cpu()
    try:
        traced = torch.jit.trace(model_cpu, (dummy_input,))
        traced.save(output_path)
        print("Saved TorchScript model to", output_path)
    except Exception as e:
        print("TorchScript export failed (safe to ignore for now):", e)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_dir", default="./jarvic_model")
    parser.add_argument("--prompt", default="Hi Jarvic.")
    parser.add_argument("--out_ts", default="jarvic_ts.pt")
    args = parser.parse_args()

    tokenizer = GPT2TokenizerFast.from_pretrained(args.model_dir)
    model = GPT2LMHeadModel.from_pretrained(args.model_dir)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)

    print("Generating for prompt:", args.prompt)
    out = generate_text(model, tokenizer, f"<|user|> {args.prompt} <|assistant|>")
    print("=== Generation ===")
    print(out)

    print("Exporting TorchScript (best-effort)...")
    export_torchscript(model, tokenizer, args.out_ts)

if __name__ == "__main__":
    main()
