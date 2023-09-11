import asyncio
import aiohttp

# async def print_numbers():
#     for i in range(1, 6):
#         print(i)
#         await asyncio.sleep(1)

# async def print_letters():
#     for letter in 'ABCDE':
#         print(letter)
#         await asyncio.sleep(2)

# async def print_signs():
#     for sign in '$#^&*':
#         print(sign)
#         await asyncio.sleep(4)     

# async def main():
#     task1 = asyncio.create_task(print_numbers())
#     task2 = asyncio.create_task(print_letters())
#     task3 = asyncio.create_task(print_signs())
#     await asyncio.gather(task1, task2, task3)

# asyncio.run(main())


# 1. Асинхронний REST API запит:
# Створіть програму, яка асинхронно взаємодіє з публічним REST API за допомогою aiohttp, 
# отримуючи та оброблюючи дані з відповідей. (https://russianwarship.rip/api-documentation/v2)

async def main():

    async with aiohttp.ClientSession() as session:
        url3 = "http://api.weatherapi.com/v1/current.json"
        async with session.get(url3) as resp:
            info = await resp.json()
            print(info)

        async with session.get(url3) as resp:
            info = await resp.json()
            print(info)

asyncio.run(main())