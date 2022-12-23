import random

diceSum = 0

for i in range(2):

    diceRoll = random.randint(0, 6)
    print('Dice rolled', diceRoll)
    diceSum += diceRoll
print('Dice sum is: ', diceSum)
