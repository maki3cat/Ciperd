import matplotlib.pyplot as plt

# Data
k = [0, 1, 2]
f1 = [0.118, 0.06, 0.06]

# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(k, f1, marker='o', linestyle='-', color='b')

# Adding titles and labels
plt.title('Plot of f1 over k')
plt.xlabel('k')
plt.ylabel('f1')

# Show grid
plt.grid()

# Show the plot
plt.show()

