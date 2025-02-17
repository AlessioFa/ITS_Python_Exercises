# Exercise 3-5: Changing Guest List

# List of people invited to dinner
guest_list: list[str] = [
    "Michael Jordan",
    "Michael Phelps",
    "Shaquille O'Neal",
    "Jensen Huang"
]

# Send individual invitations using slicing and formatted strings
print(f"Dear {guest_list[0]},\nI have always appreciated your work. As you are a true inspiration to me, I would love to invite you to dinner. Looking forward to your response.\n\nAlessio Farallo\n")
print(f"Dear {guest_list[1]},\nI have always appreciated your work. As you are a true inspiration to me, I would love to invite you to dinner. Looking forward to your response.\n\nAlessio Farallo\n")
print(f"Dear {guest_list[2]},\nI have always appreciated your work. As you are a true inspiration to me, I would love to invite you to dinner. Looking forward to your response.\n\nAlessio Farallo\n")
print(f"Dear {guest_list[3]},\nI have always appreciated your work. As you are a true inspiration to me, I would love to invite you to dinner. Looking forward to your response.\n\nAlessio Farallo\n")

# Notify that one guest cannot make it to the dinner
print("Shaquille O'Neal can't make it to the dinner. You'll receive a new invitation soon.\n")

# Update the guest list using slicing (remove Shaquille O'Neal and add Elon Musk)
updated_guest_list = guest_list[:2] + ["Jensen Huang", "Elon Musk"]

# Send updated invitations
print(f"Dear {updated_guest_list[0]},\nI have always appreciated your work. As you are a true inspiration to me, I would love to invite you to dinner. Looking forward to your response.\n\nAlessio Farallo\n")
print(f"Dear {updated_guest_list[1]},\nI have always appreciated your work. As you are a true inspiration to me, I would love to invite you to dinner. Looking forward to your response.\n\nAlessio Farallo\n")
print(f"Dear {updated_guest_list[2]},\nI have always appreciated your work. As you are a true inspiration to me, I would love to invite you to dinner. Looking forward to your response.\n\nAlessio Farallo\n")
print(f"Dear {updated_guest_list[3]},\nI have always appreciated your work. As you are a true inspiration to me, I would love to invite you to dinner. Looking forward to your response.\n\nAlessio Farallo\n")


# Solving the same exercise defining a funcion and using a for loop 
# List of people invited to dinner
guest_list: list[str] = [
    "Michael Jordan",
    "Michael Phelps",
    "Shaquille O'Neal",
    "Jensen Huang"
]


# Define a function that sends dinner invitations
def dinner_invitation(guest: list[str]):
    # Loop through the guest list and print the invitation for each guest
    for person in guest:
        print(f"Dear {person},\nI have always appreciated your work. As you are a true inspiration to me, I would love to invite you to dinner. Looking forward to your response.\n\nAlessio Farallo\n")


# Call the function to send dinner invitations
dinner_invitation(guest_list)

# Notify that one guest cannot make it to the dinner
print("Shaquille O'Neal can't make it to the dinner. You'll receive a new invitation soon.\n")

# Update the guest list, replacing the unavailable guest
updated_guest_list: list[str] = ["Michael Jordan", "Michael Phelps", "Jensen Huang", "Elon Musk"]

# Call the function again to send the updated dinner invitations
dinner_invitation(updated_guest_list)
