"""QUICK CHECK: WHAT CAN BE A KEY? Decide which of the following expressions
can be a dictionary key: 1; 'bob'; ('tom', [1, 2, 3]); ["file-
name"]; "filename"; ("filename", "extension")"""

dic = {1: "one"}
print(dic)
#output: {1: 'one'}

dic = {'bob': 2}
print(dic)
#output: {'bob': 2}

dic = {('tom', [1, 2, 3]): 5}
print(dic)
#output: TypeError: unhashable type: 'list'

dic = {["file-name"]: 8}
print(dic)
#output: TypeError: unhashable type: 'list'

dic = {"filename": 1}
print(dic)
#output: {'filename': 1}

dic = {("filename", "extension"): 5}
print(dic)
#output: {('filename', 'extension'): 5}


