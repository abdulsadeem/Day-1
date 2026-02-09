Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#list example
numbers =[10,20,30]
#tuple example
coordinates=(5,10)
print(numbers)
[10, 20, 30]
print(coordinates)
(5, 10)
#########################
#slicing and indexing
a =[100,200,300,400,500]
a[-3:-1]
[300, 400]
a[1:4]
[200, 300, 400]
#skip
>>> a[1:4:2]
[200, 400]
>>> a[1:4:1]
[200, 300, 400]
>>> a=[1,2,3,4,5,6,7,8,9]
>>> a[1:4:3]
[2]
>>> a[1:9:3]
[2, 5, 8]
>>> a[-8:-2:2]
[2, 4, 6]
>>> ###################################
>>> #list method and mutability
>>> 
>>> marks=[85,43,56,70,30,50]
>>> marks.append(90)
>>> print(marks)
[85, 43, 56, 70, 30, 50, 90]
>>> marks.pop
<built-in method pop of list object at 0x000001BBDDC9FC40>
>>> marks.pop()
90
>>> print(marks)
[85, 43, 56, 70, 30, 50]
>>> marks.reverse()
>>> print(marks)
[50, 30, 70, 56, 43, 85]
>>> marks.sort()
>>> print(marks)
[30, 43, 50, 56, 70, 85]
>>> marks.reverse()
>>> print(marks)
[85, 70, 56, 50, 43, 30]
>>> marks.extend([90])
>>> print(marks)
[85, 70, 56, 50, 43, 30, 90]
>>> marks.insert(60,5)
>>> print(marks)
[85, 70, 56, 50, 43, 30, 90, 5]
