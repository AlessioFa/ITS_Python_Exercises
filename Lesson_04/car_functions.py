# From Exercise 8-14: Cars

# Define a function that returns a dict
def make_car(manufacturer: str, model: str, **car_info):
    car_info["manufacturer"] = manufacturer
    car_info["model"] = model

    return car_info


"""
car_detail = make_car("subaru", "impreza", color="blue", tow_package=True)

print(car_detail)"""
