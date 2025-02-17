# Exercise 8-3: T-Shirt

# Define a function that takes two parameters: size (str) and text (str)
def make_shirt(size: str, text: str):
    # Print the size of the shirt and the text to be printed on it
    print(f"This is the size of the shirt: {size}\nThis is going to be the message: {text}")


# Call the function using positional arguments (the order matters)
make_shirt("Xl", "Python is great!")  

# Call the function using keyword arguments (the order doesn't matter here)
make_shirt(text="Python is great!", size="Xl")
