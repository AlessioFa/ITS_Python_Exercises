from random import randint
# Exercise 3: E-commerce Shopping Cart

"""
    Create a function that defines a product with a name, price, and quantity.
    Create functions that manage the shopping cart, allowing the user to add, remove, and view products in the cart.
    Create a function that calculates the cart total and apply any discounts or taxes.
    Create a funciton to print a detailed summary of the cart including products and totals.
    Implement a for loop to iterate over the items in the cart and print detailed information about each product and the total.
"""


def shopping_cart(name: str, price: float, quantity: int) -> dict:

    cart: dict = {
        "Name": name,
        "Price": price,
        "Quantity": quantity
        }

    return cart


def manage_shopping_cart():

    cart_list: list = []

    while True:
        user_option: str = input("You want to add, remove a product or view your shopping cart? Enter a valid option ( add, remove, view, quit): ").lower().strip()

        match user_option:
            case "add":
                product_name: str = input("Enter the name of the product you want to purchase: ")
                product_price: float = float(input("Product price: "))
                product_quantity: int = int(input("Enter the quantity of the product: "))

                product = shopping_cart(product_name, product_price, product_quantity)
                cart_list.append(product)

            case "remove":
                if not cart_list:
                    print("There is no product to remove. Try a different option.")
                    continue
                
                for index, product in enumerate(cart_list, start=1):
                    print(f"{index}. {product["Name"]} x{product["Quantity"]} -{product["Price"]}£")

                product_to_remove: int = int(input("Enter the number of product to remove: "))

                if 1 <= product_to_remove <= len(cart_list):

                    remove_product = cart_list.pop(product_to_remove - 1)

                    print(f"{remove_product["Name"]} has been removed.")
                
                else:
                    print("Please, enter a valid product number.")

            case "view":
                
                if not cart_list:
                    print("Your shopping cart is empy. You can purchase a product if you want to.")
                    continue

                for product in cart_list:
                    print(f"{product["Name"]} x {product["Quantity"]} = £{product["Price"]}")

            case "quit":
                print("Seeing you to the next shopping session!")
                break

            case _:
                print("Please, enter a valid option.")

    return cart_list


def cart_total(cart_list: list):

    if not cart_list:
        return ("Your cart in empty.")
    
    total_price: float = 0
    total_product_in_cart: int = cart_list["Quantity"]

    if not product["Quantity"] > 20:

        for product in cart_list:
            if product["Quantity"] > 1:
                total_price += product["Quantity"] * product["Price"]

    print(f"Your cart's total is: {total_price:.2f}£")



    total_product_in_cart = 0

    for product in cart_list:

        total_product_in_cart += product["Quantity"]


    



    



carrello = manage_shopping_cart()
totale_prezzi = cart_total(carrello)

print(carrello)
print(totale_prezzi)