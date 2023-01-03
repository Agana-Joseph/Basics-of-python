# Program that continously take a number from user and add it to a collective sum

sum = 0
userChoice = input("Would you like to choose a number?y/n:: ")

while (userChoice == 'y'):
    userNum = input("Enter your choice of number to be added:: ")
    sum += int(userNum)

    userChoice = input("Would you like to choose a number? ")
    print(f'The sum of the number entered is {sum}')
else:
    print('EXIT!')
