from ReP3_A_Farallo import Alien, Monster
from battle_functions import evenEqual, fighting, declareWinner

if __name__ == "__main__":
    # Create an Alien
    alien = Alien("Robot-41119")  
    print(alien)

    # Access the "private" ammo list
    print("Ammo:", alien._Alien__ammo)  

    print()  # empty line to separate output

    # Create a Monster
    monster = Monster("gOrThOr", "GRAAAHHH", "Uuurghhh")  
    print(monster)  # prints: Monster: gOrThOr
    print("Assault:", monster.assault)

    print()  
    print("Fight\n")

    # Simulate fight
    winner = fighting(alien, monster)

    # Print the victory shout 3 times
    for _ in range(3):
        print(winner.get_victory_shout())

    print()
    print(f"The {winner.__class__.__name__}s won!\n")  

    # Declare the winner
    declareWinner(winner)
