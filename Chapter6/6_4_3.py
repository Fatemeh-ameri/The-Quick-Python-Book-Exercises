"""QUICK CHECK: STRIP If the string x equals "(name, date),\n", which of
the following would return a string containing "name, date"?
x.rstrip("),")
x.strip("),\n")
x.strip("\n)(,")"""

x = "(name, date),\n"

print(x.rstrip("),"))
#output:(name, date),


print(x.strip("),\n"))
#output:(name, date

print(x.strip("\n)(,"))
#output:name, date