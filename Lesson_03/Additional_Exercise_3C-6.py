"""Esercizio 3C-6. Modificare il codice dell'esercizio 3C-4, affinchè si possa scrivere un codice python che consenta all'utente di inserire il nome di un animale ed un habitat. Quando il codice dell'esercizo 3C-4 classifica l'animale inserito in una delle categorie tra mammiferi, rettili, uccelli o pesci, oltre a mostrare un messaggio a schermo, deve salvare tale categoria in una variabile animal_type. Se l'animale inserito non è classificabile in una delle quattro categorie proposte, il valore di animal_type sarà ' "unknown".

Inserire, poi, in un dizionario il nome dell'animale, la categoria a cui esso appartiene (animal_type) e l'habitat.

Verificare con un match statement se l'animale e la categoria a cui esso appartiene possano vivere nell'habitat inserito; dunque, verificare:
- se l'animale può vivere nell'habitat specificato, stampare un messaggio appropriato.
- se l'habitat non è compatibile con l'habitat specificato, stampare un avviso.
- Se l'animale o l'habitat non sono riconosciuti, stampare un messaggio di errore.

Le categorie di classificazione devono essere:
- Mammiferi: cane, gatto, cavallo, elefante, leone, balena, delfino.
- Rettili: serpente, lucertola, tartaruga, coccodrillo.
- Uccelli: aquila, pappagallo, gufo, falco, cigno, anatra, gallina, tacchino.
- Pesci: squalo, trota, salmone, carpa.

Categorie di habitat:
- acqua
- aria
- terra

NOTA.
Il codice deve produrre un risultato sensato, ovvero che l'animale inserito possa effettivamente vivere nell'habitat specificato.
Tenere in considerazione il fatto che alcuni animali tra quelli specificati possono vivere in più di un habitat, mentre altri solo in uno.

Suggeirmento: può essere utile per coprire tutti i possibili casi implementare istruzioni match annidate.
"""


animal_name: str = input("Enter a name of an animal: ").lower()
animal_habitat: str = input(f"Enter the habitat of the animal {animal_name}: ")
animal_type: str = []

mammals: list[str] = ["dog", "cat", "horse", "elephant", "lion", "whale", "dolphin"]
reptiles: list[str] = ["serpent", "lizard", "tortoise", "cocodrille"]
birds: list[str] = ["eagle", "parot", "howl", "falcon", "swan", "hen", "turkey" ]
fishes: list[str] = ["shark", "trout", "salmon", "carp"]

match animal_name:
    case user_animal if user_animal in mammals:
        print(f"{user_animal} is in the category of mammals.")
    case user_animal if user_animal in reptiles:
        print(f"{user_animal} is in the category of reptiles.")
    case user_animal if user_animal in birds:
        print(f"{user_animal} is in the category of birds.")
    case user_animal if user_animal in fishes:
        print(f"{user_animal} is in the category of fishes.")

animal_dict: dict = {"Animal": animal_name, "Habitat": animal_habitat, "Type": animal_type}