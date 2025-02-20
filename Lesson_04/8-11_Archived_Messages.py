# Exercise 8-11: Archived Message 

"""I'm going to modify this exercise aswell

# Define a function that takes messages form a list and puts them in another one
def show_messages(phrases: list[str]) -> list[str]:
    new_short_messages = []
    
    while len(phrases) > 0:
        message = phrases.pop()
        new_short_messages.append(message)
    
    print("Final list: ", new_short_messages)
    
    if len(phrases) == 0:
        new_list_copy = new_short_messages.copy()
    
    print("Copy of the final list : ", new_list_copy)


# Create a list the shows short messages
short_messages: list[str] = [
    "I love to learn python!",
    "Chess is a stimulating game.",
    "I'd love to visit the whole world."
    ]

show_messages(short_messages)
"""


# Define a function
def send_messages(short_messages: list[str], sent_messages: list[str]) -> list[str]:
    while short_messages:
        message = short_messages.pop()  # Take a message from the original list
        sent_messages.append(message)   # Add the message to sent_messages

    # Print both lists
    print("Original list:", short_messages)
    print("Sent messages:", sent_messages)


# The list of original messages
short_messages: list[str] = [
    "I love to learn python!",
    "Chess is a stimulating game.",
    "I'd love to visit the whole world."
]

# Create an empty list where the messages will go
sent_messages: list[str] = []

# Call the function with a copy of short_messages so it doesn't affect the original list
send_messages(short_messages.copy(), sent_messages)

# Print both lists after calling the function
print(f"Original list after calling send_messages(): {short_messages}")
print(f"Sent messages after calling send_messages(): {sent_messages}")
