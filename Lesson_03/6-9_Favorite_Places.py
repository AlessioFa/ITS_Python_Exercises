# Exercise 6-9: Favorite Places

# Create a dictionary with names as keys and lists of favorite places as values
favorite_places: dict[str, list[str]] = {
    "Alessio": ["Cali", "Buenaventura", "New Mexico"],
    "Andrea": ["Capri", "Grecia", "Polinesia"],
    "Christian": ["Japan", "Thailandia", "New Zeland"]
}
# Loop through each person in the dictionary
for names, cities in favorite_places.items():
    # Print the person's name and their favorite places, separated by commas
    print(f"{names}: {', ' .join(cities)}")
