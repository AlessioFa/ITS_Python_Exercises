"""Scrivi una funzione che calcoli i fattori primi di un numero intero positivo n.

Un fattore primo di n è un numero primo che divide esattamente n (cioè senza resto), e la cui moltiplicazione in sequenza restituisce n. Un numero può avere lo stesso fattore primo più volte.
Cosa sono i fattori primi?

I fattori primi di un numero sono numeri primi che, moltiplicati tra loro, danno come risultato proprio quel numero.

🔹 Esempio:
Il numero 60 si può scomporre in: 2 × 2 × 3 × 5 → cioè: 2² × 3 × 5

🔎 Suggerimento:
Prova a pensare a come potresti "smontare" un numero dividendolo più volte, iniziando dal numero primo più piccolo possibile. Cosa succede ogni volta che la divisione ha resto 0? E cosa potresti fare quando non lo è più?

For example:

print(prime_factors(4))  output [2,2]
print(prime_factors(60))  output [2, 2, 3, 5]

"""

def prime_factors(n: int) -> list[int]:
    factors = []  
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    i = 3
    while i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i  
        i += 2  

    if n > 2:
        factors.append(n)

    return factors

print(prime_factors(60))

	

