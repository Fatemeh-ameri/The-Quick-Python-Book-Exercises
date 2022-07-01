"""QUICK CHECK: TUPLES Explain why the following operations aren’t legal for
the tuple x = (1, 2, 3, 4):
x.append(1)
x[1] = "hello"
del x[2]
If you had a tuple x = (3, 1, 4, 2), how might you end up with x sorted?"""

x = (1, 2, 3, 4)

#x.append(1)
"""output: Traceback (most recent call last):
  File "/media/fatemeh/HDD/CS/Git/The-Quick-Python-Book-Exercises/Chapter5/5_7_4.py", line 9, in <module>
    x.append(1)
AttributeError: 'tuple' object has no attribute 'append'"""

#x[1] = "hello"
"""Traceback (most recent call last):
  File "/media/fatemeh/HDD/CS/Git/The-Quick-Python-Book-Exercises/Chapter5/5_7_4.py", line 16, in <module>
    x[1] = "hello"
TypeError: 'tuple' object does not support item assignment"""

#del x[2]
"""Traceback (most recent call last):
  File "/media/fatemeh/HDD/CS/Git/The-Quick-Python-Book-Exercises/Chapter5/5_7_4.py", line 22, in <module>
    del x[2]
TypeError: 'tuple' object doesn't support item deletion"""

x = (3, 1, 4, 2)
print(tuple(sorted(x)))
#output: (1, 2, 3, 4)

