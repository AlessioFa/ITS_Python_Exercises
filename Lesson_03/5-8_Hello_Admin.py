# Exercise 5-8: Hello Admin

# List of usernames
usernames: list[str] = ["DavidBombal", "NetworkChuck", "ProfessorMesser", "MrRip", "admin"]

# Loop through each user in the list
for user in usernames:
    # Check if the user is "admin" to display a special message
    if user == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        # Generic greeting for regular users
        print(f"Hello {user}, thank you for logging in again.")
