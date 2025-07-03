"""
Scrivere un programma in Python che legga dall’utente una serie di nomi di persona (stringhe). L'inserimento dei nomi deve terminare quando l’utente inserisce un nome già inserito in precedenza, oppure sono stati inseriti 30 nomi distinti. Inoltre, si deve porre il vincolo che ciascun nome sia una stringa di lunghezza inferiore a 20 caratteri e che non venga inserita una stringa vuota.

Al termine dell'inserimento, il programma deve:
- stampare quanti nomi sono stati inseriti in totale;
- stampare il nome più lungo tra quelli inseriti;
- stampare la lunghezza del nome più lungo.

Se ci sono più nomi con la stessa lunghezza massima, puoi scegliere uno qualsiasi tra quelli più lunghi.

Esempio:
Inserisci un nome: Dora
Inserisci un nome: Marcella
Inserisci un nome: Teresa
Inserisci un nome: Valentina
Inserisci un nome: Dora
 
Hai inserito 4 nomi distinti.
Il più lungo è Valentina con 9 caratteri.
"""


def word_checker() -> str:

    word_list: list[str] = []

    while True:

        user_word: str = input("Enter a sequence of word: ")

        if len(user_word) >= 20:
            continue

        if not user_word:
            continue

        if user_word in word_list:

            print("The entered word in already in the list!")

            break

        if len(word_list) == 30:

            break

        word_list.append(user_word)

        s_max = max(word_list, key=len)

    print(word_list)

    print(f"You entered {len(word_list)} different names.")
    print(f"The longest is {s_max} with {len(s_max)} characters.")


word_checker()
