# Task 1

# File Context Manager class

# Create your own class, which can behave like a built-in function "open". 
# Also, you need to extend its functionality with counter and logging. 
# Pay special attention to the implementation of "__exit__" method, 
# which has to cover all the requirements to context managers mentioned here:

# Context Manager Types 

# The with statement

class FileContextManager:
    def __init__(self, filename, mode="r"):
        self.filename = filename
        self.mode = mode
        self.file = None
        self.operation_count = 0

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        self.log("File opened.")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            self.log("File closed.")

        if exc_type:
            self.log(f"Exception of type {exc_type} occurred with value {exc_val}.")
        return False

    def log(self, message):
        print(f"[LOG]: {message}")
        self.operation_count += 1

with FileContextManager("sample.txt", "w") as file:
    file.write("Hello, World!")
    print("Inside with block, file written.")
