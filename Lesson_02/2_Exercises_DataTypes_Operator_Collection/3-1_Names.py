# Exercise 3-1: Names

# Storing some strings value into a list called names
names: list[str] = ["Andrea", "Christian", "Simone", "Luana"]

# Print each person’s name by accessing each element in the list,
# Use indexing to access all the element in the list
print(f"{names[0]}, {names[1]}, {names[2]}")

# Solving the exercise using a for loop
# Iterating thorugh the list using a for loop and printing each name
for name in names:
    print(name)
