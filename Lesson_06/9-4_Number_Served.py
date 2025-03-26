# Exercise 9-4 : Number Served

class Restaurant:
    def __init__(self, restaurant_name: str, cousine_type: str, number_served=0):
        self.restaurant_name = restaurant_name
        self.cousine_type = cousine_type
        self.number_served = number_served

    def describe_restaurant(self):
        return f"Name: {self.restaurant_name}\nType of cousine: {self.cousine_type}\nActual served customers: {self.number_served}"

    def open_restaurant(self):
        return f"The restaurant is open!"

    def increment_number_served(self):
        return self.number_served


alta_vela = Restaurant("Altavela", "Fish")

print(alta_vela.describe_restaurant())

print(alta_vela.open_restaurant())

restaurant = Restaurant("My restaurant", "barbeque", 15)

print(restaurant.describe_restaurant())
