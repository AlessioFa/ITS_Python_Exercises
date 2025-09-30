# Exercise 1-6

ITS_Bakery_Menù: dict[str, float] = {
    "Pizza": 9.00,
    "Pasta": 10.50,
    "Soup": 7.00,
    "Hamburger": 15.50,
    "Cutlet": 10.00,
    "Salmon": 20.20,
    "French Fries": 5.50,
    "Roasted Potatoes": 5.50,
    "Daily Vegetables": 7.00,
    "Cheesecake": 6.00,
    "Tiramisu": 6.00,
    "Focaccia with Nutella": 6.00,
    "Coca-Cola": 3.50,
    "Water": 1.50,
    "Wine": 5.00
    }

print("Restaurant Menu:\n")

for item, price in ITS_Bakery_Menù.items():
    print(f"{item}: {price:.2f} euros")

client_order: dict[str, float] = {
    "Pasta": 10.50,
    "Hamburger": 15.50,
    "French Fries": 5.50,
    "Acqua": 1.50,
    "Tiramisù": 6.00
    }

print("Client's order:")
for item, price in client_order.items():
    print(f"{item}: {price:.2f} euros")


total_price = sum(client_order.values())
print(f"\nThis is the price the client has to pay: {total_price}$")
