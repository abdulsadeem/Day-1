import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

df = pd.read_csv("employee_salary.csv")

X = df[["Experience"]]
y = df["Salary"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

linear_preds = linear_model.predict(X_test)
linear_r2 = r2_score(y_test, linear_preds)

print("Linear R2 Score:", linear_r2)

poly = PolynomialFeatures(degree=2)

X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)

poly_preds = poly_model.predict(X_test_poly)
poly_r2 = r2_score(y_test, poly_preds)

print("Polynomial R2 Score:", poly_r2)
print("Improvement (Polynomial - Linear):", poly_r2 - linear_r2)
