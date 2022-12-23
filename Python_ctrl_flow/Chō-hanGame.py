# ChoHan game Roll dice with the sum of the both dice, It is cho if it even, han if its odd
import random
diceSum = 0
userGuess = input("What did you think the game will print Cho or Han? [C/H]: ")

for i in range(2):  # the both dice

    diceRoll = random.randint(0, 6)  # the total numbers of dice count
    print('Dice rolled', diceRoll)
    diceSum += diceRoll
print('Dice sum is: ', diceSum)
if (diceSum % 2 == 0):
    print("Dice sum is even.")
    if (userGuess == "C"):
        print("You win🎉")
    else:
        print('You lose❗')
else:
    print("Dice sum is odd.")
    if (userGuess == 'H'):
        print('You win🎉')
    else:
        print('You lose❗')
