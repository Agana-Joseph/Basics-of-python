playerOne = input("what element does player one choos:: ")
playerTwo = input("what element does player two choos:: ")

if (playerOne == playerTwo):
    print("Its a tie")

elif (playerOne == "rock"):
    if (playerTwo == "paper"):
        print("player two wins")
    elif (playerTwo == "scissor"):
        print("player one wins")

elif (playerOne == "paper"):
    if (playerTwo == "rock"):
        print("player one wins")
    elif (playerTwo == "scissor"):
        print("player two wins")

elif (playerOne == "scissor"):
    if (playerTwo == "rock"):
        print("player two wins")
    elif (playerTwo == "paper"):
        print("player one wins")
