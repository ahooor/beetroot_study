# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!

# For example:

def logger(func):
    def inner(*args):
        print(func.__name__, args)
        return func(*args)
    return inner
 
@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(5, 8)
square_all(5, 6, 7 ,8)
