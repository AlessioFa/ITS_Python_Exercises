from string import ascii_lowercase

"""Exercise 3: Get position of a letter

    Write a function that takes a letter and returns its position (a → 1, b → 2, ...).
    
    And viceversa. 
"""


def get_position(letter: str) -> int:

    if not letter.isascii() or not letter.isalpha() or not len(letter) != 1:
        print("Enter a valid letter.")

    position: int = ascii_lowercase.index(letter) + 1

    return position


print(get_position("z"))


def get_letter(num: int) -> str:

    if num < 1 or num > 26:
        print("Number not valid.")

    return f"Letter: {ascii_lowercase[num - 1]}"


print(get_letter(4))
