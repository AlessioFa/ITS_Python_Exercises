"""
Scrivere un programma che acquisisca una stringa inserita dall'utente e calcoli il numero totale di spazi
 presenti nella stringa. Il risultato deve essere visualizzato in output.
"""


def space_counter():
    """
    Count the space in a phrase.

    Ask the user for a phrase, count the spaces in it and tells
    how many there are.
    """
    user_word = input("Enter a phrase: ")

    user_spaces = 0

    for letter in user_word:

        if letter == " ":
            user_spaces += 1

        else:
            continue
    
    print(f"There are {user_spaces} spaces in the phrase:\n'{user_word}'")


space_counter()
