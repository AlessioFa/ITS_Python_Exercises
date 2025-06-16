# Exercise 6-1: Person

# Dictionary that stores personal details
person: dict[str, str | int] = {"first_name": "Andrea", "last_name": "Montanari", "age": "29", "city": "Rome"}


print(f"These are all the person's detail.\nFirst Name: {person['first_name']}\nLast Name: {person['last_name']}\nAge: {person['age']}\nCity: {person['city']}")


# Doing the same exercise using for loop

# Loop through the dictionary and print each key-value pair
for key, value in person.items():

    # Format the key and print the key-value pair
    print(f"{key.replace('_', ' ').title()}: {value}")
