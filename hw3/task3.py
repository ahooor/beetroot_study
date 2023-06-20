# Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong, 
# and then responds with a message accordingly.

expression = "2+2*2"
answer = int(input(f"{expression}=? "))

expression = 2+2*2

if answer == int(expression):
    print("The answer is correct.")
else:
    print("Your answer is incorrect.")