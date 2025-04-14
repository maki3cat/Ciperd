from sentence_transformers import SentenceTransformer
import numpy as np
import os

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


path1 = "data_2/gpt4-prompt-conversation-80"
conv1 = read_sample(80, path1)
avg1 = get_similarity(conv1)
print(f"{path1}: {avg1}")

path2 = "data_1/deepseek_avoidant_1"
conv2 = read_sample(80, path2)
avg2 = get_similarity(conv2)
print(f"{path2}: {avg2}")

path3 = "data_1/grok_narcissistic_5_300"
conv3 = read_sample(80, path3)
avg3 = get_similarity(conv3)
print(f"{path3}: {avg3}")

conv3 = read_sample(80, path3)
avg3 = get_similarity(conv3)
print(f"{path3}: {avg3}")

path4 = "data_1/sample_llm_npd"
conv4 = read_sample(80, path4)
avg4 = get_similarity(conv4)
print(f"{path4}: {avg4}")

path5 = "data_1/sample_llm_normal"
conv5 = read_sample(300, path5)
avg5 = get_similarity(conv5)
print(f"{path5}: {avg5}")

path6 = "data_1/grok_schizoid_4_300"
conv6 = read_sample(300, path6)
avg6 = get_similarity(conv6)
print(f"{path6}: {avg6}")

path7 = "data_1/grok_schizoid_1_300"
conv7 = read_sample(300, path7)
avg7 = get_similarity(conv7)
print(f"{path7}: {avg7}")

path8 = "data_1/grok_schizoid_1_300"
conv8 = read_sample(300, path8)
avg8 = get_similarity(conv8)
print(f"{path8}: {avg8}")
