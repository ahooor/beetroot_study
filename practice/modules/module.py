products = {
  "Kefir" : {"price" : "12$", "amount": "50"},
  "Milk" : {"price" : "8$", "amount": "120"},
  "Yoghurt" : {"price" : "20$", "amount": "83"}
  }

def update_dict(name, price, amount):
    if name != None:
        if name in products.keys():
            products[name]["price"] = price
            products[name]["amount"] = amount
            print(products)
        else:
            products.update({name: {"price": price, "amount": amount}})
            print(products)
    else:
        pass

def calculate(first_number, second_number, operation):
    while first_number != "q" and second_number != "q":
        first_number = int(first_number)
        second_number = int(second_number)
        if operation == "+":
            print(first_number + second_number)
            break
        elif operation == "-":
            print(first_number - second_number)
            break
        elif operation == "*":
            print(first_number * second_number)
            break
        elif operation == "/":
            print(first_number / second_number)
            break
    else:
        pass

employees = [["Petro", "Petrov", "@oracle.com"], ["Vasyl", "Tsik", "@oracle.com"], ["Fedir", "Mainov", "@oracle.com"], 
             ["Gregor", "Clegane", "@oracle.com"], ["Harry", "Potter", "@oracle.com"]]

def generate_email(employees):
    for employee in employees:
        print(employee[0].lower() + employee[1].lower() + employee[2].lower())
        print(employee[0].lower() + "_" + employee[1].lower() + employee[2].lower())
        print(employee[0][0:3].lower() + "." + employee[1].lower() + employee[2].lower())
        print("\n")

grades = {"student1": {"maths": 5, "biology": 3, "literature": 4},
          "student2": {"maths": 2, "biology": 2, "literature": 3},
          "student3": {"maths": 4, "biology": 4, "literature": 5}}

def upd_grades(st_name, disc_name, st_grade):
    if st_name in grades.keys():
        grades[st_name][disc_name] = st_grade
        print(grades, "\n")
    else:
        grades.update({st_name: {disc_name: st_grade}})
        print(grades, "\n")

orders = [("Caesar", 30), ("Ceviche", 26), ("Minestrone", 24)]

def add_order(dish, price):
    orders.append((dish, int(price)))
    print(orders)

def delete_order(dish, price):
    orders.remove((dish, price))
    print(orders)

def checkout(orders):
    total_price = 0
    for order in orders:
        dish, price = order
        total_price += price
    return total_price 

if __name__ == "_main__":
    pass