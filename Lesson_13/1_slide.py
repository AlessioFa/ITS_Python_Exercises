"""Write a Python function called countdown that takes a positive integer n as input and prints a countdown from n to zero.
If the input number is negative, display an error message.
To implement the function, you must exclusively use a while loop and the parameter n passed as input to the function.
Declaring any additional variables inside the function is not allowed.
Then, call the function with n = -5 and n = 5.
Expected Output:
Error! Inserted number is negative!
-------------------------------------------------
5
4
3
2
1
0
"""

def countdown(n: int):
    if n < 0:
        print("Error: the entered number is negative.")
        return
    while n >= 0:
        print(n)
        n -= 1
    

countdown(-10)

countdown(10)
