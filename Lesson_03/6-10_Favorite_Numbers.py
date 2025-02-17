# Exercise 6-10: Favorite Numbers

# Creating a dictionary storing people's favorite numbers
favorite_numbers: dict[str, list[int]] = {
    "Alessio": [69, 32],
    "Delia": [6, 33],
    "Noemi": [23, 50],
    "Federica": [80, 222],
    "Valerio": [1, 31]
}

# Iterating through each person and their favorite numbers
for names, numbers in favorite_numbers.items():
    # Converting each number to a string using list comprehension
    string_numbers = ", ".join([str(num) for num in numbers])

    # Printing the person's name along with their formatted favorite numbers
    print(f"{names}'s favorite numbers are: {string_numbers}")
