# Write a function that takes in two numbers from the user via input(), 
# call the numbers a and b, and then returns the value of squared a divided by b, 
# construct a try-except block which raises an exception if the two values given by the input function 
# were not numbers, and if value b was zero (cannot divide by zero).  

def calculate():
    try:
        a = int(input("Enter the first number (a): "))
        b = int(input("Enter the second number (b): "))
        result = (a ** 2) // b
        print(result)
    except ValueError:
        raise ValueError("Invalid input. Please enter numeric values for a and b.")
    except ZeroDivisionError:
        raise ZeroDivisionError("Division by zero is not allowed.")
    
calculate()