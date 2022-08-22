"""QUICK CHECK: THE FORMAT() METHOD
What will be in x when the following
snippets of code are executed?:
x = "{1:{0}}".format(3, 4)
x = "{0:$>5}".format(3)
x = "{a:{b}}".format(a=1, b=5)
x = "{a:{b}}:{0:$>5}".format(3, 4, a=1, b=5, c=10)"""

x = "{1:{0}}".format(3,4)
print(x)
#output: 4

x = "{0:$>5}".format(345)
print(x)
#output:$$345

x = "{a:{b}}".format(a=1, b=5)
print(x)
#output:    1

x = "{a:{b}}:{0:$>5}".format(3, 4, a=1, b=5, c=10)
print(x)
#output:    1:$$$$3





