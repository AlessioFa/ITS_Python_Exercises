
"""Exercise 5: Add a number to a position

    Write a function that takes a position and a number to add.

    Return the new position, but if it is more than 26, start again from 1 (wrap around)."""


def number_pos(position: int, num_to_add: int) -> int:

    new_position: int = ((position - 1) + num_to_add) % 26 + 1

    return new_position


print(number_pos(1, 0))
