# Create a function called make_operation, which takes in a simple arithmetic operator 
# as a first parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) 
# and an arbitrary number of arguments (only numbers) as the second parameter. 
# Then return the sum or product of all the numbers in the arbitrary parameter. 
# For example:

# the call make_operation(‘+’, 7, 7, 2) should return 16
# the call make_operation(‘-’, 5, 5, -10, -20) should return 30
# the call make_operation(‘*’, 7, 6) should return 42

def make_operation(operator, *numbers):
    answer = numbers[0]
    for num in numbers[1:]:
        if operator == "+": 
            answer += int(num)
        elif operator == "-":
            answer -= int(num)
        elif operator == "*":
            answer *= int(num)
    return answer

answer = make_operation("-", 5, 7, 3, 8)
print(answer)