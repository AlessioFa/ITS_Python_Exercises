"""ntermedio: Contatore di Istanze
Obiettivo: Creare una classe che tenga traccia del numero di oggetti creati.

Istruzioni:

Crea una classe Dog con gli attributi name e age.

Aggiungi una variabile di classe dog_count che tiene traccia del numero di istanze create.

Ogni volta che un oggetto Dog viene creato, dog_count deve essere aggiornato.

Aggiungi un metodo di classe total_dogs() che restituisce il numero totale di cani creati.

Crea alcune istanze di Dog e mostra il conteggio."""


class Dog:
    dog_count = 0

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Dog.dog_count += 1
    
    @classmethod
    def total_dogs(cls):
        return Dog.dog_count
    
bassotto = Dog("Rudy", 12)

levriero = Dog("Fernando", 5)

boxer = Dog("Ernesto", 3)

print(bassotto.total_dogs())