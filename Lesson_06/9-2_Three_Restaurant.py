# Exercise 9.2: Restaurant

class Restaurant:
    """Create a class that rapresents a restaurant."""
    def __init__(self, restaurant_name: str, cuisine_type: str):
        """Initialize the restaurant with a name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self) -> None:
        """Display a string describing the restaurant's name and cuisine type."""
        print(f"Name: {self.restaurant_name}\nType of cousine: {self.cuisine_type}")
    
    def open_restaurant(self) -> None:
        """Display a string indicating that the restaurants is open. """
        print("The restaurant is open!")


alta_vela = Restaurant("Altavela", "Fish")

print(alta_vela.describe_restaurant())
print(alta_vela.open_restaurant())


villa_crespi = Restaurant("Villa Crespi", "Starred cuisine")

osteria_della_carne = Restaurant("Osteria della carne", "Meat cuisine")

arte_della_pizza = Restaurant("L' arte della pizza", "Pizzeria")

villa_crespi.describe_restaurant()
villa_crespi.open_restaurant()

osteria_della_carne.describe_restaurant()
osteria_della_carne.open_restaurant()

arte_della_pizza.describe_restaurant()
arte_della_pizza.open_restaurant()
