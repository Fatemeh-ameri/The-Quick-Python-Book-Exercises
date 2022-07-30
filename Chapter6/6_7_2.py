"""QUICK CHECK: FORMATTING STRING WITH 
What would be in the variable x
after the following snippets of code have executed?
QUICK CHECK: FORMATTING STRINGS WITH %
x = "%.2f" % 1.1111
x = "%(a).2f" % {'a':1.1111}
x = "%(a).08f" % {'a':1.1111}"""

x = "%.2f" % 1.1111
print(x)
#output: 1.11

x = "%(a).2f" % {'a':1.1111}
print(x)
#output: 1.11

x = "%(a).08f" % {'a':1.1111}
print(x)
#output: 1.11110000