class Animal:
    def __init__(self, name: str, legs: int) -> str | int:
        self.name = name
        self.legs = legs

    def setLegs(self, new_legs: int):
        self.legs = new_legs

    def getLegs(self):
        return self.legs

    def printInfo(self):
        print(f"Name: {self.name} Legs: {self.legs}")


dog = Animal("dog", 4)
cat = Animal("cat", 4)

print(dog.name)
print(dog.legs)

print(cat.name)
print(cat.legs)

dog.legs = 6
print(dog.legs)


dog.setLegs(5)
print(dog.legs)

dog.printInfo()
cat.printInfo()
