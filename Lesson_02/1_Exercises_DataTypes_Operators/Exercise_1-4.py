# Exercise 1.4

# Initialize a four-digit integer to a variable
number: int = 2024

# Extract and display each digit
thousands: int = number // 1000
hundreds: int = (number % 1000) // 100
tens: int = (number % 100) // 10
units: int = number % 10

# Print each digit on a new line
print(thousands)
print(hundreds)
print(tens)
print(units)
