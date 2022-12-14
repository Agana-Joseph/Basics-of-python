# A function that take two numbers and print the bigest one

def numbersNum(firstNum, secondNum):
    if firstNum > secondNum:
        print(f"{firstNum} is the bigest")
    elif secondNum > firstNum:
        print(f"{secondNum} is the bigest")
    else:
        print('The numbers are the same')


numbersNum(90, 90)
