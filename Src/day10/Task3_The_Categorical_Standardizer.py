import pandas as pd
data = pd.DataFrame({
    'Price': ['$100.50', '$250.75', '$89.99'],
    'Date': ['2026-02-01', '2026-02-05', '2026-02-10']
})
print("Initial Data Types:")
print(data.dtypes)
data['Price'] = data['Price'].str.replace('$', '', regex=False).astype(float)
data['Date'] = pd.to_datetime(data['Date'])
print("\nData after conversion:")
print(data)
print("\nData Types after conversion:")
print(data.dtypes)
