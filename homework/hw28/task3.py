# Extend the Stack to include a method called get_from_stack that searches and 
# returns an element e from a stack. Any other element must remain on the stack 
# respecting their order. Consider the case in which the element is not found - raise ValueError with proper info Message


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def get_from_stack(self, element):
        found = False
        temp_stack = Stack()
        
        while not self.is_empty():
            item = self.pop()
            if item == element:
                found = True
                break
            temp_stack.push(item)

        while not temp_stack.is_empty():
            self.push(temp_stack.pop())

        if found:
            return element
        else:
            raise ValueError(f"Element '{element}' not found in the stack")

if __name__ == "__main__":
    stack = Stack()
    
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    try:
        element = stack.get_from_stack(3)
        print(f"Element found: {element}")
    except ValueError as e:
        print(e)

    try:
        element = stack.get_from_stack(5) 
        print(f"Element found: {element}")
    except ValueError as e:
        print(e)
