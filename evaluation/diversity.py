import os
from simi_sen import get_similarity, read_sample
import matplotlib.pyplot as plt

# Base directory
base_dir = ["data_1", "data_2"]
x_label = []
y_label = []
for dir in base_dir:
    for file in os.listdir(dir):
        path = os.path.join(dir, file)
        print(f"Processing {path}, is file:{os.path.isfile(path)}")
        if not os.path.isfile(path):
            print(f"Skip file {path}")
            continue
        if file.endswith(".py"):
            continue
        conv = read_sample(300, path)
        avg = get_similarity(conv)
        print(f"{path}: {avg}")
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
