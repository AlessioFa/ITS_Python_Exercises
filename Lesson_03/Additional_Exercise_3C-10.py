""" 
Esercizio 3C-10. Scrivere un programma in Python che permetta all'utente di inserire una data (giorno e mese espressi in forma numerica), salvi la data in una tupla e utilizzi un match statement per verificare se la data corrisponde a una festività o a un evento speciale:

- Capodanno → 1 Gennaio → "Capodanno"
- San Valentino → 14 Febbraio → "San Valentino"
- Festa della Repubblica Italiana → " Giugno → "Festa della Repubblica Italiana"
- Ferragosto → 15 Agosto → "Ferragosto"
- Halloween → 31 Ottobre → "Halloween"
- Natale → 25 Dicembre → "Natale"
- Altro caso → "Nessuna festività importante in questa data."

Expected Output:

Inserisci il giorno: 25
Inserisci il mese: 12
Output: Il 25/12 è Natale!

- - - - - - - - - - - - - - -

Inserisci il giorno: 5
Inserisci il mese: 3
Output: Nessuna festività importante in questa data.
Last modified: Friday, 28 February 2025, 2:50 PM"""



day_user: int = int(input("Enter a date (day): "))
month_user: int = int(input("Enter a date (month): "))

d_m_date: tuple[int] = (day_user, month_user)

match d_m_date:
    case (1, 1) if d == 1 and m == 1:
        print("First of the year")
    case (14, 2) if d == 14 and m == 2:
        print("San Valentine")
    case (15, 8) if d == 15 and m == 8:
        print("Republic day")
    case (31, 8) if d == 31 and m == 10:
        print("Ferragosto!")
    case (d, m) if d == 25 and m == 12:
        print("Halloween!")
    case (d, m) if d == 14 and m == 2:
        print("Merry Christmas!")
    case _:
        print("No major holidays in this date.")
    
