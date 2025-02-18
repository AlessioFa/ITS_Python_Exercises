# Exercise 4-11: My Pizzas, Your Pizzas

# List of favourite pizzas
favourite_pizzas: list[str] = ["margherita", "sausages and potatoes", "sausages and tomatoes"]

# Create a copy of friend_pizzas for favourite_pizzas
friend_pizzas = favourite_pizzas.copy()

# Add different pizza to the list friend_pizzas
friend_pizzas.append("prosciutto e mozzarella")
friend_pizzas.insert(0, "carbonara")

# print both the lists
print("My favourite pizzas are:")
for pizza in favourite_pizzas:
    print(f"- {pizza}")

print("\nMy friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")
