# Exercise: 6-8 Pets

# Create three different dict storing owner and his/ her animal
pet1: dict[str, str] = {"Owner": "Alex", "Animal": "dog"}
pet2: dict[str, str] = {"Owner": "Elise", "Animal": "dog"}
pet3: dict[str, str] = {"Owner": "Alex", "Animal": "dog"}

# Store all thre dict in a list
all_pets: list[dict[str, str]] = [pet1, pet2, pet3]


for pet in all_pets:
    print(f"Owner: {pet['Owner']}")
    print(f"Pet: {pet['Animal']}")
    print()
