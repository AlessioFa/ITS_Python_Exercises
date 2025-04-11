""" Requisiti del Codice:
- Utilizzare il modulo random per la generazione dei numeri casuali.
- Definire e utilizzare:
    - una funzione per visualizzare le posizioni sulla corsia di gara,
    - una funzione per calcolare la mossa della tartaruga,
    - una funzione per calcolare la mossa della lepre.
- Implementare un loop per simulare i tick dell'orologio. Ad ogni tick, calcolare le mosse, mostrare la posizione sulla corsia di gara, e determinare l'eventuale fine della gara."""

# usare massimo 3 funzioni

import random


def position(tortoise_pos, hare_pos):
    print(f"The current position of tortoise is {tortoise_pos}\nThe current position of the hare is: {hare_pos}")


position()


def tortoise_movement(current_pos: int):
    move = random.randint(1, 100)

    if 1 <= move <= 50:
        current_pos += 3

    elif 51 <= move <= 70:
        current_pos = max(1, current_pos - 6)

    else:
        current_pos += 1

    return min(current_pos, 70)


def hare_movement(current_pos):
    move = random.randint(1, 100)

    if 1 <= move <= 20:
        pass

    elif 21 <= move <= 40:
        current_pos += 9

    elif 41 <= move <= 50:
        current_pos = max(1, current_pos - 12)

    elif 51 <= move <= 80:
        current_pos += 1

    else:
        current_pos = max(1, current_pos - 2)

    return min(current_pos, 70)


tortoise_pos: int = 1

hare_pos: int = 1


print(f"'BANG!!! AND THEY'RE OFF!!!!!\n")