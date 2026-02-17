import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv("cars.csv")

print("\nOriginal Dataset:\n")
print(df.head())
print(df.tail())

le = LabelEncoder()
df["Transmission"] = le.fit_transform(df["Transmission"])

df = pd.get_dummies(df, columns=["Color"], drop_first=True)

print("\nAfter Encoding:\n")
print(df.head())

X = df.drop("Price", axis=1)
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

baseline_model = LinearRegression()
baseline_model.fit(X_train_scaled, y_train)

baseline_preds = baseline_model.predict(X_test_scaled)
baseline_r2 = r2_score(y_test, baseline_preds)

print("\nBaseline R2 Score:", baseline_r2)

poly = PolynomialFeatures(degree=2, include_bias=False)

X_train_poly = poly.fit_transform(X_train_scaled)
X_test_poly = poly.transform(X_test_scaled)

poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)

poly_preds = poly_model.predict(X_test_poly)
poly_r2 = r2_score(y_test, poly_preds)

print("Polynomial R2 Score:", poly_r2)

print("Improvement in R2:", poly_r2 - baseline_r2)
