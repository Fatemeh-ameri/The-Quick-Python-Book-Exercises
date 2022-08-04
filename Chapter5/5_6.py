"""TRY THIS: LIST COPIES Suppose that you have the following list: x = [[1, 2,
3], [4, 5, 6], [7, 8, 9]] What code could you use to get a copy y of
that list in which you could change the elements without the side effect of
changing the contents of x?"""

import copy

x = [[1, 2,3], [4, 5, 6], [7, 8, 9]]
deep = copy.deepcopy(x)
deep[0][0] = 0
print(deep)
#output: [[0, 2, 3], [4, 5, 6], [7, 8, 9]]

print(x)
#output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

"""y = x[:]
y[0][0] = 0
print(y)
#output: [[0, 2, 3], [4, 5, 6], [7, 8, 9]]"""