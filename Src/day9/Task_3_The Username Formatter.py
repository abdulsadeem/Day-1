import pandas as pd

usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])

cleaned_usernamesl = usernames.str.strip().str.lower()
cleaned_usernamesu = usernames.str.strip().str.upper()


contains_a = cleaned_usernamesl.str.contains('a')
contains_b = cleaned_usernamesu.str.contains('A','D')


print("Cleaned Usernames:")
print(cleaned_usernamesl)
print(cleaned_usernamesu)
print("\nContains letter 'a':")
print(contains_a)
print("\nContains letter :")
print(contains_b)