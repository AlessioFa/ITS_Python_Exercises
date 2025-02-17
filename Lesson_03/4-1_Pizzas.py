# Exercise 4-1: Pizzas

# Store three kind of pizzas in the list 
favorite_pizzas: str = ["margherita", "sausages and potatoes", "sausages and tomatoes"]

# Loop to print each pizza with a message
for pizza in favorite_pizzas:
    print(f"I really like pizza {pizza}.")

# Additional sentences with specific pizza types using indexing
print(f"I'm in love with the pizza {favorite_pizzas[0]}.")
print(f"I like {favorite_pizzas[1]} pizza.")
print(f"I really like {favorite_pizzas[2]} pizza.")

print("I really love pizza!")
