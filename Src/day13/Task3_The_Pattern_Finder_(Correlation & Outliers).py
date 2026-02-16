import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("housing.csv")

print("Dataset Preview:\n", df.head())

correlation_matrix = df.corr(numeric_only=True)
print("\nCorrelation Matrix:\n", correlation_matrix)

plt.figure(figsize=(6,5))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

print("\nHighly Correlated Pairs (>0.8):")
for i in range(len(correlation_matrix.columns)):
    for j in range(i):
        if abs(correlation_matrix.iloc[i, j]) > 0.8:
            print(correlation_matrix.columns[i], "and",
                  correlation_matrix.columns[j], "=",
                  correlation_matrix.iloc[i, j])

plt.figure(figsize=(5,4))
sns.boxplot(y=df['Price'])
plt.title("Boxplot for Price")
plt.show()
