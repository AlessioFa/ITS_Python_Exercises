# Ask for a user's name ,role and age
user_name: str = input("Enter the name of the user: ").title()
user_role: str = input("Enter the role of the user: ").title()
user_age: int = int(input("Enter the age of the user: "))

# Storing all the user's details in a dictionary
user_dict: dict = {"Name": user_name, "Role": user_role, "Age": user_age}

# Check the user's role and age, and print the appropriate message
match user_dict["Role"]:
    case "Admin":
        print("Full access at all the activities.")

    case "Moderator":
        print("Can manage content but cannot change settings.")

    case "User" if user_dict["Age"] >= 18:
        print("Standard access at all services.")

    case "User" if user_dict["Age"] <= 18:
        print("Restricted access! Some features are blocked.")

    case "Guest":
        print("Restricted access! Only content viewing is allowed.")

    case _:
        print("Warning! Unrecognized role! Access denied.")
