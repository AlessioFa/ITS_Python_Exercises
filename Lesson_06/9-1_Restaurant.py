# Exercise 9.1: Restaurant

class Restaurant:
    """Create a class that represents a restaurant"""
    def __init__(self, restaurant_name: str, cousine_type: str) -> None:
        self.restaurant_name = restaurant_name
        self.cousine_type = cousine_type

    def describe_restaurant(self) -> None:
        """Print a summary of the restaurant's information"""
        print(f"Name: {self.restaurant_name}\nType of cousine: {self.cousine_type}")

    def open_restaurant(self) -> None:
        """Print a message indicating that the restaurant is open"""
        print(f"The restaurant is open!\n")



# Create an instance of the Restaurant Class
alta_vela = Restaurant("Altavela", "Fish")

# Call the method to indicate that the restaurants is open
alta_vela.open_restaurant()

# Call the method to descrive the restaurant
alta_vela.describe_restaurant()
