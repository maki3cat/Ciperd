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


# calculate_tokens("data_2/prompt.txt")


# read every file in dir data_1, calcualte the token


def calculate_tokens_dir(directory):
    total_tokens = 0
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip non-files (just in case)
        if not os.path.isfile(file_path):
            continue
        calculate_tokens(file_path)
    print(f"\n🔢 Total tokens in directory '{directory}': {total_tokens}")


calculate_tokens_dir("data_1")
