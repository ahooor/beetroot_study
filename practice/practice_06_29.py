# Calculator

try:
    a = input("Enter your first number: ")
    b = input("Enter your second number: ")
    while a != "q" and b != "q":
        c = input("Choose your operation (+, -, *, /): ")
        a = int(a)
        b = int(b)
        if c == "+":
            print(a + b)
            break
        if c == "-":
            print(a - b)
            break
        if c == "*":
            print(a * b)
            break
        if c == "/":
            print(a / b)
            break
    else:
        pass
except ZeroDivisionError:
    print("You cannot divide by zero!")

