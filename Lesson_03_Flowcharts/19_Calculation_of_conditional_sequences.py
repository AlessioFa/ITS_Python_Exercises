n: int = int(input("Enter an integer value: "))

if n > 0:
    if n % 2 == 0:
        count: int = 4
        result: int = 0

        if count <= n:
            result = result + count
            count = count + 4
        else:
            print(result)
    
    elif n % 2 != 0:
        count = 1
        result = 1

        if count <= n:
            result = result * count
            count = count + 2

        else:
            print("")
        