position :int = int(input("Enter a position: "))

if position < 1:
    print(f"You should insert a valid number.")
    position :int = int(input("Enter a position: "))
if position == 1:
    print(f"Your position is: {position}st")
elif position == 2:
    print(f"Your position is: {position}nd")
elif position == 3:
    print(f"Your position is: {position}rd")
else:
    print(f"Your position is: {position}th")




