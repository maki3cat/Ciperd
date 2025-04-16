from transformers import AutoTokenizer
import os

tokenizer = AutoTokenizer.from_pretrained(
    "google-t5/t5-small",
)


def calculate_tokens(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    tokens = tokenizer.encode(text, add_special_tokens=True)
    return len(tokens)


# read every file in dir data_1, calcualte the token


def calculate_tokens_dir(directory):
    total_tokens = 0
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if file_path.endswith("py"):
            continue
        if not os.path.isfile(file_path):
            continue
        total_tokens += calculate_tokens(file_path)
    print(f"\n🔢 Total tokens in directory '{directory}': {total_tokens}")


calculate_tokens_dir("data_1")
calculate_tokens_dir("data_2")
