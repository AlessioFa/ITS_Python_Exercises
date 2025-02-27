vote: str = int(input("Enter your vote:"))

match vote:
    case 10:
        print("Your vote is: Excellent!")
    case (8 | 9):
        print("Your vote is: Very Good")
    case (6 | 7):
        print("Your vote is: Sufficient")
    case (4 | 5):
        print("Your vote is: Not Sufficient")
    case (1 | 2 | 3):
        print("Your vote is: Badly not sufficient")
    case _:
        print("Vote not valid")
