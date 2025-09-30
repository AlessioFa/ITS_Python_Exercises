sum_0: int = 0

for n in range(1, 11):
    sum_0 += n

sum_1: int = 0

for n in range(20, 38):
    sum_1 += n

sum_2: int = 0

for n in range(35, 50):
    sum_2 += n


print("This is the first sum: ",sum_0)
print(sum_1)
print(sum_2)

sommone =  sum(range(1,11))


def sum4(nMin: int, nMax: int):
    x = 0
    for n in range(nMin, nMax + 1):
        x += n 
    
    return x


print(sum4(1,10))
