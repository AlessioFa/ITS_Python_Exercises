"""
Scrivere un programma che permetta all'utente di inserire una serie di parole in input, terminando l'inserimento quando viene digitata la parola "fine" (che non deve essere considerata nell'elaborazione).
Per ogni parola inserita, il programma deve verificare se il primo e l'ultimo carattere sono uguali e visualizzare un messaggio corrispondente.
"""


def word_checker():
    """
    Check words entered by the user.

    Ask the user to enter words until 'fine' is typed.
    For each word, check if it is empty. If not, check if the first
    and last letters are the same and print a message.
    """
    while True:
        user_words: str = input("Enter as many words as you want(type 'fine' to end.): ").lower()

        if len(user_words) == 0:
            print("You entered an empty word, try again.")
            continue

        if user_words == "fine":
            break

        else:
            if user_words[0] == user_words[-1]:
                print(f"First and last letter of the word '{user_words}' are equal.")

            else:
                print(f"First and last letter of the word '{user_words}' are not equal.")


word_checker()
