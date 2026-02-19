import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
data = np.random.exponential(scale=50000, size=10000)

plt.figure(figsize=(8,5))
sns.histplot(data, bins=40, kde=True)
plt.title("Original Skewed Distribution (Income)")
plt.xlabel("Income")
plt.ylabel("Frequency")
plt.show()

sample_means = []

for i in range(1000):
    sample = np.random.choice(data, size=30, replace=True)
    sample_means.append(np.mean(sample))

sample_means = np.array(sample_means)

plt.figure(figsize=(8,5))
sns.histplot(sample_means, bins=30, kde=True)
plt.title("Distribution of 1000 Sample Means (n=30)")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.show()

print("Population Mean:", np.mean(data))
print("Mean of Sample Means:", np.mean(sample_means))
