
n: int = int(input("How many numbers do you want to enter: "))

i: int = 0
user_sum = 0
average: int = 0
sum_even = 0
sum_odd = 0

while i < n:
    x: int = int(input(f"Enter the number {i + 1} of the list of {n} numbers: "))

    user_sum += x
    average = user_sum / (i + 1)

    if x % 2 == 0 and x > average:
        sum_even += x

    elif x < average or x % 2 != 0:
        sum_odd += x

    i += 1

print(f"The sum of even numbers is: {sum_even}")
print(f"The sum of odd numbers is: {sum_odd}")

if sum_even > sum_odd:
    print(f"Sum of even numbers ({sum_even}), is greater than the sum of odd numbers ({sum_odd})")

elif sum_odd > sum_even:
    print(f"The sum of odd numbers ({sum_odd}), is greater than the sum of even numbers ({sum_even})")

else:
    print("The sums are equal.")
