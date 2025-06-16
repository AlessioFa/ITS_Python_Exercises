# Ask the user for a name
user_name: str = input("Enter your name: ").title()

# Ask the user for a gender ( m / f)
user_gender: str = input("Enter your gender (m for male, f for female): ").lower()

# Use match statement to check the gender and print the result
match user_gender:
    case "m":
        print(f"Name: {user_name}\nGender: Male")

    case "f":
        print(f"Name: {user_name}\nGender: Female")

    case _:
        print(f"I'm sorry {user_name}, it's not possible to generate a valid ID.")
