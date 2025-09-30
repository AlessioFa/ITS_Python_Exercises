"""
Scrivere un programma che acquisisca una stringa inserita dall'utente e generi una nuova stringa che corrisponda alla versione invertita della stringa originale. Il programma deve poi visualizzare la stringa ottenuta in output. Per risolvere il problema non si deve utilizzare alcun tipo di funzione, ma esclusivamente i cicli.
"""


def string_inverter():
    """
    Reverse a string entered by the user.

    The function asks the user to input a phrase and prints it in reverse order.
    """
    inverted_phrase: str = ""

    user_phrase = input("Enter a phrase: ")

    for letter in user_phrase:
        inverted_phrase = letter + inverted_phrase
    
    print(inverted_phrase)


string_inverter()
