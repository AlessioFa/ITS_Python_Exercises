n: int = int(input("Enter a positive number: "))

if n <= 0:
    print("The value of n must be positive.")
else:
    count: int = 0
    i: int = 0

    while i < 10:
        x: int = int(input(f"Enter the number {i + 1}: "))

        if x % n == 0:
            count += 1

        i += 1

    print(f"The count is: {count}")
