import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv("employee_salary.csv")

education_order = {
    "Bachelors": 0,
    "Masters": 1,
    "PhD": 2
}

df["Education_Level"] = df["Education_Level"].map(education_order)

df = pd.get_dummies(df, columns=["Department"], drop_first=True)

X = df.drop("Salary", axis=1)
y = df["Salary"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

baseline_model = LinearRegression()
baseline_model.fit(X_train, y_train)
baseline_preds = baseline_model.predict(X_test)
baseline_r2 = r2_score(y_test, baseline_preds)

print("Baseline R2 Score:", baseline_r2)

std_scaler = StandardScaler()
X_train_std = std_scaler.fit_transform(X_train)
X_test_std = std_scaler.transform(X_test)

std_model = LinearRegression()
std_model.fit(X_train_std, y_train)
std_preds = std_model.predict(X_test_std)
std_r2 = r2_score(y_test, std_preds)

print("Standard Scaled R2 Score:", std_r2)

mm_scaler = MinMaxScaler()
X_train_mm = mm_scaler.fit_transform(X_train)
X_test_mm = mm_scaler.transform(X_test)

mm_model = LinearRegression()
mm_model.fit(X_train_mm, y_train)
mm_preds = mm_model.predict(X_test_mm)
mm_r2 = r2_score(y_test, mm_preds)

print("MinMax Scaled R2 Score:", mm_r2)

print("Improvement (Standard - Baseline):", std_r2 - baseline_r2)
print("Improvement (MinMax - Baseline):", mm_r2 - baseline_r2)

experience_index = list(X.columns).index("Experience")

plt.figure(figsize=(14,6))

plt.subplot(1,2,1)
sns.histplot(X_train["Experience"], kde=True)
plt.title("Before Scaling (Experience)")

plt.subplot(1,2,2)
sns.histplot(X_train_std[:, experience_index], kde=True)
plt.title("After Standard Scaling (Experience)")

plt.tight_layout()
plt.show()
