import requests

response = requests.get('https://en.wikipedia.org/wiki/Gammalsvenskby')

with open('robots.txt', 'w+') as file:
    file.write(response.text)