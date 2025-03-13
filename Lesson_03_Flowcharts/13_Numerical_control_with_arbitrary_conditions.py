x: int = int(input("Enter the value of x: "))
y: int = int(input("Enter the value of y: "))
z: int = int(input("Enter the value of z: "))


if x % 1 != 0 or x <= 0:
    print("x must be a positive integer.")
else:

    if y % 1 != 0 or y <= 0:
        print("y must be a positive integer.")
    else:

        if z % 1 != 0 or z <= 0:
            print("z must be a positive integer.")
        else:

            if (x + y + z) % 2 == 0 and x % 3 == 0 and y % 5 == 0 and z % 7 == 0:
                print("Rules respected.")
            else:
                print("Rules not respected.")
