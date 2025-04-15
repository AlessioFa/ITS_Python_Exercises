# from the module person.py , import the Person class

from persona import Persona

#  student class inherit form Person class
class Studente(Persona):
    """Attribute from Person class , cause Student inherit from Person
    self.name: str
    self.lastname: str
    self.age: int

    Student Attributes
    self.freshman(matricola): str
    
    
    
    """

    def __init__(self, name: str, lastname: str, age: int, matricola: int):
        super().__init__(name, lastname, age)

        # instruction that initialize an object of Student's class
        self.setMatricola(matricola)

        # method that sets the value of self.matricola value
    def setMatricola(self, matricola: str) -> None:
        if matricola:
            self.matricola = matricola
        else:
            print("\nErrore! La matricola non puo essere rappresentata da una stringa vuota.")
    
    # getter methods

    # method that returns the self.matricola's value
    def getMatricola(self) -> str:
        return self.matricola
