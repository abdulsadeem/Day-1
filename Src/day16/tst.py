import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV
df = pd.read_csv("shape_shifter.csv")

# Create subplot layout (1 row, 3 columns)
fig, axes = plt.subplots(1, 3, figsize=(18,5))

for i, column in enumerate(df.columns):
    
    mean = df[column].mean()
    median = df[column].median()
    
    print("\n" + "="*40)
    print(f"{column}")
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median:.2f}")
    
    if mean > median:
        print("Distribution Type: Right-Skewed")
    elif mean < median:
        print("Distribution Type: Left-Skewed")
    else:
        print("Distribution Type: Approximately Normal")
    
    # Plot in subplot
    sns.histplot(df[column], bins=10, kde=True, ax=axes[i])
    axes[i].axvline(mean, color='red', linestyle='--', label='Mean')
    axes[i].axvline(median, color='green', linestyle='--', label='Median')
    axes[i].set_title(f"{column} Distribution")
    axes[i].set_xlabel("Value")
    axes[i].set_ylabel("Frequency")
    axes[i].legend()

plt.tight_layout()
plt.show()
