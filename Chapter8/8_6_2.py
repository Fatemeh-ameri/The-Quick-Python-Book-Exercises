"""QUICK CHECK: BOOLEANS AND TRUTHINESS Decide whether the following state-
ments are true or false: 1, 0, -1, [0], 1 and 0, 1 > 0 or []."""

"""Python bool() function is used to return or convert a value to a Boolean value i.e.,
 True or False, using the standard truth testing procedure"""
 
print(bool(1))
#output: True

print(bool(0))
#output: False

print(bool(-1))
#output: True

print(bool([0]))
#output: True

print(bool(1 and 0))
#output: False

print(bool(1 and 0))
#output: False

print(bool(1 > 0 or []))
#output: True
