Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = 10
print(type(a))
<class 'int'>
a =20.5
print(type(a))
<class 'float'>
a = 1j
print(type(a))
<class 'complex'>
a = ["apple","banana","cherry"]
print(type(a))
<class 'list'>
a = ("apple","banana","cherry")
print(type(a))
<class 'tuple'>
a = "hello wolrd"
>>> print(type(a))
<class 'str'>
>>> a = range(6)
>>> print(type(a))
<class 'range'>
>>> a = {"name":"john" , "age":"19"}
>>> print(type(a))
<class 'dict'>
>>> a = {"apple","banana","cherry"}
>>> print(type(a))
<class 'set'>
>>> a = frozenset ({"apple","banana","cherry"})
>>> print(type(a))
<class 'frozenset'>
>>> a = true
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a = true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> a = True
>>> print(type(a))
<class 'bool'>
>>> a = b"hello"
>>> print(type(a))
<class 'bytes'>
>>> a = bytearray(4)
>>> print(type(a))
<class 'bytearray'>
>>> a = memoryview (bytes(5))
>>> print(type(a))
<class 'memoryview'>
>>> a = None
>>> print(type(a))
<class 'NoneType'>
