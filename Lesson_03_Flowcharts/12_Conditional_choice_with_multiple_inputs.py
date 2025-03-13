n: int = int(input("Enter the number ov values: "))
i: int = 0

while i < n:
    x: int = int(input("Enter the value of x: "))
    y: int = int(input("Enter the value of y: "))

    if x > 0 and y > 0:
        result: int = x * y
        print(f"The result is: {result}")

    elif x < 0 and y < 0:
        print("Error.")

    else:
        result = x - y
        print(f"The result is{result}.")
    i += 1
