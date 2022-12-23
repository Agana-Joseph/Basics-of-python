# Dice roll with the sum of the both dice

import random

diceSum = 0

for i in range(2):  # the both dice

    diceRoll = random.randint(0, 6)  # the total numbers of dice count
    print('Dice rolled', diceRoll)
    diceSum += diceRoll
print('Dice sum is: ', diceSum)

if (diceSum % 2 == 0):
    print("Dice sum is even.")
else:
    print("Dice sum is odd.")
