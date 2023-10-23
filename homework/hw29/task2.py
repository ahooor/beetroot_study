# Implement a stack using a singly linked list.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        else:
            popped = self.top
            self.top = self.top.next
            return popped.data

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.top.data

    def __str__(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            current = self.top
            stack_str = ""
            while current:
                stack_str += str(current.data) + " -> "
                current = current.next
            return stack_str[:-4]

if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Stack:", stack)
    print("Top element:", stack.peek())

    popped = stack.pop()
    print("Popped element:", popped)
    print("Stack after pop:", stack)
