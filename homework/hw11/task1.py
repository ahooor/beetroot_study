# Write a Python program to detect the number of local variables declared in a function.

def count_vars(vars):
    number = len(vars)
    print(number)

def greetings():
    name = "Alisiya"
    surname = "Horbenko"
    age = "23"

    print(f"Hello, {name} {surname}! So you are {age} now?")
    vars = locals()
    return vars


greetings_vars = greetings()
count_vars(greetings_vars)
