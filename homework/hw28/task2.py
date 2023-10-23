# Write a program that reads in a sequence of characters, 
# and determines whether it's parentheses, braces, and curly brackets are "balanced."


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

def are_brackets_balanced(input_string):
    stack = Stack()
    opening_brackets = "([{"
    closing_brackets = ")]}"
    
    for char in input_string:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty():
                return False
            
            top = stack.pop()
            if (char == ')' and top != '(') or (char == ']' and top != '[') or (char == '}' and top != '{'):
                return False
    
    return stack.is_empty()

if __name__ == "__main__":
    input_string = input("Enter a sequence of characters: ")
    if are_brackets_balanced(input_string):
        print("Brackets are balanced.")
    else:
        print("Brackets are not balanced.")
