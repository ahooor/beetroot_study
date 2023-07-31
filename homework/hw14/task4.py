# Custom exception

# Create your custom exception named 'CustomException', you can inherit from base 
# Exception class, but extend its functionality to log every error message to a file 
# named 'logs.txt'. Tips: Use __init__ method to extend functionality for saving messages to file


class CustomException(Exception):
    def __init__(self, msg):
        with open("/Users/alisiyanosenko/Python/beetroot_study/homework/hw14/logs.txt", "a") as log_file:
            log_file.write(f"{msg}\n")
        super().__init__(msg)

a = 2
b = 0

try:
    a // b
except ZeroDivisionError as err:
    CustomException(err)

my_list = ["a", "b", "c"]

try:
    print(my_list[5])
except IndexError as err:
    CustomException(err)