# Exercise 2-3: Personal Message

# Initialize a name variable with a string value
name: str = "Eric"

#  Print a personalized message to the person
print(f"Hi,{name} would you like to learn some Python today?")

# In this version, i'm using the input() function to allow the user to provide a name dynamically.

# Initialize a name variable by asking the user for input
name2: str = (input("Insert a name of a person you would like to say hello: "))

# Print a personalized message to the person
print(f"Hi,{name2} would you like to learn some Python today?")
