import os
from simi_sen import get_similarity, read_sample

# Base directory
base_dir = "data_1"

# List of file/folder names
entries = [
    "deepseek_avoidant_1",
    "deepseek_avoidant_4_medium_100",
    "deepseek_avoidant_4_severe_100",
    "deepseek_normal",
    "grok_ds_avoidant_4_light_100",
    "grok_narcissistic_1_300_age_occupation",
    "grok_narcissistic_5_300",
    "grok_schizoid_1_300",
    "grok_schizoid_4_300",
    "sample_llm_normal"
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
    x_label.append(path)
    y_label.append(avg)
