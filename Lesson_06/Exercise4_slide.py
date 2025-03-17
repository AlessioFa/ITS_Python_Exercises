class Food:
    def __init__(self, name: str, price: int, description: str):
        self.name = name
        self.price = price
        self.description = description


class Menù:
    def __init__(self, foods=None):
        # Initialize Menu with a list of Food objects (default empty list)
        if foods is None:
            foods = []
        
        self.foods = foods
    
    def addFood(self, food: str):
        # Add a Food object to the menu
        self.foods.append(food)
    
    def removeFood(self, food):
        # Remove a Food object from the menu if it exists
        if food in self.foods:
            self.foods.remove(food)
        else:
            print(f"{food.name} not found in the menù.")
    
    def printPrices(self):
         # Print the name and price of each food item on the menu
        for food in self.foods:
            print(f"{food.name}: {food.price}")

    def getAverageprice(self):
        if not self.foods:
            return 0
        total_price = sum(food.price for food in self.foods)
        return total_price / len(self.foods)


pizza = Food("Pizza", 8, "Pizza is a traditional Italian dish.")
tiramisù = Food("Tiramisù", 6, "Tiramisu is a classic Italian dessert.")
pasta = Food("Pasta", 13, "Pasta is a traditional Italian dish made from durum wheat.")

print(pizza.name)
print(pizza.price)

menù = Menù()
menù.addFood(pizza)
menù.addFood(pasta)
menù.addFood(tiramisù)

# Print the food items in the menu
for food in menù.foods:
    print(f"{food.name}: {food.price}£")

# Remove an item and printing the updated menu
menù.removeFood(tiramisù)
for food in menù.foods:
    print(f"{food.name}: {food.price}")


menù.printPrices()

average_price = menù.getAverageprice()
print(f"Average price: {average_price:.2f}£")
