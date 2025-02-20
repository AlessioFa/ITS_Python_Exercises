# Exercise 8-9: Messages

# Define a function to show messages
def show_messages(message: list[str]):
    # Loop thorugh each message in the list
    for text in message:
        print(text)


# Create a list containing a series of short text messages
short_messages: list[str] = [
    "I love to learn python!",
    "Chess is a stimulating game.",
    "I'd love to visit the whole world."
    ]

# Call and pass the list of messages
show_messages(short_messages)
