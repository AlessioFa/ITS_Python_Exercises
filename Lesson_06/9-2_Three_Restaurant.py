# Exercise 9.2: Restaurant

class Restaurant:
    def __init__(self, restaurant_name: str, cousine_type: str):
        self.restaurant_name = restaurant_name
        self.cousine_type = cousine_type
    
    def describe_restaurant(self):
        return f"Name: {self.restaurant_name}\nType of cousine: {self.cousine_type}"
    
    def open_restaurant(self):
        return f"The restaurant is open!"


alta_vela = Restaurant("Altavela", "Fish")

print(alta_vela.describe_restaurant())
print(alta_vela.open_restaurant())


villa_crespi = Restaurant("Villa Crespi", "Starred cousine")

osteria_della_carne = Restaurant("Osteria della carne", "Meat cousine")

arte_della_pizza = Restaurant("L' arte della pizza", "Pizzeria")

print(villa_crespi.describe_restaurant())
print(villa_crespi.open_restaurant())

print(osteria_della_carne.describe_restaurant())
print(osteria_della_carne.open_restaurant())

print(arte_della_pizza.describe_restaurant())
print(arte_della_pizza.open_restaurant())
