# Exercise 4-9: Cube Comprehension

# Create a list of cubes for numbers from 1 to 10 using list comprehension
cube: list[int] = [n**3 for n in range(1, 11)]

# Print the list of cubes
print(cube)
