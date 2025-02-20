# Exercise 8-11: Archived Message 

# Define a function that takes messages form a list and put it in another one then create a copy of it 
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
