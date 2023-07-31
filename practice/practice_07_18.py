# Exercise 1: Building a Bank Account System
# Implement a BankAccount class that represents a bank account. 
# It should have private attributes like account number and balance, 
# and public methods for depositing, withdrawing, and getting the account balance.

# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.balance = balance

#     def deposit(self, sum):
#         self.balance = self.balance + sum
#         print(self.balance)

#     def withdraw(self, sum):
#         self.balance = self.balance - sum
#         print(self.balance)

#     def check_balance(self):
#         print(self.balance)


# my_account = BankAccount(123456789, 3000)
# my_account.deposit(500)
# my_account.withdraw(1000)
# my_account.check_balance()


# Exercise 2: Creating a Student Class
# Implement a Student class that represents a student. It should have public attributes 
# like name and grade, and a private attribute for storing the student's ID. Use protected 
# attributes to store a list of courses taken by the student.

# class Student:
#     def __init__(self, name, grade, student_id, courses: list):
#         self.name = name
#         self.grade = grade
#         self.__student_id = student_id
#         self._courses = courses

#     def list_courses(self):
#         print(self._courses)


# my_courses = ["Math", "Computer Science", "Programming", "Statistics"]
# student1 = Student("Petro Fedun", "A", 48920849, my_courses)
# student1.list_courses()


# Exercise 3: Social Media Post
# Create a class Post that represents a social media post. 
# The post should have attributes like content, author, and number of likes. 
# Use private access modifiers for the number of likes and provide methods to like and display the post.

# class Post:
#     def __init__(self, content, author, likes: int):
#         self.content = content
#         self.author = author
#         self.__likes = likes

#     def like(self):
#         self.__likes = self.__likes + 1 
#         print(self.__likes)

#     def display(self):
#         print(f"Check out the article '{self.content}' by {self.author}")


# my_post = Post("5 methods to remove bad breath smell! You will be shocked!", "pipka228", 12)
# my_post.like()
# my_post.display()


# Exercise 4: Managing Employees
# Implement an Employee class that represents an employee in a company. 
# Each employee should have attributes like name, department, manager, skills, 
# English level and salary. English level field should be protected and 
# salary field should be private. Create a Department class that contains employees 
# and methods for adding and removing employees, as well as calculating the average salary for the department.

# class Employee:
#     def __init__(self, name, department, manager, skills, eng_lvl, salary):
#         self.name = name
#         self.department = department
#         self.manager = manager
#         self.skills = skills
#         self._eng_lvl = eng_lvl
#         self.__salary = salary

#     def get_info(self):
#         print(f"Name: {self.name}, Department: {self.department}, Manager: {self.manager}, Skills: {self.skills}, Eng Lvl: {self._eng_lvl}, Salary: {self.__salary}")

#     def get_salary(self):
#         return self.__salary
        

# class Department:
#     def __init__ (self, name, employees: list):
#         self.name = name
#         self.employees = employees

#     def hire(self, employee):
#         self.employees.append(employee)
#         print("A new employee has been hired")
#         print(self.employees)

#     def fire(self, employee):
#         self.employees.remove(employee)
#         print("An employee has been fired")
#         print(self.employees)

#     def view_employees(self):
#         for employee in self.employees:
#             employee.get_info()

#     def average(self):
#         salaries = 0
#         for employee in self.employees:
#             salaries = salaries + employee.get_salary()
#         print(salaries)
#         avrg = salaries // len(self.employees)
#         print(avrg)
        

# empl1 = Employee("Petro Fedun", "IT", "Iryna Zaiets", "programming, bungee jumping, cooking", "C2", 5000)
# empl2 = Employee("Alisiya Horbenko", "IT", "Iryna Zaiets", "business analysis, sky diving, gaming", "C2", 5000)
# empl3 = Employee("Oleksandr Horbenko", "IT", "Iryna Zaiets", "programming, dancing, painting", "C2", 15000)

# employees = [empl1, empl2, empl3]

# it_dept = Department("IT", employees)
# it_dept.hire(empl2)
# it_dept.fire(empl2)
# it_dept.view_employees()
# it_dept.average()


# Exercise 5: Movie Database
# Create a Movie class that represents a movie in a movie database. 
# The class should have various fields to store information about the movie, 
# such as its title, director, genre, release year, duration, and ratings. 
# Use public, private, and protected access modifiers appropriately. 
# Implement methods to update movie details, calculate average ratings, and display movie information.

# class Movie:
#     def __init__(self, title, director, genre, year, dur, rate):
#         self.title = title
#         self.director = director
#         self.genre = genre
#         self.year = year
#         self.dur = dur
#         self.rate = rate

#     def display_info(self):
#         print(f"Title: {self.title}, director: {self.director}, genre: {self.genre}, year: {self.year}, duration: {self.dur}, rating: {self.rate}")

#     def update_info(self, title, director, genre, year, dur, rate):
#         self.title = title
#         self.director = director
#         self.genre = genre
#         self.year = year
#         self.dur = dur
#         self.rate = rate
#         print(f"Title: {self.title}, director: {self.director}, genre: {self.genre}, year: {self.year}, duration: {self.dur}, rating: {self.rate}")

#     def get_rate(self):
#         return self.rate

# my_movie = Movie("Titanic", "Cameron", "Drama", 1997, "2:45", 9)
# # my_movie.display_info()
# # my_movie.update_info("Titanic", "Petro Cameron", "Drama", 1997, "2:48", 9)

# mov1 = Movie("Great Gatsby", "Lurmann", "Drama", 2013, "2:32", 8)
# mov2 = Movie("Barbie", "Del Toro", "Comedy", 2023, "1:48", 7)

# movie_list = [my_movie, mov1, mov2]

# def average_rate(list):
#     ratings = []
#     for movie in list:
#         ratings.append(movie.get_rate())
#     print(ratings)
#     avrg = sum(ratings) / len(ratings)
#     print(avrg)

# average_rate(movie_list)

# Exercise 6: Fitness Tracker
# Create a FitnessTracker class that represents a fitness tracking application. 
# The class should have various fields to store information about user activities, 
# such as the user's name, age, weight, height, daily step count, and total calories burned. 
# Use public, private, and protected access modifiers appropriately. 
# Implement methods to log daily activities, calculate daily calorie burn, and display user information.

# class FitnessTracker:
#     def __init__(self, name, age, weight, height, steps):
#         self.name = name
#         self.__age = age
#         self._weight = weight
#         self._height = height
#         self.steps = steps

#     def display_info(self):
#         print(f"Name: {self.name}. Age: {self.__age}. Weight: {self._weight}. Height: {self._height}. Steps: {self.steps}.")

#     def add_steps(self, new_steps):
#         self.steps = self.steps + new_steps
#         print(f"Your daily steps have been increased by {new_steps} and now it's {self.steps}!")

#     def calorie_calc(self):
#         calories = self.steps / 1000 * 40
#         print(calories)


# my_tracker = FitnessTracker("Alisiya", 23, 60, 174, 10000)
# my_tracker.display_info()
# my_tracker.add_steps(2000)
# my_tracker.calorie_calc()

# Exercise 7: Flight Booking System
# Create a Flight class that represents a flight in a booking system. 
# The class should have various fields to store information about the flight, 
# such as flight number, departure city, destination city, departure time, and available seats. 
# Use public, private, and protected access modifiers appropriately. 
# Implement methods to book seats, check seat availability, calculate flight duration, and display flight information.

class Flight:
    def __init__(self, number, dep_city, dest_city, dep_time, seats):
        self.number = number
        self.dep_city = dep_city
        self.dest_city = dest_city
        self.dep_time = dep_time
        self.seats = seats

    def display_info(self):
        print(f"Flight number: {self.number}. \nDeparture city: {self.dep_city}. \nDestination city: {self.dest_city}. \nDeparture time: {self.dep_time}. \nSeats available: {self.seats}.")

my_flight = Flight("185H29A", "Odesa", "New York", "18:45", 12)
my_flight.display_info()
