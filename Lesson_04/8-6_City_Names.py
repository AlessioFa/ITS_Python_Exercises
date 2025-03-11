# Exercise 8-6: City Names

# Define a function that returns the city and its country
def city_country(city: str, country: str) -> str:
    return (f"{city}, {country}")


# Call the function with three city-country pairs
city1 = city_country("Rome", "Italy")
city2 = city_country("Tokyo", "Japan")
city3 = city_country("New York", "USA")

# Print the result
print(city1)
print(city2)
print(city3)
