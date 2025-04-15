import os
from simi_sen import get_similarity, read_sample
import matplotlib.pyplot as plt

# Base directory
base_dir = "data_1"

# List of file/folder names
entries = [
    "ds_prm1_A_1",
    "ds_prm1_A_4_medium_100",
    "ds_prm1_A_4_severe_100",
    "ds_prm1_N",
    "gk_A_4_light_100",
    "gk_N_1_300_agejob",
    "gk_N_5_300",
    "gk_N_tune_1",
    "gk_N_tune_2",
    "gk_S_1_300",
    "gk_S_4_300"
]
# Construct full paths
full_paths = [os.path.join(base_dir, entry) for entry in entries]
x_label = []
y_label = []

# Optional: Print or use the list
for path in full_paths:
    conv = read_sample(300, path)
    avg = get_similarity(conv)
    print(f"{path}: {avg}")
    x_label.append(path.split('/')[-1])
    y_label.append(avg)

path1 = "data_2/gpt4-80"
conv1 = read_sample(80, path1)
avg1 = get_similarity(conv1)
print(f"{path1}: {avg1}")
x_label.append(path1.split('/')[-1])
y_label.append(avg1)


def pain(x_label, y_label):
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


pain(x_label, y_label)
