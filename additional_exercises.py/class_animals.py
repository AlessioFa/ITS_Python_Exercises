"""Crea una classe Animal con:

Attributo name

Metodo speak() che restituisce "Some sound"

Crea due classi derivate Dog e Cat che ereditano da Animal:

Dog.speak() deve restituire "Woof!"

Cat.speak() deve restituire "Meow!"

Crea istanze di Dog e Cat e chiama speak()."""


class Animal:
    def __init__ (self, name: str) -> str:
        self.name = name
    
    def speak(self):
        return "Some sound!"
    
class Dog(Animal):

    def speak(self):
        return "Woof!"
    
class Cat(Animal):

    def speak(self):
        return "Meow"
    


