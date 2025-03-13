a: int = int(input("Enter the first number: "))
b: int = int(input("Enter the second number: "))

if a > b:
    print("A must be less than B")
elif a < b:
    if a > 0 and b > 0:
        if a % 1 == 0 and b % 1 == 0:
            sum: int = 0
            i = a

            while i <= b:
                sum += i
                i += 1
            print("The sum is:", sum)
        else:
            print("The value of a and b must be integers.")
