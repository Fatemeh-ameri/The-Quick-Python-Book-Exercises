"""QUICK CHECK: SPLIT AND JOIN How could you use split and join to change
all the whitespace in string x to dashes, such as changing "this is a test"
to "this-is-a-test"?"""

x = "this is a test"
y = x.split()
print(y)
#output: ['this', 'is', 'a', 'test']

z = "-".join(y)
print(z)
#output: this-is-a-test