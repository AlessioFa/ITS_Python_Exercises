# Exercise 4-7: Threes

# Create a list numbers from 3 to 30 using range() with a step of 3
multiples_of_3: list[int] = list(range(3, 31, 3))

# Display the list of multiples of 3
print(multiples_of_3)

# Iterate throught the list and print each multiple of 3
for n in multiples_of_3:
    print(n)
