"""Esercizio 3C-7. Si scriva un programma in python che computi la statistica di otto lanci di una moneta.
Per ciascuno dei lanci effettuati, l'utente inserisce "t" o "T" se è uscito "testa", mentre inserisce "c" o "C" se è uscito "croce".
Il programma deve mostrare in output il numero totale e la percentuale dei risultati "testa" e "croce".
NOTA.
Le percentuali devono essere mostrate in output obbligatoriamente con 2 cifre decimali.
Usare il match statement.

Expected Output:

Per ciascun lancio della moneta inserisci "t" o "T" se e' uscito "testa" mentre inserisci "c" o "C" se e' uscito "croce".

Lancio 1: t
Lancio 2: c
Lancio 3: t
Lancio 4: t
Lancio 5: c
Lancio 6: c
Lancio 7: t
Lancio 8: t

Totale "testa": 5
Percentaule "testa": 62.50%

Totale "croce": 3
Percentuale "croce": 37.50%
"""


coin_head: int = 0
coin_cross: int = 0
total_coin_toss: int = 0

while total_coin_toss < 8:
    
    user_coin_toss = input("Toss a coin ( enter c/C for cross, h/H for head):").strip()

    if user_coin_toss not in ["c", "C", "h", "H"]:
        print("You have to enter the right letter!")
        continue

    if user_coin_toss == "c" or user_coin_toss == "C":
        coin_head += 1
        total_coin_toss += 1

    elif user_coin_toss == "h" or user_coin_toss == "h" "H":
        coin_cross += 1
        total_coin_toss += 1

percentace_head: int = (coin_head / total_coin_toss) * 100
percentage_cross: int = (coin_cross / total_coin_toss) * 100

print(f"Total 'head': {coin_head} \nPercentage 'head': {percentace_head}%")
print(f"Total 'cross': {coin_cross} \nPercentage 'cross': {percentage_cross}%") 







coin_head: int = 0
coin_cross: int = 0
total_coin_toss: int = 0

while total_coin_toss < 8:
    user_coin_toss = input("Toss a coin (enter c/C for cross, h/H for head): ").strip()

    
    if user_coin_toss not in ["c", "C", "h", "H"]:
        print("You have to enter the right letter!")
        continue

    match user_coin_toss:
        case "c":
            coin_cross += 1
            total_coin_toss += 1
        case "C":
            coin_cross += 1
            total_coin_toss += 1
        case "h":
            coin_head += 1
            total_coin_toss += 1
        case "H":
            coin_head += 1
            total_coin_toss += 1


percentage_head: int = (coin_head / total_coin_toss) * 100
percentage_cross: int = (coin_cross / total_coin_toss) * 100


print(f"Total 'head': {coin_head} \nPercentage 'head': {percentage_head}")
print(f"Total 'cross': {coin_cross} \nPercentage 'cross': {percentage_cross}")

