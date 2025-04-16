import os
import matplotlib.pyplot as plt

from sentence_transformers import SentenceTransformer
import numpy as np

# 1. Load a pretrained Sentence Transformer model
model = SentenceTransformer("all-MiniLM-L6-v2", token="")

# 2. Read the sample data


def read_sample(k, path):
    conversations = []
    count = 0
    with open(path, "r") as f:
        lines = f.readlines()
        for line in lines:
            count += 1
            if len(conversations) >= k:
                break
            if count % 2 == 1:
                continue
            else:
                conversations.append(line.strip())
    return conversations


def get_similarity(conversations):
    # 2. Calculate embeddings by calling model.encode()
    # embeddings = model.encode(sentences)
    # print(embeddings.shape)
    embeddings = model.encode(conversations)
    print(embeddings.shape)
    # [3, 384]

    # 3. Calculate the embedding similarities
    similarities = model.similarity(embeddings, embeddings)
    non_diag_mask = ~np.eye(similarities.shape[0], dtype=bool)
    average_non_diag = similarities[non_diag_mask].mean()
    # tensor to float
    average_non_diag = average_non_diag.item()
    rounded_average = round(average_non_diag, 5)
    return rounded_average


# Base directory
# base_dir = ["data_1", "data_2a", "data_2b"]
base_dir = "dataset"
x_label = []
y_label = []
for dir in os.listdir(base_dir):
    dir = os.path.join(base_dir, dir)
    if os.path.isfile(dir):
        continue
    print(f"Processing {dir}")
    for file in os.listdir(dir):
        path = os.path.join(dir, file)
        if not os.path.isfile(path):
            print(f"Skip file {path}")
            continue
        if file.endswith("data.txt"):
            conv = read_sample(100000, path)
            avg = get_similarity(conv)
            print(f"similarity {path}: {avg}")
            x_label.append(path)
            y_label.append(avg)
# sort the x_label and y_label by y_label
sorted_indices = sorted(range(len(y_label)), key=lambda k: y_label[k])
x_label = [x_label[i] for i in sorted_indices]
y_label = [y_label[i] for i in sorted_indices]


def plot(x_label, y_label):
    plt.figure(figsize=(10, 6))
    plt.bar(x_label, y_label, color='blue')
    plt.xlabel('dataset names')
    plt.ylabel('similarity')
    plt.title('Similarity Evaluation')
    plt.xticks(rotation=45)
    for i, v in enumerate(y_label):
        plt.text(i, v + 0.01, f'{v:.2f}', ha='center')
    plt.tight_layout()
    plt.show()


plot(x_label, y_label)
