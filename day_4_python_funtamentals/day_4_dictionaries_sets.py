Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
student={
    "name":"amar",
    "age":21,
    "course":"Engineering"}
print(student["name"])
amar
student["age"]=22
student["city"]="Delhi"
print(student)
{'name': 'amar', 'age': 22, 'course': 'Engineering', 'city': 'Delhi'}

#######################################
#contact book
contacts={
    "Saddam":9876543219,
    "Shamim":8678954321,
    "Jalalu":6789054321}
contacts["aachhi"]=9876544134
print(contacts)
{'Saddam': 9876543219, 'Shamim': 8678954321, 'Jalalu': 6789054321, 'aachhi': 9876544134}
contacts["Shamim"]=8678956741
print(contacts)
{'Saddam': 9876543219, 'Shamim': 8678956741, 'Jalalu': 6789054321, 'aachhi': 9876544134}
print("Lookup Saddam:",contacts.get("Saddam","Contact not found"))
Lookup Saddam: 9876543219
print("Lookup Sadam:",contacts.get("Sadam","Does not exist"))
Lookup Sadam: Does not exist
print("Adam:",contacts.get("Adam","Does not exist"))
Adam: Does not exist
for name,phone in contacts.items():
    print(f"Contact:{name}|Phone:{phone}")

    
Contact:Saddam|Phone:9876543219
Contact:Shamim|Phone:8678956741
Contact:Jalalu|Phone:6789054321
Contact:aachhi|Phone:9876544134
################################################################
#duplicate cleaner
raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
unique_users = set(raw_logs)
print("ID05 is unique_user","ID05" in unique_user)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print("ID05 is unique_user","ID05" in unique_user)
NameError: name 'unique_user' is not defined. Did you mean: 'unique_users'?
>>> print("ID05 is unique_user","ID05" in unique_users)
ID05 is unique_user True
>>> print("ID09 is unique_user","ID09" in unique_users)
ID09 is unique_user False
>>> print("Total raw log entries:", len(raw_logs))
Total raw log entries: 7
>>> print("Total unique users:", len(unique_users))
Total unique users: 4
>>> print("\nUnique User IDs:",unique_users)

Unique User IDs: {'ID01', 'ID05', 'ID08', 'ID02'}
>>> 
>>> 
>>> 

>>> friend_a = {"Python", "Cooking", "Hiking", "Movies"}
... 
>>> friend_b = {"Hiking", "Gaming", "Photography", "Python"}
>>> shared_interests = friend_a & friend_b
>>> print("shared_interests")
shared_interests
>>> print(shared_interests)
{'Hiking', 'Python'}
>>> all_interests = friend_a | friend_b
>>> print(all_interests)
{'Gaming', 'Python', 'Photography', 'Cooking', 'Hiking', 'Movies'}
>>> unique_to_a = friend_a - friend_b
>>> print()
KeyboardInterrupt
>>> print(unique_to_a)
{'Cooking', 'Movies'}
>>> print()
KeyboardInterrupt
>>> print("Shared Interests:", shared_interests "\n""All Interests:", all_interests "\n""Interests only Friend A has:", unique_to_a)
SyntaxError: invalid syntax
>>> print("Shared Interests:", shared_interests"\n","All Interests:", all_interests"\n","Interests only Friend A has:", unique_to_a)
SyntaxError: invalid syntax
>>> print("Shared Interests:", shared_interests,"\n","All Interests:", all_interests,"\n","Interests only Friend A has:", unique_to_a)
Shared Interests: {'Hiking', 'Python'} 
 All Interests: {'Gaming', 'Python', 'Photography', 'Cooking', 'Hiking', 'Movies'} 
 Interests only Friend A has: {'Cooking', 'Movies'}
