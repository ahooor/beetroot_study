import asyncio

async def fibonacci(n):
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

async def factorial(n):
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

async def squares(n):
    return [x ** 2 for x in range(1, n + 1)]

async def cubes(n):
    return [x ** 3 for x in range(1, n + 1)]

async def calculate_for_range():
    numbers = list(range(1, 11))
    fibonacci_result = await asyncio.gather(*(fibonacci(n) for n in numbers))
    factorial_result = await asyncio.gather(*(factorial(n) for n in numbers))
    squares_result = await asyncio.gather(*(squares(n) for n in numbers))
    cubes_result = await asyncio.gather(*(cubes(n) for n in numbers))
    return fibonacci_result, factorial_result, squares_result, cubes_result

if __name__ == "__main__":
    import time
    
    start_time = time.time()
    
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(calculate_for_range())
    
    end_time = time.time()
    
    print("Async execution time:", end_time - start_time)
    
    fibonacci_result, factorial_result, squares_result, cubes_result = result
    
    print("Fibonacci:", fibonacci_result)
    print("Factorial:", factorial_result)
    print("Squares:", squares_result)
    print("Cubes:", cubes_result)