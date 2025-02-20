# Exercise 5-2: More Conditional Tests
car: str = "subaru"
fruit: str = "banana"
age: int = 25
number: int = 10
fruits: list = ["apple", "banana", "orange"]
animals: list = ["lion", "tiger", "leopard"]

# Test equality and inequality with strings
# Test 1: Check if car is equal to "subaru"
print("Is car == 'subaru'? I predict True.")
print(car == "subaru")

# Test 2: Check if car is equal to "audi"
print("\nIs car == 'audi'? I predict False.")
print(car == "audi")

# Test the lower() method
# Test 3: Check if fruit in lowercase is equal to "banana"
print("\nIs fruit.lower() == 'banana'? I predict True.")
print(fruit.lower() == "banana")

# Test 4: Check if fruit in lowercase is equal to "apple"
print("\nIs fruit.lower() == 'apple'? I predict False.")
print(fruit.lower() == "apple")

# Perform numerical tests: equality, inequality, greater than, and less than
# Test 5: Check if number is greater than 5
print("\nIs number > 5? I predict True.")
print(number > 5)

# Test 6: Check if number is greater than 15
print("\nIs number > 15? I predict False.")
print(number > 15)

# Test 7: Check if age is equal to 25
print("\nIs age == 25? I predict True.")
print(age == 25)

# Test 8: Check if age is less than or equal to 20
print("\nIs age <= 20? I predict False.")
print(age <= 20)

# Test logical operators
# Test 9: Check if both age > 20 and number < 15 are true
print("\nIs age > 20 and number < 15? I predict True.")
print(age > 20 and number < 15)

# Test 10: Check if age is greater than 30 or number is greater than 15
print("\nIs age > 30 or number > 15? I predict False.")
print(age > 30 or number > 15)

# Test membership in a list
# Test 11: Check if "banana" is in the fruits list
print("\nIs 'banana' in fruits? I predict True.")
print("banana" in fruits)

# Test 12: Check if "grape" is in the fruits list
print("\nIs 'grape' in fruits? I predict False.")
print("grape" in fruits)

# Test 13: Check if "cat" is not in the animals list
print("\nIs 'cat' not in animals? I predict True.")
print("cat" not in animals)

# Test 14: Check if "tiger" is not in the animals list
print("\nIs 'tiger' not in animals? I predict False.")
print("tiger" not in animals)
