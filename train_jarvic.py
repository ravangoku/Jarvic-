# train_jarvic.py
# Train a small causal LM from scratch using HuggingFace Trainer.
# Usage:
#   python train_jarvic.py --seed_file jarvic_seed.jsonl --output_dir ./jarvic_model --epochs 3

import os
import argparse
from datasets import load_dataset
from transformers import (
    GPT2TokenizerFast,
    GPT2LMHeadModel,
    DataCollatorForLanguageModeling,
    Trainer,
    TrainingArguments
)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed_file", default="jarvic_seed.jsonl")
    parser.add_argument("--output_dir", default="./jarvic_model")
    parser.add_argument("--epochs", type=int, default=3)
    parser.add_argument("--vocab_size", type=int, default=8000)
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    print("Loading GPT2 tokenizer (pretrained gpt2)...")
    tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
    special_tokens = {"bos_token":"<|user|>", "eos_token":"<|assistant|>", "pad_token":"<|pad|>"}
    tokenizer.add_special_tokens(special_tokens)

    # Load dataset from our jsonl file
    dataset = load_dataset("json", data_files=args.seed_file, split="train")
    def preprocess(ex):
        return tokenizer(ex["text"], truncation=True, max_length=256)
    tokenized = dataset.map(preprocess, remove_columns=dataset.column_names)

    # Data collator for causal LM
    data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

    # Model config: small
    from transformers import GPT2Config
    config = GPT2Config(
        vocab_size=len(tokenizer),
        n_positions=256,
        n_ctx=256,
        n_embd=384,
        n_layer=6,
        n_head=6
    )
    model = GPT2LMHeadModel(config)
    model.resize_token_embeddings(len(tokenizer))

    training_args = TrainingArguments(
        output_dir=args.output_dir,
        overwrite_output_dir=True,
        num_train_epochs=args.epochs,
        per_device_train_batch_size=4,
        save_steps=200,
        save_total_limit=2,
        logging_steps=20,
        fp16=False,
        push_to_hub=False,
        report_to=[],
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized,
        data_collator=data_collator,
    )
    trainer.train()
    trainer.save_model(args.output_dir)
    tokenizer.save_pretrained(args.output_dir)
    print("Training complete. Model saved to", args.output_dir)

if __name__ == "__main__":
    main()
