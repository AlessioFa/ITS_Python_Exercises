class Libro:
    def __init__(self):
        self.titolo = "" 
        self.autore = "" 
        self.genere: list[str] = []

    def set_titolo(self, titolo: str) -> None:
        self.titolo =  titolo
    
    def set_autore(self, nome: str) -> None:
        self.autore = nome
    
    def set_genere(self, tipo_genere: list[str]) -> None:
        self.genere = tipo_genere
    
    def get_titolo(self) -> str:
        return self.titolo
    
    def get_autore(self) -> str:
        return self.autore

    def get_genere(self) -> list[str]:
        return self.genere
    

class Biblioteca:
    def __init__(self):
        self.libri: list[Libro] = []
    
    def add_libro(self, libro: Libro) -> None:
        self.libri.append(Libro)

    def get_titolo(self) -> None:
        for item in self.libri:
            print(item.get_titolo(), item.get_autore(), item.get_genere())


# codice driver

collezione: Biblioteca = Biblioteca()

#LIbro1
libro1: Libro = Libro()

libro1.set_titolo("Il piccolo principe")

libro1.set_autore("Sconosciuto")

libro1.set_genere(["Narrativa"])

collezione.add_libro(libro1)

# Libro 2
libro2: Libro = Libro()

libro2.set_titolo("Harry Potter")

libro2.set_autore("J.K Rowling")

libro2.set_genere(["Narrativa", "Fantasy"])

collezione.add_libro(libro2)
