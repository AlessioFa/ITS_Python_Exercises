# Exercise 4-10: Slices (from exercise 4-4)

# Create a list with numbers between 1 and 1 million
one_million: list[int] = list(range(1, 1000001))

# Get the first three elements
slicing_one_million = one_million[0:3]
print(f"The first three elements of the list are: {slicing_one_million}")

# Find the middle index
middle_index = len(one_million) // 2

# Get three elements from the center
middle_three = one_million[middle_index - 1: middle_index + 2]
print(f"The central elements of the list are: {middle_three}")

# Get the last three elements
last_three = one_million[-3:]
print(f"The last three elements of the list are: {last_three}")
