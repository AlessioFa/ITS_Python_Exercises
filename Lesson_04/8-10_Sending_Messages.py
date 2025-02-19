# Exercise 8-10: Sending Messages

# Define a function that takes messages form a list and put it in another one 
def show_messages(phrases: list[str]):
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

show_messages(short_messages)
