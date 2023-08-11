voters = int(input("How old are you?: "))
if (voters < 18):
    print("you're under age and you can't vot yet, wait till you're 18yrs and above")
elif (voters >= 18):
    print("you are quolified to vote.")
else:
    print("Age not specify")
