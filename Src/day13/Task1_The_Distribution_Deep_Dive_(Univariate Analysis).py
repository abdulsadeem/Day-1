import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis
import numpy as np

df = pd.read_csv("housing.csv")

# Histogram + KDE
plt.figure(figsize=(8,5))
sns.histplot(df["Price"], kde=True)
plt.title("Distribution of Housing Prices")
plt.show()

# Skewness & Kurtosis
print("Skewness:", skew(df["Price"]))
print("Kurtosis:", kurtosis(df["Price"]))

# Count Plot
plt.figure(figsize=(8,5))
sns.countplot(x=df["City"])
plt.xticks(rotation=45)
plt.title("Count of Houses by City")
plt.show()

# Log Transformation (if needed)
df["Log_Price"] = np.log(df["Price"])