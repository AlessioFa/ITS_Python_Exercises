"""Base: Creazione di una Classe Semplice
Obiettivo: Creare una classe Car con attributi di base e un metodo per mostrare le informazioni dell'auto.

Istruzioni:

Crea una classe Car con gli attributi:

brand (marca dell'auto, es. "Toyota")

model (modello dell'auto, es. "Yaris")

year (anno di produzione, es. 2022)

Aggiungi un metodo display_info() che stampa le informazioni dell'auto.

Crea un'istanza della classe e chiama il metodo."""


class Car:
    def __init__(self, brand: str, model: str, year: int) -> str:
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        return f"Brand: {self.brand.title()}\nModel: {self.model.title()}\nYear: {self.year}"
    

info = Car("Toyota", "Yaris", 2025)

print(info.display_info())
