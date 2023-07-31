import datetime


'''1. Реалізувати декоратор, який перевіряє, чи є аргумент функції числом
 та виводить повідомлення про помилку, якщо це не так.
2. Написати декоратор, який обмежує кількість разів виклику функції та видає помилку, якщо ліміт перевищено.
3. Створити декоратор, який змінює результат функції на протилежне значення (наприклад, з True на False).
4. Напишіть декоратор, який перевіряє типи аргументів,
 переданих до функції, та виводить повідомлення про помилку, якщо типи не відповідають очікуваним.'''

#Task 1
'''
def our_decorator(func):
    def decorator_numbers(arg_list):
        
        for el in arg_list:
            if type(el) == int or type(el) == float:
                print("all is ok")

            else:
                #decorator_numbers = int(numbers())

                print('Use degits format!')
    return decorator_numbers

@our_decorator
def numbers(my_list):
    return my_list

numbers([3, 2])
numbers(['3', '2'])
numbers([3, '2'])
'''
#Task 2
'''
def changer_decorator(func):
    def dec(*args):
        result = func(*args)
        if result:
            return False
        else:
            return True
    return dec

@changer_decorator
def initial_func(k):
    if k%3==0:
        return True
    else:
        return False

print(initial_func(6))
'''
#Task 3
#2. Написати декоратор, який обмежує кількість разів виклику функції та видає помилку, якщо ліміт перевищено.

'''
def decorator(func):
    calls = 0
    def wrapper():
        nonlocal calls
        if calls >= 5:
            print('You call func > 5 times')
        else:
            calls += 1
            func()
    return wrapper


@decorator
def test():
    print('func called')

test()
test()
test()
test()
test()
test()
'''
#Task 4
#4. Напишіть декоратор, який перевіряє типи аргументів,
# переданих до функції, та виводить повідомлення про помилку, якщо типи не відповідають очікуваним
'''
def decorator(func):
    def wrapper(a):
        if type(a) != int:
            print('incorrect type')
        else:
            return func(a)
    return wrapper

@decorator
def test(a):
    print(a)

test('a')
'''

#Реалізуйте функцію, яка перетворює рядок на ініціали (перші літери кожного слова).
# Використайте вкладену функцію для розбиття рядка на окремі слова та отримання першої літери кожного слова.

#Task 4
'''
def decorator(func):
    def wrapper(a):
        if type(a) != str:
            print('not string format')
        else:
            a = a.split()
            for word in a:
                print(word[0].upper())
        return func(a)
    return wrapper

@decorator
def test(a):
    print(a)

test('This is test')
'''

#1. Реалізувати функцію, яка буде загорнута в декілька декораторів (декоратори потрібно написати самим)
'''
def validation(func):
    def wrapper(a, b):
        if type(a) != str or len(a) < 8:
            print('Invalid password!')
        else:
            return func(a, b)
    return wrapper

def location(func):
    def wrapper(a, b):
        if b == 'russia':
            print('Slava Ukraini!')
        else:
            return func(a, b)
    return wrapper

@location
@validation
def test(a, b):
    print(a, b)

test('aaa', 'Denmark')
'''
#Task 6
#2. Написати декоратор, який всередині буде відловлювати помилку (реалізувати try-except statement)

def zero_division(func):
    def wrapper(a, b):
        try:
            return func(a, b)
        except ZeroDivisionError:
            print('You cannot divide by zero')
    return wrapper

@zero_division
def test(a, b):
    print(a//b)

test(10, 0)

#3. Напишіть декоратор, який записує в файл час, коли була викликана функція.
'''

def decorator(func):
    def wrapper():
        now = datetime.datetime.now()
        formatted = now.strftime('%H:%M:%S')
        #hour = now.hour
        #minute = now.minute
        #second = now.second
'''