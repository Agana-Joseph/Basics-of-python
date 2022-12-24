import random


def DiceRoll(numbersOfRoll=1):
    dicsum = 0

    for i in range(numbersOfRoll):
        roll = random.randint(1, 6)
        dicsum += roll
        print(f'on roll number {i}, we got {roll}')

    return dicsum


print(DiceRoll(3))
