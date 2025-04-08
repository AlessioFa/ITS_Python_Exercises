"""Nel gioco del Blackjack, il valore di una mano è determinato dalla somma dei valori delle carte. Ogni carta ha un valore compreso tra 2 e 11 inclusi.

    Il valore numerico delle carte (da 2 a 10) è equivalente al loro valore nominale.
    Le figure (Jack, Regina, Re) non sono incluse in questo esercizio e vengono ignorate.
    L'Asso (valore 11) può valere 1 o 11, a seconda di quale sia più favorevole al giocatore:
        Se la somma della mano supera 21, e c'è almeno un asso valutato 11, quell'asso deve essere considerato 1 per evitare il "bust" (superare 21).

Scrivi una funzione che prende in input una lista di interi rappresentanti i valori delle carte e restituisce il valore totale della mano secondo le regole del Blackjack."""


def blackjack_hand_total(cards: list[int]) -> int:
    
    for n in cards:
        if sum(cards) > 21:
            if n == 11:
                cards[cards.index(11)] = 1
        
        if sum(cards) <  21:
            if n == 1:
                n == 11
        
        if sum(cards) > 21:
            if 1 in cards and 11 in cards:
                cards[cards.index(11)] = 1
            
    
    return(sum(cards))

print(blackjack_hand_total([1, 10, 11]))         

