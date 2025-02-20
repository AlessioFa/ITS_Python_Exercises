# Exercise 8-12: Sandwiches

# Define a function that takes an 
def item_s(*foods: str) -> None:
    ingredients = "Ingredients of your sandiwch: " + ", ". join(foods)
    print(ingredients)


# Call the function with a different number of argument each time
item_s("bread", "hamburger", "onion", "bacon", "cheddar", "barbeque sauce")
item_s("bread", "hamburger", "mushrooms")
item_s("bread", "fried chicken", "mayonnaise", "pepper")
