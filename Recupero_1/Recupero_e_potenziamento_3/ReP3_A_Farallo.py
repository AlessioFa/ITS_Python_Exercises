from random import randint


class Creature:
    """ Base class representing a generic creature with a validated name."""
    def __init__(self, name: str) -> None:

        self.set_name(name)

    def set_name(self, name: str) -> None:
        """
        Set the creature's name, if invalid set a default name.
        """
        if not isinstance(name, str) or name.strip() == "":
            self.__name = "Generic Creature"

        else:
            self.__name = name

    def get_name(self) -> str:
        """Returns the creature's name."""
        return self.__name

    def __str__(self) -> str:
        """Returns a string rapresenting the creature's name."""
        return f"Creature: {self.__name}"


class Alien(Creature):
    """
    Creature's subclass, representing an alien and its characteristics.

    Checks if the alien name is correct, if not, shows a warning phrase and sets a default name.
    """
    def __init__(self, name):

        self.__set_id_number()
        self.__set_ammo()

        if not name.startswith(f"Robot + {self.__id_number}"):
            print("Warning! All aliens must have the name 'Robot' followed by their ID number! Resetting alien name now!\n")
            name = f"Robot - {self.__id_number}"

        super().__init__(name.upper())

    def __set_id_number(self) -> None:
        """Sets the alien's ID number."""
        self.__id_number = randint(10000, 90001)  # 10000 / 90000.

    def __set_ammo(self) -> None:
        """Set the alien's ammo list."""
        self.__ammo = [n * n for n in range(0, 15)]
    
    def get_ammo(self) -> list[int]:
        """Returns the alien's ammo list."""
        return self.__ammo
    
    def get_victory_shout(self) -> str:
        """Returns the alien's victory shout."""
        return "GRAAAHHH"

    def __str__(self) -> str:
        """Returns a sting representation of an alien."""
        return f"Alien: {self.get_name()}"       # output: Alieno: Robot-16326


class Monster(Creature):
    """
    Subclass of Creature, representing a monster and its characteristics.
    """
    def __init__(self, name, victory_shout: str, defeat_groan: str) -> None:
        super().__init__(name.upper())

        self.__set_Victory(victory_shout)
        self.__set_defeat(defeat_groan)
        self.__set_assault()

    def __set_assault(self) -> None:
        """Set the monster's assault list with 15 random values from 1 to 100."""
        self.assault = []

        while len(self.assault) < 15:

            n = randint(1, 101)

            self.assault.append(n)   # [randint(1, 101) for _ in range(15)

    def __set_Victory(self, victory: str) -> None:
        """Set the victory shout if valid; if not assign a default string."""
        if not isinstance(victory, str) or victory.strip() == "":

            self.victory_shout = "GRAAAHHH"

        else:
            self.victory_shout = victory

    def __set_defeat(self, lost: str) -> None:
        """Set the default groan if valid, if not assign a default string."""
        if not isinstance(lost, str):
            self.defeat_groan = "Uuurghhh"

        else:
            self.defeat_groan = lost

    def get_victory_shout(self) -> str:
        """Return the monster's victory shout."""
        return self.victory_shout

    def __str__(self) -> str:
        """Return a string representation of the monster with camel case name."""
        new_name: str = ""

        for index, letter in enumerate(self.get_name()):

            if index % 2 == 0:
                new_name += letter.lower()

            else:
                new_name += letter.upper()

        return f"Monster: {new_name}"
