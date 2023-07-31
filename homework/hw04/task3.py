# Words combination

# Create a program that reads an input string and then creates 
# and prints 5 random strings from characters of the input string.

import random

text = input("Enter your text here: ")

chars = [char for char in text]

for i in range(5):
    random.shuffle(chars)
    print("".join(chars))

