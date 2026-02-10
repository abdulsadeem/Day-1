Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> inventory = ["Apples", "Bananas", "Carrots", "Dates"]
>>> print("Current inventory:", inventory)
Current inventory: ['Apples', 'Bananas', 'Carrots', 'Dates']
>>> inventory.append("Eggs")
>>> inventory.remove("Bananas")
>>> inventory.sort()
>>> print("Final updated inventory:", inventory)
Final updated inventory: ['Apples', 'Carrots', 'Dates', 'Eggs']
>>> ######################################################################
>>> #t2Indexing & Slicing
>>> 
>>> temperatures = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]
>>> print("First reading:", temperatures[0])
First reading: 22
>>> print("Last reading:", temperatures[-1])
Last reading: 22
>>> print("Last reading:", temperatures[9])
Last reading: 22
>>> print("Last reading:", temperatures[-9])
Last reading: 24
>>> print("one", temperatures[2])
one 25
>>> afternoon_peak = temperatures[3:6]
>>> print("Afternoon Peak readings:", afternoon_peak)
Afternoon Peak readings: [28, 30, 29]
>>> last_three_hours = temperatures[-3:]
>>> print("Last 3 hours readings:", last_three_hours)
Last 3 hours readings: [26, 24, 22]
>>> #####################################################################
>>> #t3 tuple
>>> 
>>> screen_res = (1920, 1080)
>>> print("Current Resolution:", screen_res[0], "x", screen_res[1])
Current Resolution: 1920 x 1080
>>> 
>>> screen_res = (1920, 1080)
>>> print(f"Current Resolution: {screen_res[0]}x{screen_res[1]}")
Current Resolution: 1920x1080
>>> screen_res[0] = 1280  
... print("Tuples cannot be modified!")
SyntaxError: multiple statements found while compiling a single statement
screen_res[0] = 1280 print("Tuples cannot be modified!")
SyntaxError: invalid syntax
#screen_res[0] = 1280  
print("Tuples cannot be modified!")
Tuples cannot be modified!
