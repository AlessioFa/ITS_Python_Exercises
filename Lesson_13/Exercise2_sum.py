""" Write a function called sum that takes a positive integer number n as input and returns the sum of the numbers from 0 to n.
If the input number n is negative, display an error message and the function must return None.
To implement the sum function, you must exclusively use a while loop and the parameter n passed as input to the function.
It is allowed to declare only one variable inside the function to manage the sum.
Then, call the function sum for n = -5 and n = 5.
Expected Output:
Error! Inserted number is negative!
None
--------------------------------------------------
15"
"""
def sum(n: int) -> int:
    if n < 0:
        
        print("Entered number is negative.")
        return None
    else:
        sum = 0
        
        while n:
            sum +=n
            n -= 1
        return sum


print(sum(10))
    
