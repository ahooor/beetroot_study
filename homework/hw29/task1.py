# Implement append, index, pop, insert methods for UnsortedList. Also implement a slice method, 
# which will take two parameters 'start' and 'stop', and return a copy of the list starting 
# at the position and going up to but not including the stop position.


class UnsortedList:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)

    def index(self, item):
        try:
            return self.items.index(item)
        except ValueError:
            return -1 

    def pop(self, index=-1):
        return self.items.pop(index)

    def insert(self, index, item):
        self.items.insert(index, item)

    def slice(self, start, stop):
        return self.items[start:stop]

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    my_list = UnsortedList()

    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)
    my_list.append(5)

    print(my_list)

    index = my_list.index(3)
    print(index)

    popped_item = my_list.pop()
    print(popped_item)

    my_list.insert(1, 6)
    print(my_list)

    sliced_list = my_list.slice(1, 4)
    print(sliced_list)
