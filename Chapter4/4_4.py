""" TRY THIS:variables and expressions: Use parentheses to group the
numbers in different ways and see how the result changes compared with the
original ungrouped expression."""


#fatemeh ameri = 0
#print(fatemeh ameri)
#SyntaxError: invalid syntax
#in variable name should not be a space

#fatemeh-ameri = 0
#print(fatemeh-ameri)
#SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?

#fatemeh~ameri = 0
#print(fatemeh~ameri)
#SyntaxError: invalid syntax

x = 2 + 4 * 5 - 6 / 3
x1 = (2 + 4) * (5 - 6) / 3
x2 = (2 + 4) * (5- 6 / 3) 
print("x = ",x)
#output: x =  20.0
print("x1 = ",x1)
#output: x1 =  -2.0
print("x2 = ",x2)
#output: x2 =  18.0