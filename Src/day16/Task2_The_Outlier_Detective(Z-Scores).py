import pandas as pd
import numpy as np

df = pd.read_csv("shape_shifter.csv")

print("Original Dataset:")
print(df.head())

for col in df.columns:
    
    mean = df[col].mean()
    std = df[col].std()
    
    print("\n" + "="*50)
    print(f"{col}")
    print(f"Mean (μ): {mean:.2f}")
    print(f"Standard Deviation (σ): {std:.2f}")
    
    df[f"{col}_Z"] = (df[col] - mean) / std
    
    outliers = df[np.abs(df[f"{col}_Z"]) > 3]
    
    if outliers.empty:
        print("No statistical outliers found (|Z| > 3).")
    else:
        print("Outliers:")
        print(outliers[[col, f"{col}_Z"]])

print("\nFinal Data with Z-Scores:")
print(df)
