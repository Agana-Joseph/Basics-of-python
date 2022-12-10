import random


def guess(x):

    guess = 0
    random_number = random.randint(1, x)

    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}:: "))
        if guess < random_number:
            print("Number guess is low. try agian")
        elif guess > random_number:
            print("Number guess is high. try again")
    print(f"Yay, you guess the number {random_number} right")


guess(5)
