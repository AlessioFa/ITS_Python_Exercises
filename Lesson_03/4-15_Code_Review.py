# Exercise 4-15: Code review 

# From exercise 4-1, I updated the type hinting for the favorite_pizzas list from str to list[str].

favorite_pizzas: list[str] = ["margherita", "sausages and potatoes", "sausages and tomatoes"]

# Loop to print each pizza with a message
for pizza in favorite_pizzas:
    print(f"I really like pizza {pizza}.")

# Additional sentences with specific pizza types using indexing
print(f"I'm in love with the pizza {favorite_pizzas[0]}.")
print(f"I like {favorite_pizzas[1]} pizza.")
print(f"I really like {favorite_pizzas[2]} pizza.")
print("I really love pizza!")


# From exercise 4-2, I updated the variable name to 'animals_list', 
# changed the type hinting to 'list[str]', and improved PEP 8 compliance 
# by ensuring proper spacing in comments.

# Exercise 4-2: Animals

# Store the names of three kinds of animals
animals_list: list[str] = ["lion", "tiger", "leopard"]

# Loop to print each animal with a message
for animal in animals_list:
    print(f"The {animal} is a majestic beast.")

# Add a sentence about what these animals have in common
print("These animals are all big cats with incredible strength and agility!")


# From exercise 4-5, I renamed "million" to "million_numbers" for clarity.
# I corrected the type hint for "million_numbers" from "int" to "list[int]".

# Exercise 4-5: Summing a million

# Create a list of numbers from 1 to 1 million
million_numbers: list[int] = list(range(1, 1000001))

# Find the minimum value in the list
min_million = min(million_numbers)
print(min_million)

# Find the maximum value in the list
max_million = max(million_numbers)
print(max_million)

# Calculate the sum of all numbers in the list
sum_million = sum(million_numbers)
print(sum_million)
