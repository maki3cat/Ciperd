import numpy as np
from transformers import DistilBertTokenizer, DistilBertModel
import torch

access_token = ""
# Initialize tokenizer and model
tokenizer = DistilBertTokenizer.from_pretrained(
    'distilbert-base-uncased', token=access_token)
model = DistilBertModel.from_pretrained(
    'distilbert-base-uncased', token=access_token)

# Example passages
passages = [
    "The quick brown fox jumps over the lazy dog.",
    "Machine learning is transforming the world of technology."
]

# Function to get DistilBERT embedding (from previous response)


def get_distilbert_embedding(passage, pooling='mean'):
    inputs = tokenizer(
        passage,
        return_tensors='pt',
        max_length=512,
        truncation=True,
        padding=True
    )
    with torch.no_grad():
        outputs = model(**inputs)
    hidden_states = outputs.last_hidden_state
    if pooling == 'cls':
        embedding = hidden_states[:, 0, :]
    elif pooling == 'mean':
        attention_mask = inputs['attention_mask']
        mask = attention_mask.unsqueeze(-1).expand(
            hidden_states.size()).float()
        sum_hidden = torch.sum(hidden_states * mask, dim=1)
        sum_mask = torch.clamp(mask.sum(dim=1), min=1e-9)
        embedding = sum_hidden / sum_mask
    return embedding.squeeze().numpy()


# Get embeddings for the two passages
embedding1 = get_distilbert_embedding(passages[0], pooling='mean')
embedding2 = get_distilbert_embedding(passages[1], pooling='mean')

# Compute cosine similarity


def cosine_similarity(emb1, emb2):
    emb1_norm = emb1 / np.linalg.norm(emb1)
    emb2_norm = emb2 / np.linalg.norm(emb2)
    similarity = np.dot(emb1_norm, emb2_norm)
    return similarity


# Calculate and print similarity
similarity = cosine_similarity(embedding1, embedding2)
print(f"Passage 1: {passages[0]}")
print(f"Passage 2: {passages[1]}")
print(f"Cosine Similarity: {similarity:.4f}")
