class Persona:
    
    def __init__(self, name: str, last_name: str, age: int) -> None:

        self.name = name
        self.last_name = last_name
        self.age = age
    
    def displayData(self) -> None:
        print(f"Name: {self.name}\nLast name: {self.last_name}\nAge: {self.age}")


    def getName(self) -> None:
        return self.name
    
    def getLastname(self) -> None:
        return self.last_name
    
    def getAge(self) -> None:
        return self.name
    
    def displayData(self) -> (None):
        print(f"Name: {self.name}\nLast name: {self.last_name}\nAge: {self.age}")
