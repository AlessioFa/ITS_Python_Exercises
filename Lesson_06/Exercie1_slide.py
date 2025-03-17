"""Exercise 1
1. Copy the code and print the age of
bob (using the dot notation)
2. Create an if-statement that prints
the name of the oldest of the two
Persons
3. Create three other Persons. Make
a list called people with all 5
Persons.
4. Make a loop that finds and prints
the youngest person’s name"""

# Define a class named Person that stores 2 attributes: name and age
class Person:

    # The __init__ method initializes the attributes for each instance
    def __init__(self, name: str, age: int):
        # The 'self' keyword refers to the current object
        self.name = name  # Attribute to store the name of the person
        self.age = age    # Attribute to store the age of the person

# Create instances (objects) of the Person class
alessio = Person("Alessio F.", 29)   # Instance for Alessio, 29 years old
riccardo = Person("Riccardo L.", 19)  # Instance for Riccardo, 19 years old

# Print the age of Alessio
print(alessio.age)

# Variable to store the maximum age
max_age: int = 0

# Compare the ages of Riccardo and Alessio to determine the greater one
if riccardo.age > alessio.age:
    max_age = riccardo.age  # Riccardo is older
else:
    max_age = alessio.age  # Alessio is older or the same age

# Print the greater age
print("The greater age is", max_age)

# Additional Person instances
federico = Person("Federico R.", 29)
arjol = Person("Arjol J.", 58)
rebecca = Person("Rebecca D.R", 25)

# List containing all the Person instances created
people: list = [alessio, riccardo, federico, arjol, rebecca]

# Initialize the youngest person's age as Riccardo's age
young_person = riccardo.age

# Loop through all people and find the youngest
for person in people:
    if person.age < young_person:  # Compare each person's age
        young_person = person.age  # Update youngest age


print(young_person)  # This will only print the youngest age, not the person's name

# Correcting the logic to print the name of the youngest person:
youngest_person_name = riccardo.name

for person in people:
    if person.age < young_person:
        young_person = person.age
        youngest_person_name = person.name  # Store the name of the youngest person

print(youngest_person_name)
