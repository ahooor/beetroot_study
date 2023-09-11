# Task 2

# Create your own implementation of a built-in function range, named in_range(), 
# which takes three parameters: 'start', 'end', and optional step. Tips: See the documentation for 'range' function

def in_range(start, end=None, step=1):
    if end is None:
        start, end = 0, start

    if step == 0:
        raise ValueError("A step must not be zero")

    if step > 0:
        while start < end:
            yield start
            start += step
    else:
        while start > end:
            yield start
            start += step

for i in in_range(3):
    print(i)

print("\n")

for i in in_range(1, 8):
    print(i)

print("\n")

for i in in_range(1, 12, 4):
    print(i)

print("\n")

for i in in_range(1, 12, 0):
    print(i)