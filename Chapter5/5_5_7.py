"""QUICK CHECK: LIST OPERATIONS
What would be the result of len([[1,2]] * 3)?
What are two differences between using the in operator and a list’s index()
method?
Which of the following will raise an exception?: min(["a", "b”, "c"]);
max([1, 2, "three"]); [1, 2, 3].count("one")"""

x = [[1,2]] * 3
print(x)
#output: [[1, 2], [1, 2], [1, 2]]

x1 = [1,2,3,4,5]
print(x1.index(2))
#output: 1

print(2 in x1)
#output: True

print(min(["a", "b", "c"]))
#output: a

print([1, 2, 3].count("one"))

print(max([1, 2, "three"]))
"""output: Traceback (most recent call last):
  File "/media/fatemeh/HDD/CS/Git/The-Quick-Python-Book-Exercises/Chapter5/5_5_7.py", line 22, in <module>
    print(max([1, 2, "three"]))
TypeError: '>' not supported between instances of 'str' and 'int'"""