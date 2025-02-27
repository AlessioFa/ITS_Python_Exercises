"""Esercizio 3C-8. Scrivere un programma in Python che legga una frase di una riga e mostri una delle seguenti risposte:
- "Si" -> se la frase termina con un punto interrogativo (?) ed il numero dei caratteri è pari;
- "No" -> se la frase termina con un punto interrogativo (?) ed il numero dei caratteri è dispari;
- "Wow!" -> se la frase termina con un punto esclamativo (!)
- "Tu dici" seguito dalla frase inserita racchiusa tra doppi apici in tutti gli altri casi.

Expected Output:

frase: di essere bellissimo
Output: Tu dici "di essere bellissimo"

- - - - - - - - - - - - - - - - - - - - - -

frase: ho vinto!
Output: Wow!"""


user_phrase: str = input("Enter a phrase: ").strip()

match user_phrase[-1]:
    case "?":
        if len(user_phrase) % 2 == 0:
            print("Yes")
        else:
            print("No")
    
    case "!":
        print("Wow!")

    case _:
        print(f"You say \"{user_phrase}\"")
