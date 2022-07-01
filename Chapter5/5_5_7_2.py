"""TRY THIS: LIST OPERATIONS If you have a list x, write the code to safely remove
an item if—and only if—that value is in the list.
Modify that code to remove the element only if the item occurs in the list
more than once."""

x = [1,2,3,4,5,2]

if 1 in x:
    x.remove(1)

print(x)  
#output: [2,3,4,5,2]

if x.count(2)>1 : 
    while 2 in x :
        x.remove(2)
print(x)        


    