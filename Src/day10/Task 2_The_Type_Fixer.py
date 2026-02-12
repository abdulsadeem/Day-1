import pandas as pd

df = pd.read_csv("customer_orders.csv")

print("Before conversion:")
print(df.dtypes)

df["OrderAmount"] = pd.to_numeric(df["OrderAmount"], errors="coerce")
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

print("\nAfter conversion:")
print(df.dtypes)

print("\nAverage Order Amount:", df["OrderAmount"].mean())

