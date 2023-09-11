# Task 1

# Create your own implementation of a built-in function enumerate, named 
# 'with_index', which takes two parameters: 'iterable' and 'start', default is 0. 
# Tips: see the documentation for the enumerate function

def with_index(iterable, start=0):
    for item in iterable:
        yield start, item
        start += 1


for index, value in with_index(["a", "b", "c", "d", "e"], start=1):
    print(index, value)
