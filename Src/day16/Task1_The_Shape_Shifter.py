import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(1)

heights = np.random.normal(loc=170, scale=10, size=1000)            # Normal
incomes = np.random.exponential(scale=50000, size=1000)             # Right-skewed
scores = 100 - np.random.exponential(scale=15, size=1000)           # Left-skewed

datasets = {
    "Human Heights (Normal Distribution)": heights,
    "Household Incomes (Right-Skewed Distribution)": incomes,
    "Easy Exam Scores (Left-Skewed Distribution)": scores
}

fig, axes = plt.subplots(1, 3, figsize=(18,5))

for i, (name, data) in enumerate(datasets.items()):
    
    mean = np.mean(data)
    median = np.median(data)
    
    print("\n" + "="*50)
    print(name)
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median:.2f}")
    
    if mean > median:
        print("Distribution Type: Right-Skewed")
    elif mean < median:
        print("Distribution Type: Left-Skewed")
    else:
        print("Distribution Type: Approximately Normal")
    
    sns.histplot(data, bins=30, kde=True, ax=axes[i])
    axes[i].axvline(mean, color='red', linestyle='--', label='Mean')
    axes[i].axvline(median, color='green', linestyle='--', label='Median')
    axes[i].set_title(name)
    axes[i].set_xlabel("Value")
    axes[i].set_ylabel("Frequency")
    axes[i].legend()

plt.tight_layout()
plt.show()
