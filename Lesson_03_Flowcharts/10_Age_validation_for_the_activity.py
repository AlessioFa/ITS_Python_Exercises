age: int = int(input("Enter your age: "))

if age >= 18 and age <= 65:
    print("You can join the activity.")
else:
    if age < 18:
        print("You cannot join the activity because you don't meet the age requirement.")
    else:
        print("You cannot join the activity because you have exceeded the maximum allowed age.")
