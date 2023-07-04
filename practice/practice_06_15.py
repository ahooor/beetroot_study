# 1. Реалізуйте функціонал генерування пошт для компанії "kobzar.com", де користувач 
# повинен самостійно вводити своє ім'я і прізвище з терміналу.

name = input("Name: ")
surname = input("Surname: ")
email = "@kobzar.com"

print("\n\n\n")

print(f"{name.lower()}"[0:1], f"{surname.lower()}", f"{email}", sep = "")

print(f"{name}.{surname}{email}".lower())

print(f"{name[0:3]}.{surname[0:3]}{email}".lower())

# 2. Ви - настирливий продавець і коли хтось відвідує ваш сайт онлайн-магазину, 
# ви запитуєте 5 разів у користувача, чи потрібно йому передзвонити. На 6-ий раз 
# ви нарешті лишаєте покупця в спокої і бажаєте йому гарних покупок.

print("\n\n\n")

i = 1

while i != 6:
    print("Need help?\n")
    i += 1
else: pass

# 3. Ви - тепер ще більш настирливий продавець і коли користувач відвідує ваш сайт, 
# ви прямо таки постійно питаєте у нього, чи потрібно йому передзвонити для формування замовлення. 
# Допоки користувач не натиснув кнопку "ні, дякую", ви постійно нагадуватимете йому про дзвінок.
# *під натисканням кнопки ми зараз маємо на увазі ввід користувача з терміналу

print("\n\n\n")

print("Need help? ")
while input() != "No":
    print("Need help? ")

# 4. Ви - власник онлайн магазину канцтоварів. Кожному 3-му покупцю ви обіцяєте в подарунок 
# ручку до замовлення, а кожному 5-му - лінійку.

print("\n\n\n")

customers = input("Amount of customers: ")

if customers.isdigit():
    for x in range(1, int(customers)):
        print(x)
        if x % 3 == 0:
            print("You've won a pen!")
        if x % 5 == 0:
            print("You've won a ruler!")
else: 
    print("You've entered the wrong value.")

# 5. Створіть програму, яка перевіряє, чи може користувач отримати кредит в банку. 
# Запитайте у користувача про його дохід, вік та наявність роботи. Врахуйте різні умови, 
# такі як мінімальний дохід, мінімальний/максимальний вік та наявність роботи.
# Мінімальний дохід, мінімальний/максимальний вік задайте самостійно.

print("\n\n\n")

min_age = 18
max_age = 65
min_income = 15000

age = input("Enter your age: ")

if age.isdigit() and int(age) >= min_age and int(age) <= max_age:
    if  input("Are you employed (yes/no): ").lower() == "yes":
        if int(input("Enter your income (in UAH): ")) >= min_income:
            print("Mortgage accepted.")
        else:
            print("Sorry, your income is not enough.")
    else:
        print("Sorry, you need to be employed")
else:
    print("Sorry, we can't help you.")

# 6. Напишіть програму, яка перевіряє, чи відповідає пароль для сайту вашим вимогам. 
# Напишіть самостійно список вимог до паролю (наявність великої букви, спеціальних символів, 
# чисел, пароль має бути довший 8 символів і тд) і перевірте, чи введений пароль сформований вірно.

# requirements: 1 upper 1 lower 1 digit min 12 symbols

print("\n\n\n")

min_length = 12

password = input("Please, enter your password: ")
password_len = len(password)
password_up = False
password_low = False
password_digit = False

for x in password:
    if x.isdigit():
        password_digit = True
        continue
    if x.upper() == x:
        password_up = True
        continue
    if x.lower() == x:
        password_low = True

if password_len >= 12 and password_digit and password_up and password_low:
    print("Password saved.")
else:
    print("Password is invalid.")