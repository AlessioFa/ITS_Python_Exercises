"""Exercise 2 
1. Write a class called Student with the attributes name (str) and
studyProgram (str)
2. Create three instances. One for yourself, one for your left neighbour and one
for our right neighbour.
3. Add a method printInfo that prints the name and studyProgram of a
Student. Test your method on the objects!
4. Modify the code and add age and gender to the attributes. Modify your
printing methods respectively too."""


class Student:
    def __init__(self, name: str, studyProgram: str, age: int, gender: str):
        # Initialize the student object with name, study program, age, and gender
        self.name = name
        self.studyProgram = studyProgram
        self.age = age
        self.gender = gender

    def printInfo(self):
        # Print student information
        print(self.name)
        print(self.studyProgram)
        print(self.age)
        print(self.gender)


# Creating instances of the Student class
alessio = Student("Alessio", "Computer Science", 29, "M")
riccardo = Student("Riccardo", "CyberSecurity", 19, "M")
arjol = Student("Arjol", "Modern Dance", 58, "M")

# Printing information of each student
alessio.printInfo()
riccardo.printInfo()
arjol.printInfo()
