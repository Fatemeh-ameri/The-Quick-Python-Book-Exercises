"""TRY THIS: CREATE A DICTIONARY Write the code to ask the user for three
names and three ages. After the names and ages are entered, ask the user for
one of the names, and print the correct age."""

dict = {}
for i in range(3):
    first_name = input("Please enter first_name:\n")
    age = int(input("Please enter age:\n"))
    dict[first_name] = age

name = input("Please enter one of the previous name:\n")  
for key in dict:
    if name==key:
        print(name, "is", dict[key], "years old.")