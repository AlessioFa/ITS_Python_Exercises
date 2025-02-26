
# Ask the user to input the number of babies
babies: int = int(input("Enter the number of your babies: "))

# Check the number of babies printing a corresponding message
match babies:
    case 1:
        print("Congratulation!")
    case 2:
        print("Wow! Twins!")
    case 3:
        print("Wow three!")
    case 4:
        print("Four, incredible! Wow!")
    case 5:
        print("Incredible! Five!")
    case _:
        print(f"I don't believe it! {babies} babies!")
