import multiprocessing

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    result = [0, 1]
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
        result.append(b)
    return result

def factorial(n):
    if n < 0:
        return []
    elif n == 0:
        return [1]
    
    result = [1]
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        result.append(fact)
    return result

def squares(n):
    return [x ** 2 for x in range(1, n + 1)]

def cubes(n):
    return [x ** 3 for x in range(1, n + 1)]

def calculate_for_range_multiprocessing():
    numbers = list(range(1, 11))
    with multiprocessing.Pool() as pool:
        fibonacci_result = pool.map(fibonacci, numbers)
        factorial_result = pool.map(factorial, numbers)
        squares_result = pool.map(squares, numbers)
        cubes_result = pool.map(cubes, numbers)
    return fibonacci_result, factorial_result, squares_result, cubes_result

if __name__ == "__main__":
    import time
    
    start_time = time.time()
    
    result = calculate_for_range_multiprocessing()
    
    end_time = time.time()
    
    print("Multiprocessing execution time:", end_time - start_time)
    
    fibonacci_result, factorial_result, squares_result, cubes_result = result
    
    print("Fibonacci:", fibonacci_result)
    print("Factorial:", factorial_result)
    print("Squares:", squares_result)
    print("Cubes:", cubes_result)
