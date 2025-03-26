# Exercise 9-3: Users

class User:
    def __init__(self, first_name: str, last_name: str, age: int, gender: str):
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
    
    def describe_user(self):
        return f"First name: {self.first_name}\nLast name: {self.last_name}\nAge: {self.age}\nGender: {self.gender}\n"

    def greet_user(self):
        return f"Hello {self.first_name}, welcome to the server!"
    

user_1 = User("Elise", "Poppins", 33, "F")
user_2 = User("Erik", "Ball", 29, "M")
user_3 = User("Richard", "Mc Castle", 22, "M")

print(user_1.describe_user())
print(user_2.describe_user())
print(user_3.describe_user())
