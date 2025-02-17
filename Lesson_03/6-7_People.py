# Exercise 6-7: People

# Create 3 dictionary storing different values
person1: dict[str, str | int] = {"first_name": "Andrea", "last_name": "Montanari", "age": "29", "city": "Rome"}
person2: dict[str, str | int] = {"first_name": "Christian", "last_name": "De Palma", "age": "29", "city": "Rome"}
person3: dict[str, str | int] = {"first_name": "Simone", "last_name": "Calabrese", "age": "33", "city": "Rome"}

# Store all three dictionaris in an unique list
people: list[dict[str, str | int]] = [person1, person2, person3]

# Loop through the list and print each person's details
for person in people:
    print(f"First Name: {person['first_name']}")
    print(f"Last Name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
    print()
