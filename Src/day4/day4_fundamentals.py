Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a={"key":"value"}
>>> print(a)
{'key': 'value'}
>>> student = {"name":"Amit"}
>>> student = {"name":"Amar",
...            "age":"22",
...            "course":"Engineering"}
>>> print(student["name"])
Amar
>>> student["age"]=22
>>> student["city"]="Delhi"
>>> print(student)
{'name': 'Amar', 'age': 22, 'course': 'Engineering', 'city': 'Delhi'}
>>> ##################
>>> #met&iter
>>> marks={"math":80,"Science":75,"English":85}
>>> print(marks.get("math"))
80
>>> print(marks.get("history",0))
0
>>> for subject score in marks.item():
...     
SyntaxError: invalid syntax
>>> for subject,score in marks.item():
...     print(subject,score)
... 
...     
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    for subject,score in marks.item():
AttributeError: 'dict' object has no attribute 'item'. Did you mean: 'items'?
>>> for subject,score in marks.items():
...     print(subject,score)
... 
...     
math 80
Science 75
English 85
