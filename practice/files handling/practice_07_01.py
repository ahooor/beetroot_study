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

# f = open("/Users/alisiyanosenko/Python/beetroot_study/practice/nestle_employee.csv", "r")
# print(f.read())

f = open("/Users/alisiyanosenko/Python/beetroot_study/practice/nestle_employee.csv", "r")
print(f)

# with open("/Users/alisiyanosenko/Python/beetroot_study/practice/nestle_employee.csv", "r") as file:
#     reader = csv.reader(file)
#     for item in reader:
#         print(item)

# with open("/Users/alisiyanosenko/Python/beetroot_study/practice/nestle_employee.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow(['Alisiya', 'Horbenko', '23', '+370 12345678', 'Odesa', 'Ukraine', 'Business Analysis', 'Business Analyst'])

# with open("/Users/alisiyanosenko/Python/beetroot_study/practice/nestle_employee.csv", "r") as file:
#     reader = csv.reader(file)
#     for item in reader:
#         print(item)

# with open("/Users/alisiyanosenko/Python/beetroot_study/practice/nestle_employee.csv", "w+") as file:
#     writer = csv.writer(file)
#     writer.writerow(['Alisiya', 'Horbenko', '23', '+370 12345678', 'Odesa', 'Ukraine', 'Business Analysis', 'Business Analyst'])