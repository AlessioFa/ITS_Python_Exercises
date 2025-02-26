vote: str = int(input("Enter your vote:"))

match vote:
    case 10:
            print(f"Your vote is: Excellent!")
    case (8 | 9):
            print(f"Your vote is: Very Good")
    case (6 | 7):
            print(f"Your vote is: Sufficient")
    case (4 | 5):
            print(f"Your vote is: Not Sufficient")
    case (1 | 2| 3):
            print(f"Your vote is: Badly not sufficient")
    case _:
        print("Vote not valid")