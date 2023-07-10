# 1. Реалізувати декоратор, який перевіряє, чи є аргумент функції числом та виводить повідомлення про помилку, якщо це не так.

def check_args(func):
    def check(a):
        if type(a) == int or type(a) == float:
            return "It's a number!"
        else:
            return "It's not a number!"
    return check

@check_args
def test(a):
    return a

print(test(8))

# 2. Написати декоратор, який обмежує кількість разів виклику функції та видає помилку, якщо ліміт перевищено.

def check_limits(func):
    def inner(a):
      calls = 0
      if calls >= 5:
         print("You've got func many times")
      else:
         calls += 1
    return inner

@check_limits
def test(a):
   print("Func called")

test("q")
test("q") 
test("q") 

def check_limits(func):
    calls = 0
    def inner(a):
        nonlocal calls  # declare calls as nonlocal ???
        if calls >= 5:
            print("You've called function too many times")
        else:
            calls += 1
            func(a)  
    return inner

@check_limits
def test(a):
   print("Function called")

test("q")
test("q")
test("q")
test("q")
test("q")
test("q")

# 3. Створити декоратор, який змінює результат функції на протилежне значення (наприклад, з True на False).

def invert(func):
    def inner(a):
        result = func(a) 
        return not result
    return inner

@invert
def even(a):
    return a % 2 == 0

print(even(1))    

# 4. Напишіть декоратор, який перевіряє типи аргументів, переданих до функції, та виводить повідомлення про помилку, якщо типи не відповідають очікуваним.

def check_type(func):
    def inner(a):
        if type(a) != int:
            print("It's not an int")
        else:
            return func(a)
    return inner

@check_type
def test(a):
    print(a)

test("5")

# 5. Реалізуйте функцію, яка перетворює рядок на ініціали (перші літери кожного слова). 
# Використайте вкладену функцію для розбиття рядка на окремі слова та отримання першої літери кожного слова.
        
def initials(func):
    def inner(a):
        if type(a) != str:
            print("It's not a string!")
        else:
            a = a.split()
            for word in a:
                print(word[0].upper())
        return func(a)
    return inner

@initials
def test(a):
    print(a)
        
test("petro fedun")