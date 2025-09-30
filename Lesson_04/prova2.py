"""Scrivere un programma che permetta di analizzare una lista di numeri interi inseriti dall’utente.

Il programma deve:

    acquisire una sequenza di numeri interi, terminando l’inserimento quando l’utente digita 0 (che non deve essere considerato nei calcoli);
    calcolare e visualizzare la somma di tutti i numeri pari inseriti;
    calcolare e visualizzare la media di tutti i numeri dispari inseriti;
    determinare e visualizzare il numero con la frequenza più alta (cioè quello che compare più volte nella lista);
    se più numeri hanno la stessa frequenza massima, visualizzarli tutti.
"""

# Create a list to store all numbers
sequence: list = []
# List that stores all the even values
even_numbers: list = []
# List that stores all the even values
odd_numbers: list = []
# List that stores the sum between all the even values
sum_even_numbers: int = 0
# Variable that store the sum between all the even values
sum_odd_numbers: int = 0
# Variable that store the average of odd numbers
average_odd_numbers: float = 0
# Numbers that appear most times
most_frequent_number: list[int] = []
# Variable that store the maximum occurrence of any number
max_occurrency: int = 0


while True:
    # Ask the user for one or more integer nnumbers
    number: int = int(input("Enter a number (0 to end): "))
    if number <= 0:
        print("By entering 0 you stopped the program.")
        break
    else:
        sequence.append(number)

# Loop in sequence and calculate the sum of odd numbers
for even in sequence:
    if even % 2 == 0:
        even_numbers.append(even)
for even in even_numbers:
    sum_even_numbers += even

print(f"This is the sum of all the even numbers: {sum_even_numbers}")

# Loop in sequence and calculate the sum of odd numbers
for odd in sequence:
    if odd % 2 != 0:
        odd_numbers.append(odd)

# Calculate the average of odd numbers
for odd in odd_numbers:
    sum_odd_numbers += odd
average_odd_numbers = sum_odd_numbers / len(odd_numbers)


print(f"This is the average of odd numbers: {average_odd_numbers}")

# Find the maximum occurrence of any number
for n in sequence:
    counter = sequence.count(n)
    if counter > max_occurrency:
        max_occurrency = counter

# Find all numbers with the maximum occurrence
for n in sequence:
    if sequence.count(n) == max_occurrency and n not in most_frequent_number:
        most_frequent_number.append(n)

print(f"The number that appear most frequently is: {most_frequent_number} ({max_occurrency} times)")
