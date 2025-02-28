"""This is an additiional exercise about match statement , here is the text: Imagine you're participating in a Mario Kart race with your friends. Each player finishes the race in a specific position.
Write a Python program that takes as input the finishing position of a player, given as a positive integer, and returns the
position in cardinal form (e.g., "1st", "2nd", "3rd", "4th", "5th", etc.)."""

# Solve the exercise with if-elif-else

# Get the finishing position from the user input
f_position: int = int(input("Enter your finishing position: "))

# Check if the position is 1 and print "st"
if f_position == 1:
    print(f"Finishing position: {f_position} \n\n{f_position}st!")
# Check if the position is 2 and print "nd"
elif f_position == 2:
    print(f"Finishing position: {f_position} \n\n{f_position}nd!")
# Check if the position is 3 and print "rd"
elif f_position == 3:
    print(f"Finishing position: {f_position} \n\n{f_position}rd!")
# If the position is any other number, print "th"
else:
    print(f"Finishing position: {f_position} \n\n{f_position}th")


# Same exercise solved with match statement

# Get the finishing position from the user input
f_position = int(input("Enter your finishing position: "))

# Use a match statement to check the position
match f_position:
    # If position is 1, print "st"
    case 1:
        print(f"Finishing position: {f_position} \n\n{f_position}st!")
    # If position is 2, print "nd"
    case 2:
        print(f"Finishing position: {f_position} \n\n{f_position}nd!")
    # If position is 3, print "rd"
    case 3:
        print(f"Finishing position: {f_position} \n\n{f_position}rd!")
    # If position is any other number, print "th"
    case _:
        print(f"Finishing position: {f_position} \n\n{f_position}th")
