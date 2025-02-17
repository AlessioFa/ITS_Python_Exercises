# Exercise 6-2: Favorite Numbers

# Creating a dictionary storing people's favorite numbers

favorite_numbers: dict[str | int] = {
    "Alessio": 69,
    "Delia": 6,
    "Noemi": 23,
    "Federica": 80,
    "Valerio": 1
}
# Loop through the dictionary and print each name and their favorite number
for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}")
    print()
