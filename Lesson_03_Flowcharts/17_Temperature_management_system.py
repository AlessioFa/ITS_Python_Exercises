t_max = -9999999
day_max: int = 0
t_min = 9999999
day_min: int = 0
count_normal: int = 0
average_t: int = 0
i: int = 1

while i < 8:
    user_temp: int= int(input(f"Enter a temperature for day{i}: "))
    average_t += user_temp

    if user_temp > t_max:
        t_max = user_temp
        day_max = i

    if user_temp < t_min:
        t_min = user_temp
        day_min = i

    if 10 <= user_temp <= 30:
        count_normal += 1

    if 5 > user_temp or user_temp > 35:
        print("Temperature alert.")

    i += 1

average_t = average_t / 7

print(f"The average temperature is: {average_t:.2f}")
print(f"The highest temperature reached is: {t_max}")
print(f"The lowest temperature reached is: {t_min}")
print(f"The day with the highest temperature is: {day_max}")
print(f"The day with the lowest temperature is: {day_min}")
