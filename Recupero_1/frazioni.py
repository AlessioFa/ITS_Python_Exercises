"""

8.A Si Scriva in Python in un file frazioni.py una classe Frazione, i cui attributi privati siano rispettivamente numeratore e denominatore.
Si definiscano i metodi __init__, setter, getter, __str__, value.
In particolare:

    il metodo value(), deve restituire il valore della frazione, ovvero numeratore / denominatore arrotondato a 3 cifre decimali;

    il metodo __str__ deve mostare in output la frazione nel seguente modo: "numeratore / denominatore ";
    i metodi setter devono controllare che il valore inserito sia un intero, in caso contrario il numeratore ed il denominatore devono essere impostati per default rispettivamente a 13 e 5. Inoltre, il metodo setter relativo al denominatore deve assicurarsi che questo non sia mai uguale a 0. Nel caso in cui il denominatore passato sia 0, impostarlo per default a 5.

Suggerimento: per verificare che il numeratore ed il denominatore siano numeri interi, usare la funzione is_integer().

"""


class Frazione:

    def __init__(self, numeratore: int, denominatore: int) -> None:

        self.set_numeratore(numeratore)
        self.set_denominatore(denominatore)

    def set_numeratore(self, numeratore) -> None:

        if not float(numeratore).is_integer():
            self.__numeratore = 13

        else:
            self.__numeratore = int(numeratore)

    def set_denominatore(self, denominatore) -> None:

        if not float(denominatore).is_integer() or denominatore == 0:
            self.__denominatore = 5

        else:
            self.__denominatore = int(denominatore)

    def get_numeratore(self) -> int:

        return self.__numeratore

    def get_denominatore(self) -> int:

        return self.__denominatore

    def value(self) -> float:

        return round(self.__numeratore / self.__denominatore, 3)

    def __str__(self) -> str:

        return f"{self.__numeratore} / {self.__denominatore}"
