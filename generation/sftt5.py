import os
import torch
from datasets import Dataset
from transformers import (
    AutoTokenizer, AutoModelForSeq2SeqLM, Trainer,
    TrainingArguments, DataCollatorForSeq2Seq)
from sklearn.metrics import accuracy_score

access_token = ""
DEVICE = torch.device(
    'cuda') if torch.cuda.is_available() else torch.device('cpu')
model = AutoModelForSeq2SeqLM.from_pretrained(
    "google-t5/t5-small", token=access_token)
model.to(DEVICE)
tokenizer = AutoTokenizer.from_pretrained(
    "google-t5/t5-small", token=access_token)

SAVE_DIR = "mdls/t5-small-finetuned"
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)


# Load data from txt files
with open("data_2/prompt.txt", "r", encoding="utf-8") as f:
    inputs = f.readlines()

with open("data_2/response.txt", "r", encoding="utf-8") as f:
    targets = f.readlines()

# Build a Hugging Face dataset
raw_dataset = Dataset.from_dict({"input_text": inputs, "target_text": targets})

# Preprocessing function


def preprocess(example):
    model_inputs = tokenizer(
        example["input_text"], max_length=512, truncation=True)
    labels = tokenizer(example["target_text"], max_length=128, truncation=True)
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs


tokenized_dataset = raw_dataset.map(preprocess, remove_columns=[
                                    "input_text", "target_text"])

# Define training arguments
training_args = TrainingArguments(
    output_dir="./results",
    eval_strategy="epoch",
    save_strategy="epoch",
    learning_rate=5e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
    weight_decay=0.01,
    logging_dir="./logs",
    logging_steps=10,
    save_total_limit=2,
    push_to_hub=False,
)

# Data collator
data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

# Initialize trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    eval_dataset=tokenized_dataset,
    tokenizer=tokenizer,
    data_collator=data_collator,
)

# Fine-tune
trainer.train()


# Generate predictions
preds = []
labels = []

for ex in raw_dataset:
    input_ids = tokenizer(
        ex["input_text"], return_tensors="pt").input_ids.to(DEVICE)
    output_ids = model.generate(input_ids, max_length=128)
    decoded_pred = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    preds.append(decoded_pred.strip())
    labels.append(ex["target_text"].strip())

# Basic string accuracy
accuracy = accuracy_score(labels, preds)
print(f"Accuracy: {accuracy:.2f}")

print("💾 Saving model to current directory...")
model.save_pretrained(SAVE_DIR)
tokenizer.save_pretrained(SAVE_DIR)
