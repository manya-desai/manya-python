Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> year = int(input("Enter a year:"))
Enter a year:2027
>>> if(year % 400 == 0) or (year % 4 == 0 and year % 100 !=0):
...     print("LEAP YEAR")
... else:
...     print("NOT A LEAP YEAR")
... 
...     
NOT A LEAP YEAR
>>> import math
>>> print("Value of PI =",math.pi)
Value of PI = 3.141592653589793
>>> PI = 3.14
>>> print("Constant value of PI =",PI)
Constant value of PI = 3.14
