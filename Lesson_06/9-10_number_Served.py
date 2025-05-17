# Exercise 9-4 : Number Served

class Restaurant:
    """Create a class that represents a restaurant."""
    def __init__(self, restaurant_name: str, cousine_type: str, number_served=0):
        """Initialize the restaurant with a name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cousine_type = cousine_type
        self.number_served = number_served

    def describe_restaurant(self) -> None:
        """Display the restaurant's characteristic."""
        print(f"Name: {self.restaurant_name}")
        print(f"Type of cuisine: {self.cousine_type}")
        print(f"Customers served: {self.number_served}\n")

    def open_restaurant(self) -> None:
        """Display a message indicating that the restaurant is open."""
        return f"The restaurant is open!"

    def set_number_served(self, number_served: int) -> None:
        """Set the number of customers the restaurant has served."""
        self.number_served = number_served

    def increment_number_served(self, number: int) -> None:
        """Increment the number of customers served by a given number."""
        self.number_served += number


# Create an instance of the Restaurant class
alta_vela = Restaurant("Altavela", "Fish")

# Print initial details
alta_vela.describe_restaurant()

# Change the number of customers served and print again
alta_vela.set_number_served(50)
print("After setting number served:")
alta_vela.describe_restaurant()

# Increment the number of customers served and print again
alta_vela.increment_number_served(20)
print("After incrementing number served:")
alta_vela.describe_restaurant()
