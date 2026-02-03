Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> current_year = int(input("Enter the current year: "))
Enter the current year: 2026
>>> print("Current Year:", current_year)
Current Year: 2026
>>> name = input("Enter your name: ")
Enter your name: Sadeem
>>> age = int(input("Enter your current age: "))
Enter your current age: 22
>>> years_to_2030 = 2030 - current_year
>>> new_age = age + years_to_2030
>>> print(f"Hey {name}, you will be {new_age} years old in 2030!")
Hey Sadeem, you will be 26 years old in 2030!
>>> 
>>> #####################################################
>>> #The bill splitter
>>> bill = float(input("Total bill amount: "))
Total bill amount: 750
>>> people_count = int(input("Number of people: "))
Number of people: 4
>>> share = bill / people_count
>>> print("Total Bill:", bill, "Each person pays:", share)
Total Bill: 750.0 Each person pays: 187.5
>>> ##########################################################
>>> #Raw data
>>> bill = float(input("Total bill amount: "))
Total bill amount: 750
>>> people_count = int(input("Number of people: "))
Number of people: 4
>>> share = bill / people_count
>>> print("Total Bill:", bill, "Each person pays:", share)
Total Bill: 750.0 Each person pays: 187.5
