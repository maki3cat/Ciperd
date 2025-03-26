import matplotlib.pyplot as plt
import numpy as np

# Data
disorders_by_cluster = [
    ['Paranoid (0.5-2.5%)', 'Schizoid (0.5-7%)', 'Schizotypal (3%)'],
    ['Antisocial (1%)', 'Borderline (1.6%)', 'Histrionic (1-3%)', 'Narcissistic (2-16%)'],
    ['Avoidant (5.2%)', 'Dependent (0.6%)', 'Obsessive-Compulsive (2.4%)']
]
percentages_by_cluster = [
    [1.5, 3.5, 3],  # Average percentages for Cluster A
    [1, 1.6, 2, 9],  # Average percentages for Cluster B
    [5.2, 0.6, 2.4]   # Percentages for Cluster C
]
cluster_labels = ['A', 'B', 'C']

# Flatten disorders and percentages
all_disorders = []
all_percentages = []
for i, disorders in enumerate(disorders_by_cluster):
    for j, disorder in enumerate(disorders):
        all_disorders.append(f"{cluster_labels[i]}: {disorder}")
        all_percentages.append(percentages_by_cluster[i][j])

# Sort both lists based on percentages (descending)
sorted_indices = np.argsort(all_percentages)[::-1]
sorted_disorders = [all_disorders[i] for i in sorted_indices]
sorted_percentages = [all_percentages[i] for i in sorted_indices]

# Increase font sizes
plt.rcParams.update({'font.size': 14})  # Set base font size
title_size = 18
axis_label_size = 16
tick_label_size = 14
legend_size = 12

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Create horizontal bars with reduced height
bars = ax.barh(range(len(sorted_disorders)), sorted_percentages, height=0.5)  # Smaller bar height

# Add percentage labels with larger font
for i, v in enumerate(sorted_percentages):
    ax.text(v + 0.1, i, f"{v}%", va='center', fontsize=tick_label_size)
# Add color coding by cluster
for i, bar in enumerate(bars):
    cluster = sorted_disorders[i][0]  # First character is the cluster label
    if cluster == 'A':
        bar.set_color('skyblue')
    elif cluster == 'B':
        bar.set_color('lightcoral')
    else:  # Cluster C
        bar.set_color('lightgreen')

# Labeling
ax.set_yticks(range(len(sorted_disorders)))
ax.set_yticklabels(sorted_disorders)
ax.set_xlabel('Population Percentage Averaged (%)')
ax.set_title('Personality Disorders Sorted by Prevalence in US population')
ax.invert_yaxis()  # Highest values at the top

# Add a legend for clusters
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='skyblue', label='Cluster A'),
    Patch(facecolor='lightcoral', label='Cluster B'),
    Patch(facecolor='lightgreen', label='Cluster C')
]
ax.legend(handles=legend_elements, loc='lower right')

plt.tight_layout()
plt.show()
