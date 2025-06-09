import random
"""
    Create a function that generates a random number within a range specified by the user.
    Prompt the user to guess the number within a specified maximum number of attempts.
    Provide feedback to the user after each guess, indicating whether their guess is too high, too low, or correct.
    Terminate the loop when the user guesses the number correctly or reaches the maximum number of attempts.
"""


def guess_the_number() -> None:
    user_name: str = input("Please, enter your name: ")

    print(f"{user_name.title()}, welcome to 'Guess the number'! A game where you can decide a specific range of numbers and guess a number!\n")

    guesses: int = int(input("How many guesses do you want to have?: "))

    print(f"\nNice! Now you have {guesses} guesses to guess the number, good luck!")
    print("One last step before you can start the game. You have to decide a lower and an upper number, the number to guess is between them.")

    lower_num: int = int(input("Enter the lower number: "))
    greatest_num: int = int(input("Enter the greatest number: "))

    number_to_guess: int = random.randint(lower_num, greatest_num)

    print("The game is now started! Try to guess the number.\n")

    counter: int = 0

    while counter < guesses:
        user_num: int = int(input("Enter your number: "))

        if user_num == number_to_guess:
            print(f"Well done {user_name}! {number_to_guess} is the right number!")

            break

        if user_num < number_to_guess:
            print("Your number is lower than the number to guess, go higher!")

        else:
            print("Your number is higher than the number to guess, go lower!")

        counter += 1

    else:
        print(f"Sorry {user_name}, you've run out of guesses. The number was {number_to_guess}.")    


guess_the_number()
