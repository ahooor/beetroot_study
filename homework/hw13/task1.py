# A Person class

# Make a class called Person. Make the __init__() method take firstname, 
# lastname, and age as parameters and add them as attributes. Make another method 
# called talk() which makes prints a greeting from the person containing, 
# for example like this: "Hello, my name is Carl Johnson and I’m 26 years old".

class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def talk(self):
        print(f"Hello! My name is {self.fname} {self.lname} and I am {self.age} years old.")


p = Person("Harry", "Potter", 11)
p.talk()