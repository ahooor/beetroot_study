# Make a program that has your name and the current day of the week 
# stored as separate variables and then prints a message like this:

#      "Good day <name>! <day> is a perfect day to learn some python."
# Note that  <name> and <day> are predefined variables in source code.

# An additional bonus will be to use different string formatting methods for constructing result string.

# 1 option

print("\n")

print("Good day, {name}! {day} is a perfect day to learn some python.".format(name = "Alisiya", day = "Thursday"))

# 2 option

print("\n")

name = "Alisiya"
from datetime import date
today = date.today()

print(f"Good day, {name}! {today} is a perfect day to learn some python.")

print("\n")