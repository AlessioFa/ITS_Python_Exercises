points: int = 0

while points < 100:
    d1: int = int(input("Enter the value of the first dice: "))
    d2: int = int(input("Enter the value of the second dice: "))

    if not (1 <= d1 <= 6) or not (1 <= d2 <= 6):
        print("Please enter valid values for the dice (1-6).")
    else:
        dice_sum = d1 + d2

        if d1 % 2 == 0 and d2 % 2 == 0 and dice_sum > 8:
            points = 100
            print("Victory!")
            break

        elif d1 == 6 or d2 == 6 or dice_sum == 7:
            points += 10

        else:
            points = 0
            print("You lost.")

    if points >= 100:
        print("Victory!")
        break
