# Exercise 3-8: Seeing the World

# Creating the locations list 
locations: list[str] = ["Cali", "Buenaventura", "Sidney", "Madagascar", "Sudafrica"]

# Display the list in alphabetical order
print(f"Alphabetical order:{sorted(locations)}")

# Show the list is stil in it's original order
print(f"Original order after sorted(): {locations}")

# Print the list in reverse alphabetical order using sorted() with reverse=True
(print(f"Reverse alphabetical order:{sorted(locations, reverse=True)}"))

# Show the list is still in it's original order
print(locations)

locations.reverse()

print(locations)
