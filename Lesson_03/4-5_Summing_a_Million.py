# Exercise 4-5: Summing a million

# Create a list of numbers from 1 to 1 million
million: int = list(range(1, 1000001))

# Find the minimum value in the list
min_million: int = min(million)
print(f"The smallest number is: {min_million}\n")

# Find the maximum value in the list
max_million = max(million)
print(f"The greatest number is: {max_million}\n")

# Calculate the sum of all numbers in the list
sum_million = sum(million)
print(f"The sum between all numbers is: {sum_million}")
