# Task 2

# Writing tests for context manager

# Take your implementation of the context manager class from Task 1 and write tests for it. 
# Try to cover as many use cases as you can, positive ones when a file exists and everything works as designed. 
# And also, write tests when your class raises errors or you have errors in the runtime context suite.

import unittest
import os

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


class TestFileContextManager(unittest.TestCase):

    def setUp(self):
        self.filename = "test_sample.txt"

    def test_file_write(self):
        with FileContextManager(self.filename, "w") as file:
            file.write("Test content")
        with open(self.filename, "r") as file:
            content = file.read()
        self.assertEqual(content, "Test content")

    def test_file_read(self):
        with open(self.filename, "w") as file:
            file.write("Test content")
        with FileContextManager(self.filename, "r") as file:
            content = file.read()
        self.assertEqual(content, "Test content")

    def test_exception_propagation(self):
        with self.assertRaises(ValueError):
            with FileContextManager(self.filename, "w") as file:
                raise ValueError("Test exception")

    def test_non_existent_file_read(self):
        with self.assertRaises(FileNotFoundError):
            with FileContextManager("non_existent.txt", "r") as file:
                pass

    def test_operation_count(self):
        with FileContextManager(self.filename, "w") as file:
            file.write("Test")
        self.assertEqual(file.operation_count, 2)

    def test_log_output(self):
        with FileContextManager(self.filename, "w") as file:
            file.write("Test")

if __name__ == "__main__":
    unittest.main()
