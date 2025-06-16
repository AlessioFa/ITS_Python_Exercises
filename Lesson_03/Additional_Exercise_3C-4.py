"""Esercizio 3C-4. Scrivere un programma in Python che permetta all'utente di inserire il nome di un animale e, utilizzando un match statement, identifichi a quale categoria esso appartiene. L'animale deve essere classificato in una delle seguenti categorie:

- Mammiferi: cane, gatto, cavallo, elefante, leone.
- Rettili: serpente, lucertola, tartaruga, coccodrillo.
- Uccelli: aquila, pappagallo, gufo, falco.
- Pesci: squalo, trota, salmone, carpa.

Se l'animale non appartiene a nessuna delle categorie sopra elencate,  mostrare un messaggio indicante che il programma non è in grado di classificare l'animale inserito.

Suggerimento: Utilizzare una lista per ognuna della quattro categorie."""


user_input: str = input("Enter a name of an animal: ").lower()


match user_input:
    case user_input if user_input == "dog" or "cat" or "horse" or "elephant" or "lion":
        print(f"{user_input} is in the mammals category.")

    case user_input if user_input == "serpent" or "lizard" or "tortoise" or "cocodrille":
        print(f"{user_input} is in the reptiles category.")

    case user_input if user_input == "eagle" or "parot" or "howl" or "falcon":
        print(f"{user_input} is in the category of birds.")

    case user_input if user_input == "shark" or "trout" or "salmon" or "carp":
        print(f"{user_input} is in the category of fishes.")



# Same exercise using lists

user_animal: list[str] = input("Enter a name of an animal: ").lower()

mammals: list[str] = ["dog", "cat", "horse", "elephant", "lion"]
reptiles: list[str] = ["serpent", "lizard", "tortoise", "cocodrille"]
birds: list[str] = ["eagle", "parot", "howl", "falcon"]
fishes: list[str] = ["shark", "trout", "salmon", "carp"]

match user_animal:
    case user_animal if user_animal in mammals:
        print(f"{user_animal} is in the category of mammals.")

    case user_animal if user_animal in reptiles:
        print(f"{user_animal} is in the category of reptiles.")

    case user_animal if user_animal in birds:
        print(f"{user_animal} is in the category of birds.")

    case user_animal if user_animal in fishes:
        print(f"{user_animal} is in the category of fishes.")
