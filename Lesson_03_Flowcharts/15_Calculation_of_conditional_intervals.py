"""Progettare un algoritmo che chieda all’utente di inserire un valore intero n.
L'algoritmo deve:

    Verificare se n è compreso tra 1 e 100:
        se sì, calcolare e mostrare la somma di tutti i numeri pari compresi tra 1 e n.
    Verificare se n è 0 o negativo:
        Se sì, mostrare un messaggio di errore e terminare.
    Altrimenti, calcolare e mostrare la somma di tutti i numeri dispari compresi tra 1 e n.
"""

while True:
        n: int = int(input("Enter a n value: "))
    
        if n > 0 and n <= 100:
            sum = 0
            
            for i in range(n+1):
                
                if i % 2 == 0:
                    sum += i
                    i += 1
        
            print(sum)
        
        elif n == 0 or n < 0:
            print("Error.")
        else:
            sum = 0

            for i in range(n+1):

                if i % 2 != 0:
                    sum += i
                
            print(sum)
