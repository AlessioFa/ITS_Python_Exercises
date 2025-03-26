class Animal:
    def __init__(self, name: str, legs: int) -> None:
        # Initialize the animal object with a name and number of legs
        self.name = name
        self.legs = legs

    def setLegs(self, new_legs: int):
        # Set a new number of legs
        self.legs = new_legs

    def getLegs(self):
        # Return the current number of legs
        return self.legs

    def printInfo(self):
        # Print the animal's name and number of legs
        print(f"Name: {self.name} Legs: {self.legs}")


dog = Animal("dog", 4)
cat = Animal("cat", 4)

print(dog.name)
print(dog.legs)

print(cat.name)
print(cat.legs)


# Directly modifying the attribute
dog.legs = 6
print(dog.legs)


dog.setLegs(5)
print(dog.legs)

# Printing all information
dog.printInfo()
cat.printInfo()
