password = "Onahi"
counter = 1
userGuess = input("Input the password: ")

while (userGuess != password):
    userGuess = input("Input the password: ")
    counter += 1
    if (counter == 5):
        print(
            f"you have been loged out of this system cause you tried {counter} times")
        break
if (userGuess == password):
    print(f"Hello user {password} you have successfully loged in")
