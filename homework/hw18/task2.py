# Task 2

# Write tests for the Phonebook application, which you have implemented in module 1. 
# Design tests for this solution and write tests using unittest library

import unittest
from unittest.mock import patch
import os
import json
from phonebook import read_phonebook, add_entry, search_by_fname

class TestPhonebook(unittest.TestCase):

    def setUp(self):
        self.test_path = "test_contacts.json"
        self.sample_data = [
            {"fname": "John", "lname": "Doe", "number": "12345", "location": "NY"},
            {"fname": "Jane", "lname": "Doe", "number": "67890", "location": "LA"}
        ]
        with open(self.test_path, "w") as f:
            json.dump(self.sample_data, f)

    def test_read_phonebook(self):
        data = read_phonebook(self.test_path)
        self.assertEqual(data, self.sample_data)

    @patch("builtins.input", side_effect=["Mike", "Tyson", "112233", "LV"])
    def test_add_entry(self, mock_input):
        add_entry(self.test_path)
        with open(self.test_path, "r") as file:
            data = json.load(file)
            self.assertIn({"fname": "Mike", "lname": "Tyson", "number": "112233", "location": "LV"}, data)

    @patch("builtins.input", side_effect=["John"])
    def test_search_by_fname(self, mock_input):
        with patch("builtins.print") as mock_print:
            search_by_fname(self.test_path)
            mock_print.assert_called_with({"fname": "John", "lname": "Doe", "number": "12345", "location": "NY"})

    def tearDown(self):
        os.remove(self.test_path)

if __name__ == "__main__":
    unittest.main()
