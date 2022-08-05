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
        print(name, "is", dict[key], "years old")

"""Please enter first_name:
fatemeh
Please enter age:
26
Please enter first_name:
zeynab
Please enter age:
24
Please enter first_name:
zahra
Please enter age:
20
Please enter one of the previous name:
zahra
zahra is 20 years old"""