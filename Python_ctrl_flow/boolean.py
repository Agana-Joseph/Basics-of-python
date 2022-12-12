age = int(input("How old are you? :: "))

if (age >= 18) and (age <= 24):
    print("You're among the young voters category")
elif (age >= 25) and (age <= 60):
    print("You're among the adault voters category")
else:
    print("You're not among the voters category")
