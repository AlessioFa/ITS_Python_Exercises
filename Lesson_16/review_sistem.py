"""Obiettivo:
Implementare una classe Media che rappresenti un media generico (ad esempio, un film o un libro) e una classe derivata Film che rappresenti specificamente un film e ne specifichi il titolo. Gli studenti dovranno anche creare oggetti di queste classi, aggiungere valutazioni e visualizzare le recensioni.
 
Specifiche della Classe Media:
 
Attributi:
- title (stringa): Il titolo del media.
- reviews (lista di interi): Una lista di valutazioni del media, con voti compresi tra 1 e 5, dove 1=Terribile, 2=Brutto, 3=Normale, 4=Bello, 5=Grandioso.
 
Metodi:
- set_title(self, title): Imposta il titolo del media.
- get_title(self): Restituisce il titolo del media.
- aggiungiValutazione(self, voto): Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5).
- getMedia(self): Calcola e restituisce la media delle valutazioni.
- getRate(self): Restituisce una stringa che descrive il giudizio medio basato sulla media delle valutazioni, ovvero mostra "Terribile" se il voto medio si avvicina a 1, "Brutto" se il voto medio si avvicina a 2, "Normale" se il voto medio si avvicina a 3, "Bello" se il voto medio si avvicina a 4, "Grandioso" se il voto medio si avvicina a 5.
- ratePercentage(self, voto): Calcola e restituisce la percentuale di un voto specifico nelle recensioni.
- recensione(self): Mostra un riassunto delle recensioni e delle valutazioni del media, stampando il titolo, il voto medio, il giudizio e le percentuali di ciascun voto. Esempio di riassunto:
 
Titolo del Film: The Shawshank Redemption
Voto Medio: 3.80
Giudizio: Bello
Terribile: 10.00%
Brutto: 10.00%
Normale: 10.00%
Bello: 30.00%
Grandioso: 40.00%

Si verifichi il funzionamento scrivendo un codice che crei almeno due oggetti di tipo Film, aggiunga a ognuno dei due almeno dieci valutazioni e richiami il metodo recensione().
"""


"""Specifiche della Classe Media:
 
Attributi:
- title (stringa): Il titolo del media.
- reviews (lista di interi): Una lista di valutazioni del media, con voti compresi tra 1 e 5, dove 1=Terribile, 2=Brutto, 3=Normale, 4=Bello, 5=Grandioso.
 
Metodi:
- set_title(self, title): Imposta il titolo del media.
- get_title(self): Restituisce il titolo del media.
- aggiungiValutazione(self, voto): Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5).
- getMedia(self): Calcola e restituisce la media delle valutazioni.
- getRate(self): Restituisce una stringa che descrive il giudizio medio basato sulla media delle valutazioni, ovvero mostra "Terribile" se il voto medio si avvicina a 1, "Brutto" se il voto medio si avvicina a 2, "Normale" se il voto medio si avvicina a 3, "Bello" se il voto medio si avvicina a 4, "Grandioso" se il voto medio si avvicina a 5."""


class Media:

    def __init__(self, title: str) -> None:

        self.title = title
        self.reviews = []

    def set_title(self, title: str) -> None:

        self.title = title

    def get_title(self) -> str:

        return self.title

    def add_evaluation(self, evaluation: int) -> None:

        if evaluation < 1 or evaluation > 5:

            print("Reviews must be a value between 1 and 5.")

        else:

            self.reviews.append(evaluation)

    def get_media(self) -> float | int:

        if len(self.reviews) > 1:

            average_reviews: float = sum(self.reviews) / len(self.reviews)

            return round(average_reviews, 2)

        else:

            return self.reviews[0]

    def get_rate(self) -> str:

        average: float = self.get_media()
        rounded_average: float = round(average)

        if rounded_average == 1:
            return "Terrible."

        if rounded_average == 2:
            return "Bad."

        if rounded_average == 3:
            return "Normal."

        if rounded_average == 4:
            return "Nice"

        else:
            return "Great!"

    def rate_percentage(self, review: int) -> float:

        if not self.reviews:

            percentage_of_rate = 0

            return percentage_of_rate

        else:

            total_reviews: int = len(self.reviews)
            review_count: int = self.reviews.count(review)

            percentage_of_rate = (review_count / total_reviews) * 100

            return round(percentage_of_rate, 2)

    def review(self):

        return f"Movie title: {self.get_title()}\nAverage Vote: {self.get_media()}\nJudgement: {self.get_rate()}"


class Film(Media):
    def __init__(self, title):
        super().__init__(title)


book1 = Media("Harry potter and the Globet of Fire.")

book1.add_evaluation(5)
book1.add_evaluation(5)
book1.add_evaluation(4)
book1.add_evaluation(3)

print(book1.get_media())
print(book1.get_rate())
print(book1.review())


film1 = Film("Inception")

film1.add_evaluation(3)
film1.add_evaluation(4)
film1.add_evaluation(7)
film1.add_evaluation(1)

print(film1.get_media())
print(film1.get_rate())
