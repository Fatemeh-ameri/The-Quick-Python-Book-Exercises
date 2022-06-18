"""Experiment with the input() function to get string
and integer input. Using code similar to the previous code, what is the effect
of not using int() around the call to input()for integer input? Can you
modify that code to accept a float—say, 28.5? What happens if you deliber-
ately enter the wrong type of value? Examples include a float in which an inte-
ger is expected and a string in which a number is expected—and vice versa."""

x = input("What is your name? ")
print(x)
#output: What is your name? fatemeh
#fatemeh

y = int(input("How old are you? "))
print(y)
#output: How old are you? 25
#25
#if the type of input is float the output will be: ValueError: invalid literal for int() with base 10: '25.5'

z = float(input("What is your weight? "))
print(z)
#output: What is your weight? 50
#50