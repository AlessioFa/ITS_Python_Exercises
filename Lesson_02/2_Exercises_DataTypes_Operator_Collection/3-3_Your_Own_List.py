# Exercise 3-3: Your Own List

# Initialize a list containing different modes of transportation
transport_modes: list[str] = ["Yamaha motorcycle", "MV Augusta", "Bmw m4 Competition"]

# Display each message using indexing
print(f"One day i'm going to own a {transport_modes[0]}!")
print(f"One day i'm going to own a {transport_modes[1]}!")
print(f"One day i'm going to own a {transport_modes[2]}!\n")


# Making the same exercise using for cicle
# Iterate through the list and print a personalized message for each mode of transportation
for mode in transport_modes:
    print(f"One day i'm going to own a {mode}!")
