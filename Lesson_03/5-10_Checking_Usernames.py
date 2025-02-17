# Exercise 5-10: Checking Usernames

# List of users
current_users: list[str] = ["DavidBombal", "NetworkChuck", "ProfessorMesser", "MrRip", "admin"]

new_users: list[str] = ["RootSeeker", "Admin", "EveDev", "ByteMaster", "networkchuck"]

current_users_lower: list[str] = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
        print(f"Sorry, the username {user} is already taken.")
    else:
        print(f"Great! The username {user} is available.")
