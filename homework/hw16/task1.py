# Task 1

# Create a class method named `validate`, which should be called from the `__init__` 
# method to validate parameter email, passed to the constructor. The logic inside 
# the `validate` method could be to check if the passed email parameter is a valid email string.

import re

class EmailValidator:
    def __init__(self, email):
        if self.validate(email):
            self.email = email
            print(f"Valid email: {self.email}")
        else:
            print("Invalid email address")

    @staticmethod
    def validate(email):
        pattern = r"^[\w\.-]+@[\w\.-]+$"
        
        if re.match(pattern, email):
            return True
        else:
            return False
        

my_email = EmailValidator("@gmail.com")
# my_email.validate()
