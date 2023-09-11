# Task 1

# Pick your solution to one of the exercises in this module. 
# Design tests for this solution and write tests using unittest library. 

import unittest

def with_index(iterable, start=0):
    for item in iterable:
        yield start, item
        start += 1

class TestWithIndex(unittest.TestCase):

    def test_default_start(self):
        self.assertEqual(list(with_index(["a", "b", "c"])), [(0, "a"), (1, "b"), (2, "c")])

    def test_custom_start(self):
        self.assertEqual(list(with_index(["a", "b", "c"], start=1)), [(1, "a"), (2, "b"), (3, "c")])

    def test_string_iterable(self):
        self.assertEqual(list(with_index("abc", start=1)), [(1, "a"), (2, "b"), (3, "c")])

    def test_tuple_iterable(self):
        self.assertEqual(list(with_index(("a", "b", "c"), start=1)), [(1, "a"), (2, "b"), (3, "c")])

if __name__ == "__main__":
    unittest.main()
