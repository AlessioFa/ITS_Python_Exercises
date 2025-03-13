while True: 
    n: int = int(input("Enter a n value: "))
    if n % 1 != 0:
        continue
    else:
        if 0 < n and n <= 100:
            sum_value = 0
            i = 1
            
            if i > n:
                print("The sum is:", sum_value)
            elif i % 2 == 0:
                sum += i
                i += 1
            else:
                i += 1
        
        if n == 0 or n < 0:
            print("Error.")
        else:
            sum_value = 0
            i = 1

            if i > n:
                sum += i
            elif i % 2 != 0:
