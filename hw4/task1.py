# Write a Python program to get the largest number from a list of random numbers with the length of 10

# Constraints: use only while loop and random module to generate numbers

import random

numbers = []
i = 0
while i < 10:
    numbers.append(random.randint(1, 100))
    i += 1

largest_number = numbers[0]
i = 1
while i < len(numbers):
    if numbers[i] > largest_number:
        largest_number = numbers[i]
    i += 1

print("Generated numbers:", numbers)
print("Largest number:", largest_number)
