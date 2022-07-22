"""TRY THIS: STRING OPERATIONS Suppose that you have a list of strings in which
some (but not necessarily all) of the strings begin and end with the double
quote character:
x = ['"abc"', 'def', '"ghi"', '"klm"', 'nop']Converting from objects to strings
What code would you use on each element to remove just the double quotes?
What code could you use to find the position of the last p in Mississippi?
When you’ve found that position, what code would you use to remove just
that letter?"""

x = ['"abc"', 'def', '"ghi"', '"klm"', 'nop']
for i in range(len(x)):
    if '"' in x[i]:
        x[i] = x[i].strip('"')  
print(x)
#output: ['abc', 'def', 'ghi', 'klm', 'nop']

y = "Mississippi"
print(y.rindex("p"))
#output: 9

y1 = y.rfind("p")
print(y[:y1] + y[y1+1:])
#output: Mississipi