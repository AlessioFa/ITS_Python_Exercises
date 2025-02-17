# Exercise 5-1: Conditional Tests

car: str = "subaru"
age: int = 25
temperature: int = 20
height: int = 180
number: int = 10
fruits: list[str] = ["apple", "banana", "orange"]

# Test 1 - True: car is equal to "subaru"
print("Is car == 'subaru'? I predict True.")
print(car == "subaru")

# Test 2 - False: car is not equal to "audi"
print("\nIs car == 'audi'? I predict False.")
print(car == "audi")

# Test 3 - True: age is greater than 18
print("\nIs age > 18? I predict True.")
print(age > 18)

# Test 4 - False: age is not less than 18
print("\nIs age < 18? I predict False.")
print(age < 18)

# Test 5 - True: temperature is equal to 20
print("\nIs temperature == 20? I predict True.")
print(temperature == 20)

# Test 6 - False: height is not less than 170
print("\nIs height < 170? I predict False.")
print(height < 170)

# Test 7 - True: number is not equal to 5
print("\nIs number != 5? I predict True.")
print(number != 5)

# Test 8 - False: "grape" is not in the fruits list
print("\nIs 'grape' in fruits? I predict False.")
print("grape" in fruits)

# Test 9 - True: "banana" is in the fruits list
print("\nIs 'banana' in fruits? I predict True.")
print("banana" in fruits)

# Test 10 - False: both age > 30 and height > 190 are false
print("\nIs age > 30 and height > 190? I predict False.")
print(age > 30 and height > 190)
