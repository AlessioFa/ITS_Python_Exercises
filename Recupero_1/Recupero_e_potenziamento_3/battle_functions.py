from ReP3_A_Farallo import Alien, Monster, Creature


def evenEqual(a: list[int], b: list[int]) -> list[int]:

    """Takes two lists of positive integers and compares their elements.

    Returns a new list where each element is:
    - 1 if both elements at the same position in the input lists are even
    - 0 if both elements are odd """

    c: list = []

    for el_a, el_b in zip(a, b):
        #print(el_a, el_b)

        if el_a % 2 == 0 and el_b % 2 == 0:
            c.append(1)

        if el_a % 2 != 0 and el_b % 2 != 0:
            c.append(0)

    return c


def fighting(a: Alien, m: Monster) -> Creature | None:

    """Simulate a fight between an Alien and a Monster.

    Check if inputs are valid. If not, print error and return None.

    Compare Alien's ammo and Monster's assault with evenEqual.
    If more than 4 matches, Monster wins and shouts 3 times.
    Else, Alien wins and Monster groans once.

    Return the winner or None."""

    if not isinstance(a, Alien) or not isinstance(m, Monster):
        print("Error: one or both creature not recognised.")

        return None

    result = evenEqual(a.get_ammo(), m.assault)

    check = result.count(1)

    if check > 4:

        for i in range(3):
            print(m.victory_shout)
        return m

    else:
        print(m.defeat_groan)

        return a


def declareWinner(c: Creature) -> None:
    """
    Print a framed box announcing the winner creature.

    Args:
        c (Creature): The creature to declare as the winner.
    """
    winner_str: str = str(c)
    width: int = len(winner_str) + 10
    height = 5

    for i in range(height):
        for j in range(width):

            if i == 0 or i == height - 1:
                print("*", end="")

            elif j == 0 or j == width - 1:
                print("*", end="")

            elif i == 2 and j == 5:
                print(winner_str, end="")
                print("     *", end="")
                break

            else:
                print(" ", end="")

        print()
