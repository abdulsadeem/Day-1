import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("housing_data.csv")

print("First 5 rows:")
print(df.head())

print("\nData Types:")
print(df.dtypes)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(df["SquareFootage"], df["Price"])
plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.title("Square Footage vs Price")

plt.subplot(1, 2, 2)
df.boxplot(column="Price", by="Location", ax=plt.gca())
plt.title("Price Distribution by Location")
plt.suptitle("")
plt.xlabel("Location")
plt.ylabel("Price")

plt.tight_layout()
plt.show()

print("\nObservation:")
print("As SquareFootage increases, Price seems to increase.")
