class Person:
    
    def __init__(self, name: str, age: int,  ):
        self.name = name
        self.age = age



alice = Person("Alice", 88)
bob = Person("Bob", 22)

print(bob.age)


if alice.age > bob.age:
    print(alice.name)
else:
    print(bob.name)

riccardo = Person("Riccardo", 19)
rebecca = Person("Rebecca", 30)
arjol = Person("Arjol", 58)


people = [alice, bob, riccardo, rebecca, arjol]

min: int = alice.age

min_name = alice.name

for person in people:
    if person.age < min:
        min = person.age

        min_name = person.name

print(f"La persona con l' età più bassa è {min_name}")




class Student:
    def __init__(self, name: str, studyProgram: str, age: int, gender: str):
        self.name = name
        self.studyProgram = studyProgram
        self.age = age
        self.gender = gender

    def printInfo(self):
        print(self.name)
        print(self.studyProgram)
        print(self.age)
        print(self.gender)

riccardo = Student("Riccardo", "Chimica", 30, "M")
rebecca = Student("Rebecca", "Fisica", 30, "F")
arjol = Student("Arjol", "Danza Classica", 58, "M")

riccardo.printInfo()
rebecca.printInfo()
arjol.printInfo()
