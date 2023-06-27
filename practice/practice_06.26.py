# 1.  Створіть програму для керування списком продуктів в інтернет-магазині. 
# Кожен продукт може мати назву, ціну та кількість на складі. Реалізуйте можливість 
# користувачу додавати нові продукти, оновлювати інформацію про продукти та виводити 
# список доступних продуктів за певними критеріями (наприклад, за ціною або наявністю на складі).
# (потрібно використати ф-ю input(), щоб користувач міг вводити дані з консолі)

print("\n")

products = {
  "Kefir" : {"price" : "12$", "amount": "50"},
  "Milk" : {"price" : "8$", "amount": "120"},
  "Yoghurt" : {"price" : "20$", "amount": "83"}
  }

print(products)

print("\n")

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

update_dict(name = "Eggs", price = "18$", amount = "2000")

# 2. Напишіть програму для керування списком завдань. 
# Кожне завдання може мати назву, опис, пріоритет та статус 
# (наприклад, "виконується", "в очікуванні", "завершено"). 
# Реалізуйте можливість додавання нових завдань, оновлення статусу 
# завдань та виведення списку завдань за пріоритетом.

tasks = {"to have lunch": {"description": "just eat", "status": "not started", "priority": "high"}, 
          "to walk a dog": {"description": "take a dog for a walk", "status": "in progress", "priority": "critical"}}

print("\n"*2)

def update_task(task_name, task_desc, task_status, task_prio):
    if task_name in tasks.keys():
        tasks[task_name]["status"] = task_status
        print(tasks)
    else:
        tasks.update({task_name:{"description": task_desc, "status": task_status, "priority": task_prio}})
        print(tasks)

update_task("to have lunch", "just read it already", "in progress", "low")

# 3. Запрограмуйте програму калькулятор, яка буде приймати від користувача введення 
# 2-х чисел та вид математичної операції (+, -, *, /). Виведіть результат операції та 
# продовжуйте виконання калькулятора, поки користувач не введе символ "q" для виходу.

print("\n")

# a = input("Enter your first number: ")
# b = input("Enter your second number: ")

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

calculate(first_number = "23", second_number = "24", operation = "+")
calculate(first_number = "56", second_number = "562", operation = "*")
calculate(first_number = "1045", second_number = "5", operation = "/")

# 4. Знову генеруємо пошту для працівника, але тепер всі дані містяться в списку
# ["name", "surname", "domain"]
# 5. Те ж саме завдання із генеруванням пошти, але тепер у вас декілька 
# працівників (нехай буде 5). Спробуйте використати вкладені списки

print("\n")

empl = [["Petro", "Petrov", "@oracle.com"], ["Vasyl", "Tsik", "@oracle.com"], ["Fedir", "Mainov", "@oracle.com"], 
             ["Gregor", "Clegane", "@oracle.com"], ["Harry", "Potter", "@oracle.com"]]

def generate_email(employees):
    for employee in employees:
        print(employee[0].lower() + employee[1].lower() + employee[2].lower())
        print(employee[0].lower() + "_" + employee[1].lower() + employee[2].lower())
        print(employee[0][0:3].lower() + "." + employee[1].lower() + employee[2].lower())
        print("\n")

generate_email(employees = empl)

# 6. Напишіть програму для керування студентськими оцінками. 
# Реалізуйте можливість додавання оцінок, видалення оцінок, 
# обчислення середнього балу студента та виведення списку студентів з їх оцінками.

grades = {"student1": {"maths": 5, "biology": 3, "literature": 4},
          "student2": {"maths": 2, "biology": 2, "literature": 3},
          "student3": {"maths": 4, "biology": 4, "literature": 5}}

# st_name = input("Enter the name of the student: ")
# disc_name = input("Enter the name of the discipline: ")
# st_grade = input("Enter the grade: ")

def upd_grades(st_name, disc_name, st_grade):
    if st_name in grades.keys():
        grades[st_name][disc_name] = st_grade
        print(grades, "\n")
    else:
        grades.update({st_name: {disc_name: st_grade}})
        print(grades, "\n")

upd_grades(st_name = "student4", disc_name = "maths", st_grade = "5")
upd_grades(st_name = "student4", disc_name = "biology", st_grade = "2")
upd_grades(st_name = "student2", disc_name = "maths", st_grade = "3")
upd_grades(st_name = "student1", disc_name = "PE", st_grade = "4")

# 7. Створіть програму для управління замовленнями в ресторані. 
# Використовуйте список (list) для зберігання замовлень, де кожне 
# замовлення представлене як кортеж (tuple) з назвою страви і ціною. 
# Реалізуйте можливість додавання нових замовлень, видалення замовлень 
# і розрахунку загальної суми замовлення.

print("\n")

orders = [("Caesar", 30), ("Ceviche", 26), ("Minestrone", 24)]

def add_order(dish, price):
    orders.append((dish, int(price)))
    print(orders)

add_order(dish = "Cheese plate", price = 12)

def checkout(orders):
    for order in orders: