# Exercise 3-7: Shrinking Guest List

# List of people invited to dinner
guest_list: list[str] = ["Michael Jordan", "Michael Phelps", "Shaquille O' Neal", "Jenses Huang"]

# Define a function that sends dinner invitations
def dinner_invitation (guest: list[str]):
    
    # Loop through the guest list and print the invitation for each guest
    for person in guest:
        print(f"Dear {person},\nI have always appreciated your work. As you are a true inspiration to me, i would love to invite you to dinner. Looking forward to your response,\n\nAlessio Farallo\n ")

# Call the function to send dinner invitations
dinner_invitation(guest_list)


# Notify that one guest cannot make it to the dinner
print("Shaquille O' Neal can't make it to the dinner. You'll receive a new invitation soon.\n")

# Update the guest list, replacing the unavailable guest
updated_guest_list: list[str] = ["Michael Jordan","Michael Phelps", "Jenses Huang", "Elon Musk"]

# Call the function again to send the updated dinner invitations
dinner_invitation(updated_guest_list)

# Inform guests about the bigger table
print("Great news! I found a bigger table, so three more guests will be joining us for dinner.\n")

# Add a new guest at the beginning of the list (at index 2)
updated_guest_list.insert(0, "Justin Bieber")

# Calculate the middle index of the list
midle_index = len(updated_guest_list) // 2

# Add a new guest at the middle of the list
updated_guest_list.insert(midle_index, "Scottie Pippen")

# Add a new guest at the end of the list
updated_guest_list.append("Antonino Cannavacciuolo")

# Send invitations to the updated list of guests
dinner_invitation(updated_guest_list)

# Inform the guests about the problem and that only two people can be invited
print("Unfortunately a tragic problem occured, and i can only invite two people for dinner.")

print(updated_guest_list)

"""
The following loop removes guests from the list until only two remain.
For each removed guest, a message is printed to inform them that they can no longer be invited.
"""
while len(updated_guest_list) > 2:
    removed_guest = updated_guest_list.pop()
   
    print(f"Dear,\n{removed_guest} unfortunately i cannot invite you anymore for dinner. Best regards,\nAlessio Farallo.")

# After the loop, the final list of guests is printed, showing only the two remaining guests.
print(updated_guest_list)

# The function is called again to send the final invitations to the remaining guests in the list.
dinner_invitation(updated_guest_list)

# Removing all elements from the list
del updated_guest_list[:]

# Checking if updated_guest_list is emtpy
print(updated_guest_list)
