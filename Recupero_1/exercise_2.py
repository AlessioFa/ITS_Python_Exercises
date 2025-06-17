"""Esercizio 2.
 
Scrivere un programma Python che legge in input prima un intero x positivo e poi una sequenza di interi positivi. Se l'utente inserisce il numero 0, allora la sequenza deve terminare.

Per il numero x e per ogni numero della sequenza inserita, effettuare il controllo che il numero inserito sia effettivamente un intero e forzare l'utente ad inserire un numero intero positivo nel caso in cui questa condizione non venga rispettata.
Trovare una soluzione che eviti di scrivere codice duplicato per effettuare questa serie di controlli.
Suggerimento: per controllare che un numeri sia intero, usare la funzione is_integer().

Determinato il numero x e la sequenza di interi positivi, il programma deve produrre in output:
 

    stampare la sequenza

    Il numero occ di occorrenze di x, ovvero  il numero di volte in cui appare x nella sequenza;

    La posizione pos del primo valore uguale a x.

    La somma di tutti i valori diversi da x;


Ad esempio, se l'utente inserisce come valore x il numero 3 e poi immette la sequenza: 7; 5; 1; 3; 3; 3; 11; 2; 3; 3; 0
 
il programma dovra' scrivere in output:

    stampare in output la sequenza

    Il numero 3 compare 5 volte nella sequenza (attenzione all'output se il numero compare 1 sola volta!)

    Il numero 3 compare per la prima volta in posizione 3 nella sequenza

    La somma dei valori della sequenza diversi da 3 e' 26

"""


def check_is_int():
    """Ask the user for a number until a positive integer is entered. 0 ends the input sequence."""
    while True:

        x: float = float(input("Enter a number (0 to end the program): "))

        if not x.is_integer():
            print("You have to enter an integer value.")
            continue

        elif x < 0:
            print("The entered number is below 0. Enter a positve value.")

        else:
            return int(x)


x = check_is_int()

# sequence where the numbers are going to be stored
numbers_sequence: list[int] = []

while True:

    user_number = check_is_int()

    if user_number == 0:
        break

    else:
        numbers_sequence.append(user_number)


print(f"The sequence is: {numbers_sequence}")

# count how many times 'x' appears in the sequence
count_appearence_num: int = numbers_sequence.count(x)

if count_appearence_num == 1:
    print(f"The number {x} appears {count_appearence_num} time in the sequence.")

else:
    print(f"The number {x} appears {count_appearence_num} times in the sequence.")

# find the first occurence where 'x' appears in the sequence
first_occurrence_num: int = numbers_sequence.index(x)

print(f"The number {x} in the sequence appears at position {first_occurrence_num} for the first time.")

value_to_sum = []

for num in numbers_sequence:
    if num != x:
        value_to_sum.append(num)
    # [num for num in numbers_sequence if num != x]
    
print(f"The sum of all value in the sequence, different from {x}, is: {sum(value_to_sum)}")
