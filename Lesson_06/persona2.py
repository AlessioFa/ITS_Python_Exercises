class Persona:
    def __init__(self) -> None:
        
        self.name: str = ""
        self.last_name = ""
        self.age: int = 0

    #def setName(self, Name)

    def displayData(self):
        print(f"Name: {self.name}\nLast name: {self.last_name}\nAge: {self.age}")

    
    def setName(self, name: str) -> None:
        self.name = name
    
    def setLastname(self, last_name: str) -> None:
        self.last_name = last_name
    
    def setAge(self, age: int) -> None:
        if age < 0 or age > 130:
            self.age = 0
        self.age: int = age
