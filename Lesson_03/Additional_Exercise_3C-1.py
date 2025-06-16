# Ask the user for a vote
user_vote: int = int(input("Enter your vote (1-10):"))

# Check the entered vote and print the corrispective evaluation
match user_vote:
    case 10:
        print("Your vote is: Excellent!.")
    case (8 | 9):
        print("Your vote is: Very Good.")
    case (6 | 7):
        print("Your vote is: Sufficient.")
    case (4 | 5):
        print("Your vote is: Not Sufficient.")
    case (1 | 2 | 3):
        print("Your vote is: Completely Not Sufficient.")
    case _:
        print("Vote not valid")
