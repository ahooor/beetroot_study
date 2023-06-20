# Запрограмуйте програму калькулятор, яка буде приймати від користувача введення 2-х чисел 
# та вид математичної операції (+, -, *, /). Виведіть результат операції та продовжуйте виконання калькулятора, 
# поки користувач не введе символ "q" для виходу.

print("\n")

a = input("Enter your first number: ")
b = input("Enter your second number: ")

while a != "q" and b != "q":
    c = input("Choose your operation (+, -, *, /): ")
    a = int(a)
    b = int(b)
    if c == "+":
        print(a + b)
        break
    if c == "-":
        print(a - b)
        break
    if c == "*":
        print(a * b)
        break
    if c == "/":
        print(a / b)
        break
else:
    pass

# Знову генеруємо пошту для працівника, але тепер всі дані містяться в списку:
# sunglasses:["name", "surname", "domain"]

print("\n")

email = ["Petro", "Petrov", "@oracle.com"]

print(email[0].lower() + email[1].lower() + email[2].lower())
print(email[0][0].lower() + "_" + email[1].lower() + email[2].lower())
print(email[0][0:3].lower() + "." + email[1].lower() + email[2].lower())

# Те ж саме завдання із генеруванням пошти, але тепер у вас декілька працівників (нехай буде 5). 
# Спробуйте використати вкладені списки

print("\n")

employers = [["Petro", "Petrov", "@oracle.com"], ["Vasyl", "Tsik", "@oracle.com"], ["Fedir", "Mainov", "@oracle.com"], 
             ["Gregor", "Clegane", "@oracle.com"], ["Harry", "Potter", "@oracle.com"]]

print(employers[0][0].lower() + employers[0][1].lower() + employers[0][2].lower())
print(employers[1][0].lower() + employers[1][1].lower() + employers[1][2].lower())
print(employers[2][0].lower() + employers[2][1].lower() + employers[2][2].lower())
print(employers[3][0].lower() + employers[3][1].lower() + employers[3][2].lower())
print(employers[4][0].lower() + employers[4][1].lower() + employers[4][2].lower())

print("\n")

print(employers[0][0].lower() + "_" + employers[0][1].lower() + employers[0][2].lower())
print(employers[1][0].lower() + "_" + employers[1][1].lower() + employers[1][2].lower())
print(employers[2][0].lower() + "_" + employers[2][1].lower() + employers[2][2].lower())
print(employers[3][0].lower() + "_" + employers[3][1].lower() + employers[3][2].lower())
print(employers[4][0].lower() + "_" + employers[4][1].lower() + employers[4][2].lower())

print("\n")

print(employers[0][0][0:3].lower() + "." + employers[0][1].lower() + employers[0][2].lower())
print(employers[1][0][0:3].lower() + "." + employers[1][1].lower() + employers[1][2].lower())
print(employers[2][0][0:3].lower() + "." + employers[2][1].lower() + employers[2][2].lower())
print(employers[3][0][0:3].lower() + "." + employers[3][1].lower() + employers[3][2].lower())
print(employers[4][0][0:3].lower() + "." + employers[4][1].lower() + employers[4][2].lower())

# Створіть програму для керування списком продуктів в інтернет-магазині. 
# Кожен продукт може мати назву, ціну та кількість на складі. Реалізуйте 
# можливість користувачу додавати нові продукти, оновлювати інформацію про 
# продукти та виводити список доступних продуктів за певними критеріями 
# (наприклад, за ціною або наявністю на складі).

print("\n")

products = {
  "Kefir" : {"price" : "12$", "amount": "50"},
  "Milk" : {"price" : "8$", "amount": "120"},
  "Yoghurt" : {"price" : "20$", "amount": "83"}
  }

print(products)

print("\n")

name = input("Product name: ")
price = input("Product price: ")
amount = input("Product amount: ")

print("\n")

if name in products.keys():
    products[name]["price"] = price
    products[name]["amount"] = amount
else:
    products.update({name: {"price": price, "amount": amount}})

print(products)
