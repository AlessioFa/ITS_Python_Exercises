# Exercise 8-4: Large Shirts

# Define the function with default values for size and text
def make_shirts(size: str = "L", text: str = "I love Python!"):
    # Print the size and the message of the shirt
    print(f"This is the size of the shirt: {size}\nThis is going to be the message: {text}")


# Call the function without passing any arguments: it will use the default values
make_shirts()

# Call the function passing only the size (size), keeping the default text
make_shirts(size="M")

# Call the function passing both the size and a custom text
make_shirts(size="XL", text="Rule the world!")
