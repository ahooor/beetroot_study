import json
import csv

# with open("/Users/alisiyanosenko/Python/beetroot_study/practice/processors.json", "r") as file:
#     data = json.load(file)

# unique_locations = set(item["location"] for item in data)

# for location in unique_locations:
#     print(location)

# for item in data:
#     if item["processor"] == "AMD Ryzen":
#         item["processor"] = "AMD Ryzen 2"

# with open("/Users/alisiyanosenko/Python/beetroot_study/practice/processors.json", "w") as file:
#     json.dump(data, file, indent=4)

# with open("/Users/alisiyanosenko/Python/beetroot_study/practice/processors.json", "r+") as file:
#     data = json.load(file)
#     index = 0
#     for item in data:
#         if "Russia" in item["location"]:
#             data.pop(index)
#         else:
#             index += 1

# with open("/Users/alisiyanosenko/Python/beetroot_study/practice/processors.json", "w+") as file:
#     json.dump(data, file, indent=4)


# data = [
# {
#     "name": "Gregor",
#     "surname": "Clegane",
#     "occupation": "python dev"
# },
# {
#     "name": "Jaime",
#     "surname": "Lannister",
#     "occupation": "PM"
# },
# {
#     "name": "Ned",
#     "surname": "Stark",
#     "occupation": "devops"
# }
# ]

# with open("/Users/alisiyanosenko/Python/beetroot_study/practice/workers.json", "w") as file:
#     json.dump(data, file, indent=4)

# f = open("/Users/alisiyanosenko/Python/beetroot_study/practice/files handling/nestle_employee.csv", "r")
# print(f.read())

# f = open("/Users/alisiyanosenko/Python/beetroot_study/practice/files handling/nestle_employee.csv", "r")
# print(f)

# with open("/Users/alisiyanosenko/Python/beetroot_study/practice/files handling/nestle_employee.csv", "r") as file:
#     reader = csv.reader(file)
#     for item in reader:
#         print(item)

# with open("/Users/alisiyanosenko/Python/beetroot_study/practice/files handling/nestle_employee.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow(['Alisiya', 'Horbenko', '23', '+370 12345678', 'Odesa', 'Ukraine', 'Business Analysis', 'Business Analyst'])

# with open("/Users/alisiyanosenko/Python/beetroot_study/practice/files handling/nestle_employee.csv", "r") as file:
#     reader = csv.reader(file)
#     for item in reader:
#         print(item)

# with open("/Users/alisiyanosenko/Python/beetroot_study/practice/files handling/nestle_employee.csv", "w+") as file:
#     writer = csv.writer(file)
#     writer.writerow(['Alisiya', 'Horbenko', '23', '+370 12345678', 'Odesa', 'Ukraine', 'Business Analysis', 'Business Analyst'])

list_of_employees = "/Users/alisiyanosenko/Python/beetroot_study/practice/files handling/nestle_employee.csv"

def transform_to_list(name):
    with open(name) as file:
        reader = csv.reader(file)
        l = list(reader)
        return l

list_of_employees = transform_to_list(list_of_employees)
print("\n")
print(list_of_employees[0:5])

employee = ["Petro", "Fedun", "19", "+380503451234", "Ternopil", "Ukraine", "IT", "Senior Python dev"]

def add_employee(pos, data, list):
    list.insert(pos, data)
    return list

add_employee(3, employee, list_of_employees)
print("\n")
print(list_of_employees[0:5])

def pop_employee(pos, list):
    list.pop(pos)
    return list

pop_employee(1, list_of_employees)
print("\n")
print(list_of_employees[0:5])

def check(path):
    try: 
        f = open(path, "r")
        print(f.read())
    except:
        print("Your file is not found")

# check("/Users/alisiyanosenko/Python/beetroot_study/practice/practice_06_15.py")

# with open("/Users/alisiyanosenko/Python/beetroot_study/practice/files handling/nestle_employee_new_file.csv", "w+") as file:
#     writer = csv.writer(file)
#     writer.writerows(list_of_employees)

name = input("Enter your employee name: ")
surname = input("Enter your employee surname: ")
age = input("Enter your employee age: ")
phone = input("Enter your employee phone: ")
city = input("Enter your employee city: ")
country = input("Enter your employee country: ")
department = input("Enter your employee department: ")
occupation = input("Enter your employee occupation: ")

# IF FILE IS .CSV:

# employee_data = [f"{name}", f"{surname}", f"{age}", f"{phone}", f"{city}", f"{country}", f"{department}", f"{occupation}"]
# print(employee_data)

# add_employee(3, employee_data, list_of_employees)
# print("\n")
# print(list_of_employees[0:5])

# IF FILE IS .JSON:

employee_data = {
    "name": f"{name}", 
    "surname": f"{surname}", 
    "age": f"{age}", 
    "phone": f"{phone}", 
    "city": f"{city}", 
    "country": f"{country}", 
    "department": f"{department}", 
    "occupation": f"{occupation}"
    }

print(employee_data)

# add_employee(3, employee_data, list_of_employees)
# print("\n")
# print(list_of_employees[0:5])