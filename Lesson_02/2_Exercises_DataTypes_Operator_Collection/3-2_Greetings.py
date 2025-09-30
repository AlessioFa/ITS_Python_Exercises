# Exercise 3-2: Greetings

# Initialize the list with friends' names
names: list[str] = ["Andrea", "Christian", "Simone", "Luana"]

# Use indexing to access all the element in the list
print(f"{names[0]} is a really good boy!")
print(f"{names[1]} is a funny guy!")
print(f"{names[2]} is a particoular but genuine guy!")
print(f"{names[3]} is a curious girl!\n")

# Solving the exercise using a for loop that iterate through the list
for name in names:
    print(f"{name} is a good friend!")
