# Exercise 4-11: My Pizzas, Your Pizzas

# Lista delle pizze preferite
favourite_pizzas: list[str] = ["margherita", "sausages and potatoes", "sausages and tomatoes"]

# Creiamo una copia della lista favourite_pizzas per friend_pizzas
friend_pizzas = favourite_pizzas.copy()

# Aggiungiamo pizze diverse alla lista friend_pizzas
friend_pizzas.append("prosciutto e mozzarella")
friend_pizzas.insert(0, "carbonara")

# Stampiamo entrambe le liste
print("My favourite pizzas are:")
for pizza in favourite_pizzas:
    print(f"- {pizza}")

print("\nMy friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")
