# Coin flip, this print Taill if the coin rolled 0 and print Head if it rolled 1.

import random

headsCounter = 0
tailCounter = 0

for i in range(100):
    flip = random.randint(0, 1)
    if (flip == 1):
        headsCounter += 1
    else:
        tailCounter += 1

print("HeadsCounter: ", headsCounter)
print("TailCounter: ", tailCounter)

"""
char = ('Head', 'Tail')
CoinPlay = random.choice(char)
print(CoinPlay)
"""
