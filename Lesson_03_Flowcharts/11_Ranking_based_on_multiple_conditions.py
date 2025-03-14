n: int = int(input("Enter an integer number: "))

while True:
    n: int = int(input("Enter an integer number: "))
    
    if not n % 1 == 0:
        continue
    else:
        if n % 2 == 0 and n > 10:
            print("Valid number.")
        else:
            print("Number not valid.")
            break
