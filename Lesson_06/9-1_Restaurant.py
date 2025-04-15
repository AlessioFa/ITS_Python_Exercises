# Exercise 9.1: Restaurant

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