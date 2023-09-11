# 1. Паралельна обробка списку:
# Створіть програму, яка створює два потоки. Перший потік обробляє парні елементи списку, 
# а другий - непарні. Згодом, з'єднайте результати обробки.

import threading
import time

ex_list = ["apple", "banana", "orange", "pineapple", "apricot", "pear"]

def even(list):
    for e in list:
        index = list.index(e)
        if (index % 2) == 0:
            print(e)
        else:
            pass

# even(ex_list)

def odd(list):
    for e in list:
        index = list.index(e)
        if (index % 2) != 0:
            print(e)
        else:
            pass


# odd(ex_list)

# t1 = threading.Thread(even(ex_list))
# t2 = threading.Thread(odd(ex_list))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("Done!")


# 2. Вимірювання часу виконання:
# Напишіть програму, яка виконує якусь обчислювально "важку" функцію у потоках. 
# Виміряйте час виконання обчислень з використанням потоків та без них, щоб порівняти результати.



def func():
    start_time = time.perf_counter()
    my_list = []
    for i in range(1, 10000):
        my_list.append(i)
    end_time = time.perf_counter()
    print(end_time - start_time)

# func()
st_time = time.perf_counter()
t1 = threading.Thread(func())
t2 = threading.Thread(func())

t1.start()
t2.start()

t1.join()
t2.join()

end_time = time.perf_counter()
delta_time = end_time - st_time
print(f"Execution time: {delta_time}")
