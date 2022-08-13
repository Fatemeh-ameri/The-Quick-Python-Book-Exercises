"""TRY THIS: COMPREHENSIONS What list comprehension would you use to process the list
x so that all negative values are removed?
Create a generator that returns only odd numbers from 1 to 100. (Hint: A
number is odd if there is a remainder if divided by 2; use % 2 to get the
remainder of division by 2.)
Write the code to create a dictionary of the numbers and their cubes from 11
through 15."""

"""x = [1, 3, 5, 0, -1, 3, -2]
x_remove = [ x.remove(i) for i in x if i < 0]
print(x)"""
#output: [1, 3, 5, 0, 3]

"""for i in range(1,101):
    if i % 2 != 0:
        print(i)"""
#output: 1 3 5 7

cubs = {i: i**3 for i in range(11,16)}
print(cubs)
#output: {11: 1331, 12: 1728, 13: 2197, 14: 2744, 15: 3375}

