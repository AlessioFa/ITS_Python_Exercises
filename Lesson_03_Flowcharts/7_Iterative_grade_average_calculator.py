count: int = 0
sum = 0

while True:
    answer: str = input("Do you want to enter your vote? (yes/no): ").lower()
    if answer == "yes":
        vote: int = int(input("Enter your vote: "))

        if vote > 0:
            count += 1
            sum += vote
        else:
            print("Error, the value of your vote has to be positive.")
            continue

    if answer == "no":
        if count > 0:
            average: int = sum / count
            print("The average is:", average)
        else:
            print("No vote has been entered.")
