# Exercise 8-13: User Prophile

def build_profile(first_name: str, last_name: str, **details) -> str:

    profile = f"{first_name} {last_name}"

    # Add more details
    for key, value in details.items():
        profile += f", {key} {value}"

    return profile


# Assign some values and calling the function 
user_profile = build_profile("Alessio", "Farallo", age=29, hair="brown", weight=67)
print(user_profile)
