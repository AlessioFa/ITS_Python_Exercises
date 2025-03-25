"""Crea una classe Libro che rappresenti un libro con le seguenti caratteristiche:

Attributi: titolo, autore, anno di pubblicazione, numero di pagine.
Metodi:
descrizione(): restituisce una stringa con le informazioni del libro.
è_lungo(): restituisce True se il libro ha più di 300 pagine, altrimenti False.
Poi, crea una classe Biblioteca che gestisca una collezione di libri con:

Un attributo libri che contiene una lista di oggetti Libro.
Un metodo aggiungi_libro(libro) per aggiungere un libro alla biblioteca.
Un metodo mostra_libri() per stampare la descrizione di tutti i libri nella biblioteca.
Un metodo cerca_per_autore(autore) che restituisce tutti i libri scritti da un autore specifico.
Bonus: Aggiungi un metodo rimuovi_libro(titolo) che rimuove un libro dalla biblioteca dato il titolo."""


class Book:
    def __init__(self, title: str, author: str, publication_year: int, pages: int):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.pages = pages
    
    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nYear of publication: {self.publication_year}\nPages: {self.pages}"
    
    def lenght(self):
        return self.pages >= 300
    
    
            
        
    

libretto = Book("La magia dell' ITS", "Federico March", "1995", 299)

print(libretto.lenght())

