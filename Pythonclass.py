# Calculate users age
name = input("what is your name: ")
birthYear = int(input("What is your birth year? "))
curent_age = (2023 - birthYear)
print(f"Hi {name} you're {curent_age} years old")


# Print even number
for i in range(0, 20, 2):
    print(i)

# (2) program that prompts the user to enter their age. Based on the age, check if they are eligible to vote
voters = int(input("How old are you?: "))
if (voters < 18):
    print("you're under age and you can't vot yet, wait till you're 18yrs and above")
elif (voters >= 18):
    print("you are quolified to vote.")
else:
    print("Age not specify")


# (3) program that takes a user's input for a number and checks if it is divisible by both 5 and 7
userNum = int(input("Enter number your choice: "))
if (userNum // 5 and userNum // 7):
    print("Congratulation the number you entered can be devided by 5 & 7")
else:
    print("Sorry! the number you entered can't be devided by 5 or 7")


# (4)Function that accepts three integers as input and returns the largest of the three.
print("You have three chances to insert a number to be checked to know which is the highest")
num1 = int(input("Enter the first number to be checked: "))
num2 = int(input("Enter the second number to be checked: "))
num3 = int(input("Enter the third number to be checked: "))
if (num1 > num2 and num1 > num3):
    print(f"The first number ({num1}) is the highest")
elif (num2 > num1 and num2 > num3):
    print(f"The second number ({num2}) Is the gratest")
elif (num3 > num1 and num3 > num2):
    print(f"The third number ({num3}) Is the gratest")
else:
    print(f"{num1}, {num2}, {num3} Are all equall")
