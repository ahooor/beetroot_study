# Create a function called make_country, which takes in a country’s name 
# and capital as parameters. Then create a dictionary from those two, 
# with ‘name’ as a key and ‘capital’ as a parameter. Make the function 
# print out the values of the dictionary to make sure that it works as intended.

countries = {}
def make_country(name, capital):
    countries[name] = capital

make_country("Ukraine", "Kyiv")
make_country("USA", "Washington DC")
make_country("France", "Paris")
make_country("Germany", "Berlin")
make_country("Poland", "Warsaw")

print(countries)

countries_1 = [
    {
        "country": "Ukraine", 
        "capital": "Kyiv"
    },
    {
        "country": "USA",
        "capital": "Washington DC"
    },
    {
        "country": "France",
        "capital": "Paris"
    },
    {
        "country": "Germany",
        "capital": "Berlin"
    },
    {   
        "country": "Poland",
        "capital": "Warsaw"
    }
]

presidents = {
    "Ukraine": "Zelensky",
    "USA": "Biden",
    "Poland": "Duda"
}

def show_countries(countries):
    for country in countries:
        x = country
        print(x)

show_countries(countries_1)

def add_president(presidents, countries):
    for country in countries:
        if country["country"] in presidents:
            country["president"] = presidents[country["country"]]
    print(countries)

add_president(presidents, countries_1)