# task 1

# class Stack :
#     def __init__(self):
#         self.items = []

#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         return self.items.pop()

#     def is_empty(self):
#         return (self.items == [])
    

# my_stack = Stack()
# my_stack.push("a")
# my_stack.push("b")
# my_stack.push("c")

# print(my_stack.pop())

# task 2, 3

# class Queue:

#     def __init__(self):
#         self.queue = []

#     def enqueue(self, task):
#         self.queue.append(task)

#     def dequeue(self):
#         if len(self.queue) < 1:
#             return None
#         return self.queue.pop(0)

#     def size(self):
#         return len(self.queue)
    

# t1 = ("Andriy Zavora", "Morning exercise")
# t2 = ("Alisiya Horbenko", "Wash the dishes")

# my_queue = Queue()
# my_queue.enqueue(t1)
# my_queue.enqueue(t2)
# print(my_queue.size())
# print(my_queue.dequeue())


# my_queue = Queue()
# my_queue.enqueue("apple")
# my_queue.enqueue("banana")
# my_queue.enqueue("orange")

# print(my_queue.dequeue())

# task 4

# 4. Напишіть функцію, яка використовує стек для обертання рядка задом наперед.

# class Stack:
#     def __init__(self):
#         self.items = []

#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         return self.items.pop()

#     def is_empty(self):
#         return (self.items == [])
    

# my_stack = Stack()
# my_str = "Python"

# for c in my_str:
#     my_stack.push(c)
    
# for c in my_str:
#     print(my_stack.pop())

# task 5

# 5. Створіть чергу, в якій декілька елементів знаходяться в черзі. Виведіть їх у порядку їх видалення з черги

class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)
    

my_queue = Queue()
my_queue.enqueue("a")
my_queue.enqueue("b")
my_queue.enqueue("c")

while my_queue.size() != 0:
    print(my_queue.dequeue())


# for item in (0, my_queue.size()):
#     print(my_queue.dequeue())





