numbers: list[int] = [1, 2, 3, 4]

for n in numbers:

    print(n * n)

first_compr: list[int] = [n * n for n in numbers]

print(first_compr)


"""Numeri al quadrato
Data una lista di numeri [1, 2, 3, 4, 5], crea una nuova lista con i quadrati dei numeri."""

numbers1: list[int] = [1, 2, 3, 4, 5]

quadratic_numbers: list[int] = [n ** 2 for n in numbers1]

print(quadratic_numbers)


"""Solo numeri pari
Crea una lista con solo i numeri pari dalla stessa lista."""

numbers2: list[int] = [1, 2, 3, 45, 654, 34, 232, 443, 9, 92]

even_numbers: list[int] = [n for n in numbers2 if n % 2 == 0]

print(even_numbers)


"""
Lunghezza delle parole
Data una lista di parole ["apple", "banana", "kiwi"], crea una lista con la lunghezza di ogni parola."""

words: list[str] = ["apple", "banana", "kiwi"]

for word in words:
    print(len(word), end="")
