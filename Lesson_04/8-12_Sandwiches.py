# Exercise 8-12: Sandwiches

def item_s(*foods: str) -> None:
    ingredients = "Ingredient of your sandiwch: " + ", ". join(foods)
    print(ingredients)


item_s("bread", "hamburger", "onion", "bacon", "cheddar", "barbeque sauce")
item_s("bread", "hamburger", "mushrooms")
item_s("bread", "fried chicken", "mayonnaise", "pepper")
