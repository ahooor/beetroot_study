# Make a list that contains all integers from 1 to 100, then find all integers from the list 
# that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.

# Constraint: use only while loop for iteration

numbers = list(range(1, 101))

result_list = []
i = 0
while i < len(numbers):
    if numbers[i] % 7 == 0 and numbers[i] % 5 != 0:
        result_list.append(numbers[i])
    i += 1

print(result_list)
