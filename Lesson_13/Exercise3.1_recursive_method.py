"""Recursive Functions – Example 2- Recursive/1
Write a recursive function recursiveSumInRange that calculates the sum of all integers between a and b, inclusive, where a
and b are passed as input to the function.
Assume that the value of b is always greater than the value of a. Therefore, if a > b, it is necessary to swap the values to
ensure that a is the smaller of the two.
Then, call the function recursiveSumInRange for a = 5, b = 10 and for a = 10, b = 5.
Expected Output:
45
-------
45"""

def recursiveSumInRange(a: int, b: int) -> int:
    # if a > b, swap values of a and b
    if a > b:
        # define a temporary variable called temp, containing value of a
        temp:int = a
        # swap values of a and b
        a = b
        b = temp # now b = a
    # if b = a, the recursive process must be stopped
    if b == a:
        return int(a)
    # otherwise, compute the sum recursively
    else:
        return int(b + recursiveSumInRange(a, b-1))
    

print(recursiveSumInRange(10, 20))


# Alternative Method

def recursiveSumInRange(a: int, b: int) -> int:
    # If a > b, swap the values
    if a > b:
        a, b = b, a
    
    # Base case, if a == b we return a 
    if a == b:
        return a
    
    # Passaggio ricorsivo: sommiamo b e chiamiamo la funzione con b-1
    return b + recursiveSumInRange(a, b - 1)
    
    # casting is not necessary
    # this swap method is more clear

