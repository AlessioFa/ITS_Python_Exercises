# Exercise 3-10: Every function

# Initialize the list with cities
cities: list[str] = ["Copenaghen", "Cracovia", "Bruges", "Edimburgo", "Valencia"]

# Add "Bucharest" to the list
cities.append("Bucharest")

# Print the updated list
print(cities)

# Remove "Cracovia" from the list
cities.remove("Cracovia")

# Print the list after removal
print(cities)

# Remove the first element (index 0)
cities.pop(0)

# Print the list after popping
print(cities)

# Sort the list in ascending order
cities.sort()

# Print the sorted list
print(cities)

# Sort the list in descending order
cities.sort(reverse=True)

# Print the list after sorting in reverse
print(cities)

# Reverse the list order
cities.reverse()

# Print the reversed list
print(cities)

# Insert "Buenaventura" at the beginning of the list
cities.insert(0, "Buenaventura")

# Print the list after insertion
print(cities)

# Count how many times "Valencia" appears in the list
print(cities.count("Valencia"))

# Create a sublist with the first two cities
sublist = cities[0:2]

# Print the sublist
print(sublist)

# Create a new list of cities to extend with
cities_2: list[str] = ["Amburgo", "Porto", "Helsinki"]

# Extend the list with new cities
cities.extend(cities_2)

# Print the extended list
print(cities)

# Find the index of "Amburgo"
print(cities.index("Amburgo"))

# Loop through and print each city in the list
for city in cities:
    print(city)

# Eliminate the list cities
del (cities)

print(cities_2)
