
n: int = int(input("Enter a number: "))

if n % 1 == 0 and n > 0:
    sum = 0
    i = 1

    while True:  
        if i > n: 
            print(f"The sum is: {sum}")
            break 

        sum = sum + i * i
        i = i + 1
else:
    print("n must be positive.")

