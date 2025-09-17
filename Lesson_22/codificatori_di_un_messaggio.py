from abc import ABC, abstractmethod
from string import ascii_lowercase, ascii_uppercase

class CodificatoreMessaggio(ABC):

    @abstractmethod
    def codifica(self, testo_decodificato: str):
        pass

class DecodificatoreMessaggio(ABC):

    @abstractmethod
    def decodifica(self, testo_codificato: str):
        pass

class CifratoreAScorrimento(CodificatoreMessaggio, DecodificatoreMessaggio):

    def __init__(self, chiave: int):
        
        self.chiave = chiave 
    
    def sposta_carattere(self, char: str, chiave: int) -> str:

        if char in ascii_lowercase:

            posizione = ascii_lowercase.index(char)
            nuova_posizione = (posizione + chiave) % 26

            return ascii_lowercase[nuova_posizione]

        elif char in ascii_uppercase:

            posizione = ascii_uppercase.index(char)
            nuova_posizione = (posizione + chiave) % 26

            return ascii_uppercase[nuova_posizione]

        else:

            return char
    
    def codifica(self, testo_decodificato: str) -> str:
        risultato = ""
        for char in testo_decodificato:

            risultato += self.sposta_carattere(char,self.chiave)
        
        return risultato
    

    def decodifica(self, testo_codificato: str) -> str:
        
        risultato = ""

        for c in testo_codificato:

            risultato += self.sposta_carattere(c, -self.chiave)

        return risultato

class CifratoreACombinazione(CodificatoreMessaggio, DecodificatoreMessaggio):

    def __init__(self, num: int):

        self.num = num
    
    def __combinazione(self, testo: str) -> str:

        metà = (len(testo) + 1 ) // 2

        parte1 = testo[:metà]
        parte2 = testo[metà:]

        combinato = ''

        for i in range(max(len(parte1), len(parte2))):

            if i < len(parte1):

                combinato += parte1
            
            if i < len(parte2):

                combinato += parte2
        
        return combinato

        

    def codifica(self, testo_in_chiaro: str):

        testo_in_chiaro = 