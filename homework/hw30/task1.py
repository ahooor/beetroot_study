# Реалізувати алгоритм бінарного пошуку за допомогою рекурсії.

# Прочитати про Fibonacci search та імплементуйте його за допомогою Python. 
# Визначте складність алгоритму та порівняйте його з бінарним пошуком

def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid

    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)

    else:
        return binary_search_recursive(arr, target, low, mid - 1)


def fibonacci_search(arr, target):
    def fib(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    n = len(arr)
    offset = -1
    while fib(0) < n:
        while fib(1) <= n - offset:
            offset += 1

        i = min(offset, n - 1)

        if arr[i] < target:
            offset += 1
        elif arr[i] > target:
            offset -= 1
        else:
            return i
    return -1 
