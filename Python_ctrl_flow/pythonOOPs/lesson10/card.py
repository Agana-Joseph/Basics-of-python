# Creat a OOP representation of a deck of cards
class Card:
    def __init__(self, suit, rank, point):
        self.suit = suit
        self.rank = rank
        self.point = point

    def prinCard(self):
        print("*---*")
        print(f"|{self.suit}  |")
        print(f"| {self.rank} |")
        print(f"|  {self.suit}|")
        print("*---*")
        print(f"{self.point}")


card1 = Card("♥", "K", 10)
card1.prinCard()
print(card1.point)
