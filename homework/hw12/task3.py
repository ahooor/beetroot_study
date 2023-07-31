# Write a decorator "arg_rules" that validates arguments passed to the function.
# A decorator should take 3 arguments:

# max_length: 15
# type_: str
# contains: [] - list of symbols that an argument should contain

# If some of the rules' checks returns False, the function should return False and print the reason it failed; 
# otherwise, return the result.


def arg_rules(type: type, max_length: int, contains: list):
    def decorator(func):
        def inner(arg):
            if not isinstance(arg, type):
                print("The argument is not of the expected type.")
                return False
            if len(arg) > max_length:
                print("The argument is too long.")
                return False
            if not all(e in arg for e in contains):
                print("The argument doesn't contain all required characters.")
                return False
            return func(arg)
        return inner
    return decorator


@arg_rules(type=str, max_length=15, contains=["05", "@"])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
