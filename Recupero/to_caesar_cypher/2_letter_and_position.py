from string import ascii_lowercase

"""Exercise 2: Print letters with positions

    Print letters with their positions (1 → a, 2 → b, ... 26 → z)."""


# First method
def letter_positions() -> None:

    position_counter: int = 1

    for letter in ascii_lowercase:

        print(f"Position: {position_counter}  Letter: {letter} ")

        position_counter += 1


letter_positions()


print()
print()


# Second method
def letter_pos_2() -> None:
    for index, letter in enumerate(ascii_lowercase):
        print(f"Position: {index + 1}  Letter: {letter}")


letter_pos_2()
