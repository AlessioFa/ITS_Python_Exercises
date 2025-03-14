odds: int = 0
even: int = 0
negative: int = 0
positive: int = 0
i: int = 0

while i < 10:
    n: int = int(input("Enter a number: "))

    if not (n % 1 == 0 and n != 0):
        continue

    if n > 0:
        positive += 1
        if n % 2 == 0 and n > 20:
            even += 1
    elif n < 0:
        negative += 1
        if n % 2 != 0 or n < -10:
            odds += 1

    i += 1


print(f"Positive numbers: {positive}")
print(f"Negative numbers: {negative}")
print(f"Positive and even numbers > 20: {even}")
print(f"Negative and odd numbers or < -10: {odds}")
