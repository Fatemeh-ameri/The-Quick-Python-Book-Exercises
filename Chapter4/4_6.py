"""Can you multiply a string by an integer, for example,
or can you multiply it by a float or complex number? Also load the math mod-
ule and try a few of the functions; then load the cmath module and do the
same. What happens if you try to use one of those functions on an integer or
float after loading the cmath module? How might you get the math module
functions back?"""

import math
import cmath

x = "Fatemeh"
y = 5
z = 1.5
f = 2+3j

y1 = math.exp(y)
print("y1 = ",y1)
#output: y1 =  148.4131591025766

y1 = cmath.exp(y)
print("y1 = ",y1)
#output: y1 =  (148.4131591025766+0j)

z1 = math.exp(z)
print("z1 = ",z1)
#output: z1 =  4.4816890703380645

z1 = cmath.exp(z)
print("z1 = ",z1)
#output: z1 =  (4.4816890703380645+0j)

#f1 = math.exp(f)
#print("f1 = ",f1)
#output: TypeError: must be real number, not complex

f1 = cmath.exp(f)
print("f1 = ",f1) 
#output: f1 =  (-7.315110094901103+1.0427436562359045j)

y2 = math.sqrt(y)
print("y2 = ",y2)
#output: y2 =  2.23606797749979

y2 = cmath.sqrt(y)
print("y2 = ",y2)
#output: y2 =  (2.23606797749979+0j)

z2 = math.sqrt(z)
print("z2 = ",z2)
#output: z2 =  1.224744871391589

z2 = cmath.sqrt(z)
print("z2 = ",z2) 
#output: z2 =  (1.224744871391589+0j)

#f2 = math.sqrt(f)
#print("f2 = ",f2)
#output: TypeError: must be real number, not complex

f2 = cmath.sqrt(f)
print("f2 = ",f2)
#output: f2 =  (1.6741492280355401+0.8959774761298381j)



print(x*y)
# output:FatemehFatemehFatemehFatemehFatemeh

print(x*z)
# output:TypeError: can't multiply sequence by non-int of type 'float'

print(x*f)
# output:TypeError: can't multiply sequence by non-int of type 'complex'

