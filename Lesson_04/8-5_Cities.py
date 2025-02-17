# Exercise 8_5: Cities

# Define the function with a default country parameter
def describe_city(city: str, country: str = "Japan"):
    print(f"{city} is in {country}")

# Call the function with the default country (Japan)
describe_city("Tokyo")

# Call the function with a custom country (France)
describe_city("Parigi", country="France")

# Call the function with another custom country (Italy)
describe_city("Rome", country="Italy")
