# Exercise 9-5: Login Attemps

class User:
    def __init__(self, first_name: str, last_name: str, age: int, gender: str, login_attemps=0):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attemps = login_attemps

    def describe_user(self):
        return f"First name: {self.first_name}\nLast name: {self.last_name}\nAge: {self.age}\nGender: {self.gender}\nLogin attempts: {self.login_attemps}\n"

    def greet_user(self):
        return f"Hello {self.first_name}, welcome to the server!"

    def increment_login_attemps(self):
        self.login_attemps += 1

    def reset_login_attemps(self):
        self.login_attemps = 0


user_1 = User("Elise", "Poppins", 33, "F", 0)
user_2 = User("Erik", "Ball", 29, "M")
user_3 = User("Richard", "Mc Castle", 22, "M")

print(user_1.describe_user())
print(user_2.describe_user())
print(user_3.describe_user())


user_1.increment_login_attemps()
user_1.increment_login_attemps()
user_1.increment_login_attemps()
user_1.increment_login_attemps()
user_1.increment_login_attemps()

print(user_1.login_attemps)

print(user_1.describe_user())

user_1.reset_login_attemps()

print(user_1.login_attemps)
