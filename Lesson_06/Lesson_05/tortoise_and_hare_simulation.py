""" Requisiti del Codice:
- Utilizzare il modulo random per la generazione dei numeri casuali.
- Definire e utilizzare:
    - una funzione per visualizzare le posizioni sulla corsia di gara,
    - una funzione per calcolare la mossa della tartaruga,
    - una funzione per calcolare la mossa della lepre.
- Implementare un loop per simulare i tick dell'orologio. Ad ogni tick, calcolare le mosse, mostrare la posizione sulla corsia di gara, e determinare l'eventuale fine della gara."""

# usare massimo 3 funzioni

import random

print(f"'BANG!!! AND THEY'RE OFF!!!!!\n\n")

tortoise_start_position:int = 1

hare_start_position: int = 1

path: int = list(range(1, 71))


def position():
    print(f"The current position of tortoise is {tortoise_start_position}\nThe current position of the hare is: {hare_start_position}")


actual_position = position()

def tortoise_movement(current_pos: int):
    move =random.randint(1, 10)

    if 1 <= move <= 5:
        return current_pos + 5
    elif  6 <= move <= 7:
        return max(1, current_pos - 6)


clock = 999

while True:

    
    
















