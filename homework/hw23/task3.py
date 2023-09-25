import requests

URL = 'http://api.weatherapi.com/v1/current.json'

q = input('Enter your city: ')

parameters = {
    'key': '67285c3c2df9414b9bd144613232509',
    'q': q
}

response = requests.get(URL, params=parameters)

# print(response.json())

response = response.json()

print("City:", response['location']['name'])
print("Country:", response['location']['country'])
print("Local Time:", response['location']['localtime'])
print("Temperature (Celsius):", response['current']['temp_c'])