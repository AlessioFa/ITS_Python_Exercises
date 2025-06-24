from string import ascii_lowercase, ascii_uppercase
"""Cifrario di Cesare
Il cifrario di Cesare è un antico metodo crittografico che rende alcune informazioni nascoste
a chi non possiede la chiave per decifrarle.
Immagina l’alfabeto come una lista ordinata di lettere (puoi importare la lista delle lettere
dell’alfabeto minuscole scrivendo from string import ascii_lowercase
Ogni lettera ha una posizione in questa lista:
● a è 1
● b è 2
● j è 10
● e così via…
Il cifrario di Cesare nasconde l’informazione utilizzando una chiave, che è un numero intero
positivo, da sommare alla posizione della lettera originale: il risultato ottenuto corrisponde
alla posizione della lettera cifrata.
● a con key = 2 diventa c
Se la chiave porta oltre la fine dell’alfabeto, si ricomincia dal principio:
● a con key = 28 diventa c
Per decriptare (o “decifrare”) il messaggio, si applica la stessa procedura ma muovendosi
all’indietro nell’alfabeto. Devi fornire le funzioni:
caesar_cypher_encrypt(s, key)
caesar_cypher_decrypt(s, key)
dove:
● s è una stringa (lettera, parola, frase, ecc.).
● key è un numero intero positivo, la chiave del cifrario di Cesare.
La tua implementazione deve trasformare soltanto le lettere ASCII maiuscole e minuscole.
Caratteri speciali, numeri e lettere accentate non devono essere modificati.
Le funzioni non devono stampare nulla a schermo, ma restituire la stringa cifrata o
decifrata."""


def caesar_cipher_encrypt(s: str, key: int) -> str:

    encrypted_text: str = ""

    for letter in s:
        if letter in ascii_lowercase:

            letter_position: int = ascii_lowercase.index(letter)

            letter_new_position: int = (letter_position + key) % 26

            encrypted_text += ascii_lowercase[letter_new_position]

        elif letter in ascii_uppercase:

            letter_position: int = ascii_uppercase.index(letter)

            letter_new_position: int = (letter_position + key) % 26

            encrypted_text += ascii_uppercase[letter_new_position]

        else:
            encrypted_text += letter

    return encrypted_text


def caesar_cipher_decrypt(s: str, key: int) -> str:

    encrypted_text: str = ""

    for letter in s:
        if letter in ascii_lowercase:

            letter_position: int = ascii_lowercase.index(letter)

            letter_new_position: int = (letter_position - key) % 26

            encrypted_text += ascii_lowercase[letter_new_position]

        elif letter in ascii_uppercase:

            letter_position: int = ascii_uppercase.index(letter)

            letter_new_position: int = (letter_position + key) % 26

            encrypted_text += ascii_uppercase[letter_new_position]

        else:
            encrypted_text += letter

    return encrypted_text


encrypted = caesar_cipher_encrypt("°é*Trying to encry/pt a? phras_e!!", 12)
print("Encrypted text: ", encrypted)

decrypted = caesar_cipher_decrypt(encrypted, 12)
print("Decrypted text: ", decrypted)
