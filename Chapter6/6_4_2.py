"""QUICK CHECK: STRINGS TO NUMBERS
Which of the following will not be con-
verted to numbers, and why?
int('a1')
int('12G', 16)
float("12345678901234567890")
int("12*2")"""

print(int('a1'))
#output: ValueError: invalid literal for int() with base 10: 'a1'

print(int('12G', 16))
#output: ValueError: invalid literal for int() with base 16: '12G'

print(float("12345678901234567890"))
#output: 1.2345678901234567e+19

print(int("12*2"))
#output: ValueError: invalid literal for int() with base 10: '12*2'