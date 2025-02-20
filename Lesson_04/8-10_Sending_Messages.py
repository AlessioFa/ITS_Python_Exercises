# Exercise 8-10: Sending Messages
"""
In this first version, I tried to use a temporary list 
to store the messages, but the real goal was to move the messages 
from the original list to a "sent_messages" list.
I also used 'while len(phrases) > 0:', but I realized it's better to use 
'while True' because data types such as strings, lists, and tuples return True 
as long as they have at least one element.
In the corrected version, I'll fix this and move the messages to a new list called 'sent_messages' 
while printing them.
"""
""""
def send_messages(phrases: list[str]):
    new_short_messages = []
    
    while len(phrases) > 0:
        message = phrases.pop()
        new_short_messages.append(message)
    print("Lista finale", new_short_messages)


# Create a list the shows short messages
short_messages: list[str] = [
    "I love to learn python!",
    "Chess is a stimulating game.",
    "I'd love to visit the whole world."
]

send_messages(short_messages)

"""


# Define a function that moves all messages from short_messages to sent_messages
def send_messages(short_messages: list[str], sent_messages: list[str]) -> list[str]:
    # Loop that iterate trough the list as long as is not empty
    while short_messages:
        message = short_messages.pop()
        sent_messages.append(message)


# List with original messages
short_messages: list[str] = [
    "I love to learn python!",
    "Chess is a stimulating game.",
    "I'd love to visit the whole world."
]

# Create an empty list
sent_messages: list[str] = []

# Call the function to move messages from short_messages to sent_messages
send_messages(short_messages, sent_messages)

# Print both lists to show the result
print(f"This is the original list:{short_messages}\nThis is the list of sent messages: {sent_messages}")
