north_south: int = int(input("Enter the number of vehicles passing through the north-south road: "))

east_west: int = int(input("Enter the number of vehicles passing through the east-west road: "))

threshold: int = 70

if north_south > threshold and east_west > threshold:
    time_ns: int = 50
    time_ew: int = 50

elif north_south > threshold:
     time_ns: int = 60
     time_ew: int = 40
    
elif east_west > threshold:
     time_ns: int = 40
     time_ew: int = 60

else:
     time_ns = (north_south/(north_south + east_west)) * 100
     time_ew = (east_west/(north_south + east_west)) * 100

print(f"The assigned time at north-south direction is {time_ns:2f}")
print(f"The assigne time at east-west direction is: {time_ew:2f}")
