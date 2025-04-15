# Exercise 9-5: Login Attemps

class User:
    """Create a class that represents a user."""
    
    def __init__(self, first_name: str, last_name: str, age: int, gender: str):
        """Initialize the user's information and set login_attempts to 0."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0  # Default login attempts is 0

    def describe_user(self) -> None:
        """Print a summary of the user's information."""
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Login attempts: {self.login_attempts}\n")

    def greet_user(self) -> None:
        """Print a greeting to the user."""
        print(f"Hello {self.first_name}, welcome to the server!\n")

    def increment_login_attempts(self) -> None:
        """Increment the number of login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self) -> None:
        """Reset login attempts to 0."""
        self.login_attempts = 0


# Create a user instance
user_1 = User("Elise", "Poppins", 33, "F")

# Show initial state
user_1.describe_user()

# Increment login attempts several times
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()

# Print the current number of login attempts
print(f"Login attempts after incrementing: {user_1.login_attempts}\n")

# Reset login attempts
user_1.reset_login_attempts()

# Print again to confirm it's been reset
print(f"Login attempts after reset: {user_1.login_attempts}")
