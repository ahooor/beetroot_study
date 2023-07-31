# Doggy age

# Create a class Dog with class attribute 'age_factor' equals to 7. 
# Make __init__() which takes values for a dog’s age. Then create a method 
# `human_age` which returns the dog’s age in human equivalent.

class Dog:
    age_factor = 7

    def __init__(self, age):
        self.age = age

    def human_age(self):
        h_age = self.age * Dog.age_factor
        print(f"In human's years the dog is {h_age}.")


d = Dog(3)
d.human_age()