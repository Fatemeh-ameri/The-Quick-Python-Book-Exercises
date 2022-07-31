"""QUICK CHECK: MODIFYING STRINGS What would be a quick way to change all
punctuation in a string to spaces?"""

import string


x = "I am fateme, I am 26 years old! Am I married? yes."
x2 = x.maketrans(string.punctuation, " " *len(string.punctuation))
x3 = x.translate(x2)

print(x3)
#output: I am fateme  I am 26 years old  Am I married  yes 