# The Guessing Game.

# Write a program that generates a random number between 1 and 10 
# and lets the user guess what number was generated. 
# The result should be sent back to the user via a print statement.

import random

x = random.randint(1, 10)
print(x)

guess = int(input("Guess the number: "))
while guess != x:
    print("Try again!")
    guess = int(input("Guess the number: "))
else:
    print("Grats, you've won!")