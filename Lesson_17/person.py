class Person:
    """
    A simple class that represents a person with a first name, last name, and age.
    Provides methods to set and get personal information.
    """

    def __init__(self, first_name: None | str, last_name: None | str):
        
        if isinstance(first_name, str):
            self.first_name = first_name
   
        else:
            self.first_name = None
            print("The entered name is not a string!")

        if isinstance(last_name, str):
            self.last_name = last_name

        else:
            self.last_name = None
            print("The entered last name is not a string!")

        if isinstance(first_name, str) and isinstance(last_name, str):
            self.age = 0

        else:
            self.age = None
    
    def setName(self, first_name: str):

        if isinstance(first_name, str):
            self.first_name = first_name
        
        else:
            print("The entered name is not a string!")
    
    def setLastName(self, last_name: str):

        if isinstance(last_name, str):
            self.last_name = last_name
        
        else:
            print("The entered last name is not a string!")
    
    def setAge(self, age: int):

        if isinstance(age, int):
            self.age = age
        
        else:
            print("The age must be an integer!")
    
    def getName(self) -> str:
        return self.first_name
    
    def getLastName(self) -> str:
        return self.last_name
    
    def getAge(self) -> int:
        return self.age
    
    def greet(self) -> str:
        print(f"Hi, I'm {self.first_name} {self.last_name}! I'm {self.age} years old!")



