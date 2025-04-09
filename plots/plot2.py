import matplotlib.pyplot as plt

# Data from the survey
clusters = ['Cluster A', 'Cluster B', 'Cluster C', 'Any PD']
prevalence = [5.7, 1.5, 6.0, 9.1]  # Prevalence percentages

# Create the bar graph
plt.figure(figsize=(8, 6))  # Set figure size
bars = plt.bar(clusters, prevalence, color=['#4CAF50', '#FF5733', '#3498DB', '#9B59B6'], edgecolor='black')

# Add titles and labels
plt.title('Prevalence of DSM-IV Personality Disorders in the U.S. Population\n(National Comorbidity Survey Replication)', fontsize=14, pad=15)
plt.xlabel('Personality Disorder Category', fontsize=12)
plt.ylabel('Prevalence (%)', fontsize=12)

# Add percentage labels on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.2, f'{yval}%', ha='center', va='bottom', fontsize=10)

# Adjust y-axis limit for better visibility
plt.ylim(0, 10)

# Display the graph
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Optional: adds a grid for readability
plt.tight_layout()
plt.show()
