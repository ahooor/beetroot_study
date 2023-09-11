import requests
import json
from restcountries import RestCountryApiV2 as rapi


api_url = "https://russianwarship.rip/api/v2/war-info"
response = requests.get(api_url)
print(response)
print("\n\n")

x = response.json()
print(type(x))

print("\n\n")
print(x["data"]["current_day"])

api_url = "https://russianwarship.rip/api/v2/statistics"
response = requests.get(api_url, params="offset=0&limit=50&date_from=2023-08-01&date_to=2023-08-19")
x = response.json()
print(response.headers, response.status_code)


capitals = ["kyiv", "london", "madrid", "berlin", "warsaw"]
api_url = "https://restcountries.com/v3.1/capital/"

# for capital in capitals:
#     response = requests.get(f"{api_url}"+f"{capital}")
#     # print(type(response.json()[0]))
#     x = response.json()
#     x1 = x[0]
#     print(x1["name"]["official"])

# def foo(name):
#     country_list = rapi.get_countries_by_name(name)
#     print(country_list)

# foo("F")



    


