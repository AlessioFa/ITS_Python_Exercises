# Exercise 6-11: Cities

# Loop that iterates through each city and its associated information in the 'cities' dictionary
cities = {
    "Cali": {
        "city": "Colombia",
        "population": "2.4 m",
        "fact": "Cali is known as the world capital of salsa."
    },
    "Bristol": {
        "city": "England",
        "population": "467,000",
        "fact": "Bristol is famous for its Clifton Suspension Bridge."
    },
    "Rome": {
        "city": "Italy",
        "population": "2.8 m",
        "fact": "Rome is known as the 'Eternal City'."
    }
}

# Using the city names (keys) to access the corresponding information (values) in the dictionary.
for city, info in cities.items():
    print(f"{city} ({info['city']}):\nPopulation: {info['population']}\nFact: {info['fact']}\n\n")