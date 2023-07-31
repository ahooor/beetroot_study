# School

# Make a class structure in python representing people at school. 
# Make a base class called Person, a class called Student, and another one called Teacher. 
# Try to find as many methods and attributes as you can which belong to different classes, 
# and keep in mind which are common and which are not. For example, the name should be a 
# Person attribute, while salary should only be available to the teacher. 


class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def display_info(self):
        print(f"\nName: {self.fname} \nSurname: {self.lname} \nAge: {self.age}\n")


class Student(Person):
    def __init__(self, fname, lname, age, grade, classroom):
        super().__init__(fname, lname, age)
        self.grade = grade
        self.classroom = classroom
    
    def student_info(self):
        print(f"\nName: {self.fname} \nSurname: {self.lname} \nAge: {self.age} \nGrade: {self.grade} \nClassroom: {self.classroom}\n")

    def study(self):
        print(f"{self.fname} is studying.")


class Teacher(Person):
    def __init__(self, fname, lname, age, subject, salary):
        super().__init__(fname, lname, age)
        self.subject = subject
        self.salary = salary

    def teacher_info(self):
        print(f"Name: {self.fname} \nSurname: {self.lname} \nAge: {self.age} \nSubject: {self.subject} \nSalary: {self.salary}\n")

    def teach(self):
        print(f"{self.fname} is teaching {self.subject}.")



st = Student("Ned", "Stark", 14, "A", "402")
t = Teacher("Jon", "Arryn", 54, "Sword Fighting", 2400)

st.display_info()
st.student_info()
st.study()

t.display_info()
t.teacher_info()
t.teach()
