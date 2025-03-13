x: int = int(input("Enter a positive number: "))

if x < 0:
    print("X has to be positive.")
else:
    sum: int = 0
    i: int = 0

    while i < 10:
        n: int = int(input("Enter a number: "))

        if x % 2 == 0:
            if n > x / 2:
                sum += n

        elif x % 2 != 0:
            if n < x:
                sum += n

        i += 1

    print(f"The sum is: {sum}")
