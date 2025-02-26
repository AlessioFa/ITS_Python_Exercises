vote: int = int(input("Enter the vote of your graduation: "))


match vote:
    case vote if 106 <= vote <= 110:
        print("Your GPA is: 4.0")
    case vote if 101 <= vote <= 105:
        print("Your GPA is: 3.7")
    case vote if 96 <= vote <= 100:
        print("Your GPA is: 3.3")
    case vote if 91 <= vote <= 95:
        print("Your GPA is: 3.0")
    case vote if 86 <= vote <= 90:
        print("Your GPA is: 4.0")
    case vote if 81 <= vote <= 85:
        print("Your GPA is: 2.3")
    case vote if 76 <= vote <= 80:
        print("Your GPA is: 2.0")
    case vote if 70 <= vote <= 75:
        print("Your GPA is: 1.7")
    case vote if 66 <= vote <= 69:
        print("Your GPA is 1.0")
    case _:
        print("Vote not valid.")
        