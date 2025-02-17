# Exercise 3-4: Guest List

# List of people i would like to invite to dinner
guest_list: list[str] = ["Michael Jordan", "Michael Phelps", "Shaquille O' Neal", "Jenses Huang"]

# Use indexing to print dinner invitation for each guest
print(f"Hi {guest_list[0]}, would you like to come to dinner ?")
print(f"Hi {guest_list[1]}, would you like to come to dinner ?")
print(f"Hi {guest_list[2]}, would you like to come to dinner ?")
print(f"Hi {guest_list[3]}, would you like to come to dinner ?")


# Define a function that sends dinner invitations
def dinner_invitation(guest: list[str]):

    # Loop through the guest list and print the invitation for each guest
    for person in guest:
        print(
            f"Dear {person},\n\n"
            "I have always appreciated your work. As you are a true inspiration to me, "
            "I would love to invite you to dinner. Looking forward to your response.\n\n"
            "Best regards,\n"
            "Alessio Farallo\n"
        )
