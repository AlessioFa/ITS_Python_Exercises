
v = [1, 2, 3, 3, 2, 1]
centrale: int = 2

if sum(v[:centrale + 1]) == sum(v[centrale: + 1]):

    print(centrale)

else:

    print("NOPE!!!!")



print(v[centrale: ])