# Exercise 9-3: Users

class User:
    """Create a class that represents a user."""
    def __init__(self, first_name: str, last_name: str, age: int, gender: str):
        """Initialize the user's attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self) -> None:
        """Display a summary of user's information."""
        print(f"These are all the user's information:\nFirst name: {self.first_name}\nLast name: {self.last_name}\nAge: {self.age}\nGender: {self.gender}\n")

    def greet_user(self):
        """Display a personalized welcome message."""
        print(f"Hello, {self.first_name} {self.last_name}! It's great to see you here.\n")


user_1 = User("Elise", "Poppins", 33, "F")
user_2 = User("Erik", "Ball", 29, "M")
user_3 = User("Richard", "Mc Castle", 22, "M")

user_1.greet_user()
user_1.describe_user()

user_2.greet_user()
user_2.describe_user()

user_3.greet_user()
user_3.describe_user()
