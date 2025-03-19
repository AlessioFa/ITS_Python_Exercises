"""Recursive Functions – Example 2- Iterative/1
Write a function sumInRange that calculates the sum of all integers between a and b, inclusive, where a and b are passed as
input to the function.
To solve the exercise, it is mandatory to use a while loop, and it is assumed that the value of b is always greater than the
value of a. Therefore, if a > b, it is necessary to swap the values to ensure that a is the smaller of the two.
Finally, it is allowed to declare only one variable, in addition to the function parameters, to store the sum.
Then, call the function sumInRange for a = 5, b = 10 and for a = 10, b = 5."""


def SumInRange(a: int, b:int) -> int:
    if a > b:
        sost = a
        a = b
        b = sost
    
    
    total = 0

    while b >= a:
        total += b
        b -= 1
    return total


print(SumInRange(10,20))
print(SumInRange(20, 10))



def SumInRange2(x:  int, y: int):
    if x > y:
        x, y = y, x
    
    total = 0

    while y >= x:
        total += y
        y -= 1
    return total

print(SumInRange2(10,20))






        




