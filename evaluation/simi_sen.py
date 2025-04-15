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
