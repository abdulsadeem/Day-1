import pandas as pd
locations = pd.Series([' New York', 'new york', 'NEW YORK ', 'Los Angeles', ' los angeles '])
locations_cleaned = locations.str.strip()
locations_cleaned = locations_cleaned.str.title()
unique_locations = locations_cleaned.unique()
print("Cleaned Locations:")
print(locations_cleaned)
print("\nUnique Locations:")
print(unique_locations)
