# Task 3

# Create your own implementation of an iterable, which could be used inside for-in loop. 
# Also, add logic for retrieving elements using square brackets syntax.

class CustomIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        raise StopIteration

    def __getitem__(self, key):
        return self.data[key]

data = CustomIterable([1, 2, 3, 5, 6, 7, 8])

for item in data:
    print(item)

print("\n")

print(data[6])
