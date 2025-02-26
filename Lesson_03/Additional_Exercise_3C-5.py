user_name: str = input("Enter the name of the user: ")
user_role: str = input("Enter the role of the user: ").title()
user_age: int = int(input("Enter the age of the user: "))

user_dict: dict = {"Name": user_name, "Role": user_role, "Age": user_age}
    

match user_dict["Role"]:
    case "Admin":
        print("Full access at all the activity.")
    case "Moderator":
        print("It can manage contents but not change settings.")
    case "User" if user_dict["Age"] >= 18:
        print("Standard access at all services.")
    case "User" if user_dict["Age"] <= 18:
        print("Restricted access! Some features are blocked.")
    case "Guest":
        print("Restricted access! Only content visualization.")
    case _: 
        print("Attention! Unrecognized role! Access denied.")
    