# # def make_pretty(func):

# #     def inner():
# #         print("I got decorated")
# #         func()
# #     return inner

# # @make_pretty
# # def ordinary():
# #     print("I am ordinary")

# # ordinary()  

# def smart_divide(func):
#     def inner(a, b):
#         print("I am going to divide", a, "and", b)
#         if b == 0:
#             print("Whoops! cannot divide")
#             return

#         return func(a, b)
#     return inner

# @smart_divide
# def divide(a, b):
#     print(a/b)

# divide(2,5)

# divide(2,0)

# # def check_type(func):
# #     def wrapper(arg):
# #         if not isinstance(arg, (int, float)):
# #             raise TypeError(f"Argument {arg} is not an integer or float.")
# #         return func(arg)
# #     return wrapper

# # @check_type
# # def double(arg):
# #     return arg * 2

# def check_limits(func):
#     calls = 0
#     def inner(a):
#         nonlocal calls  # declare calls as nonlocal
#         if calls >= 5:
#             print('You`ve got func many times')
#         else:
#             calls += 1
#             func(a)  # call the original function
#     return inner

# @check_limits
# def test(a):
#    print('Func called')

# test(2)
# test(2)
# test(2)
# test(2)
# test(2)
# test(2)
# test(2)
# test(2)

def check_type(func):
    def inner(a):
        if type(a) != int:
            print("It's not an int!")
        else:
            return a
    return inner

@check_type
def test(a):
    print(a)

test(2)