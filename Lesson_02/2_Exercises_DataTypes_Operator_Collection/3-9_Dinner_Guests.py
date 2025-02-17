# Exercise 3-9: Dinner guest , from 3-4

# List of people i'd like to invite to dinner
guest_list: list[str] = ["Michael Jordan", "Michael Phelps", "Shaquille O' Neal", "Jenses Huang"]


# Define a function that sends dinner invitations
def dinner_invitation(guest: list[str]):

    # Loop through the guest list and print the invitation for each guest
    for person in guest:
        print(f"Dear {person},\ni have always appreciated your work. As you are a true inspiration to me, i would love to invite you to dinner. Looking forward to your response,\n\nAlessio Farallo\n ")


# Call the function to send dinner invitations
dinner_invitation(guest_list)

# Using len function to display the lenght of the list
print(len(guest_list))
