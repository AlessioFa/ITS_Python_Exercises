# Exercise 8-14: Cars

# Different method to import a file

"""
# 1

import car_functions

car_detail = car_functions.make_car("subaru", "impreza", color="blue", tow_package=True)
print(car_detail)



car_detail = make_car("subaru", "impreza", color="blue", tow_package=True)

print(car_detail)"""


# 2
"""
from car_functions import make_car
car_detail = make_car("subaru", "impreza", color="blue", tow_package=True)
print(car_detail)

"""

# 3
"""
from car_functions import make_car as mc
car_detail = mc("subaru", "impreza", color="blue", tow_package=True)
print(car_detail)
"""

# 4
"""
import car_functions as cf
car_detail = cf.make_car("subaru", "impreza", color="blue", tow_package=True)
print(car_detail)"
"""

# 5
"""
from car_functions import *
car_detail = make_car("subaru", "impreza", color="blue", tow_package=True)
print(car_detail)"
"""
