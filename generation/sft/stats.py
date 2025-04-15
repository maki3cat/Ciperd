from load_data import TOKENIZER
import pandas as pd
import numpy as np
from collections import Counter

def compute_t5_stats():
    tokenizer = TOKENIZER
    train_sqls = []
    train_nls = []
    with open('data/train.sql') as f:
        train_sqls.extend(f.readlines())
    with open('data/train.nl') as f:
        train_nls.extend(f.readlines()) 

    train_size = len(train_nls)
    print("Train size: ", train_size)
    
    # Calculate tokenized lengths
    nl_lengths = []
    sql_lengths = []
    
    # For vocabulary analysis
    nl_tokens = Counter()
    sql_tokens = Counter()
    
    for _, idx in range(train_size):
        text_nl = train_nls[idx]
        text_sql = train_sqls[idx]
        nl_tokenized = tokenizer.tokenize(text_nl)
        sql_tokenized = tokenizer.tokenize(text_sql)
        nl_lengths.append(len(nl_tokenized))
        sql_lengths.append(len(sql_tokenized))
        nl_tokens.update(nl_tokenized)
        sql_tokens.update(sql_tokenized)
    
    mean_nl_length = np.mean(nl_lengths)
    mean_sql_length = np.mean(sql_lengths)
    print(f"Mean natural language length: {mean_nl_length}")
    print(f"Mean SQL query length: {mean_sql_length}")
    
    # Vocabulary sizes (unique tokens)
    nl_vocab_size = len(nl_tokens)
    sql_vocab_size = len(sql_tokens)

    print(f"Natural language vocabulary size: {nl_vocab_size}")
    print(f"SQL vocabulary size: {sql_vocab_size}")
    
    return {
        "Number of examples": train_size,
        "Mean sentence length": round(mean_nl_length, 2),
        "Mean SQL query length": round(mean_sql_length, 2),
        "Vocabulary size (natural language)": nl_vocab_size,
        "Vocabulary size (SQL)": sql_vocab_size
    }

if __name__ == "__main__":
    stats = compute_t5_stats()
    print(stats)