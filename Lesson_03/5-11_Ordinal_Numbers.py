# Exercise 5-11: Ordinal Numbers

# List of numbers from 1 to 9
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Loop through the list of numbers
for n in numbers:
    # Check if the number is 1, 2, or 3 and print the corresponding ordinal suffix
    if n == 1:
        print(f"{n}st")
    elif n == 2:
        print(f"{n}nd")
    elif n == 3:
        print(f"{n}rd")
    else:
        print(f"{n}th")
