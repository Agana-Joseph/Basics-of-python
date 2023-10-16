# Creat a OOP representation of a deck of cards
class Card:
    def __init__(self, suit, rank, point):
        self.suit = suit
        self.rank = rank
        self.point = point

    def printCard(self):
        print("*----*")
        print(f"|{self.suit}  |")
        print(f"| {self.rank}  |")
        print(f"|  {self.suit}|")
        print("*----*")


dec = []

suits = ["💛", "💎", "💎", "🧡"]
rankAndPoint = {
    "A": 11,
    "K": 11,
    "Q": 10,
    "J": 10,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2

}

for suit in suits:
    for rank, point in rankAndPoint.items():
        newCard = Card(suit, rank, point)
        dec.append(newCard)

for card in dec:
    card.printCard()
