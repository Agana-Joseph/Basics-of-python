# Creat a OOP representation of a deck of cards

import random
from typing import Self


class Card:
    def __init__(self, suit, rank, points):
        self.suit = suit
        self.rank = rank
        self.points = points

    def __str__(self):
        message = ""
        message += "*----*\n"
        message += f"|{self.suit}  |\n"
        message += f"| {self.rank}  |\n"
        message += f"|  {self.suit}|\n"
        message += "*----*\n"
        return message


class Deck:
    def __init__(self):
        self.deck = []

        self.makeDeck()
        self.shuffleDeck()

    def makeDeck(self):
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
                self.deck.append(newCard)

    def shuffleDeck(self):
        random.shuffle(self.deck)

    def returnCard(self):
        randomCard = random.choice(self.deck)
        self.deck.remove(randomCard)

        return randomCard


class player:
    def __init__(self, name):
        self.name = name
        self.deck = []
        self.score = 0

    def addCardTDeck(self, card):
        self.deck.append(card)
        self.score += card.points

    def hasBusted(self):
        if (self.score > 21):
            return True
        else:
            return False

    def prinDeck(self):
        for card in self.deck:
            print(card)


class dealer(player):
    def continueHittng(self):
        if (self.score < 17):
            return True


deck = Deck()
player = ("Joseph")
dealer = ("Dealer")

for i in range(2):
    playRandomCard = deck.returnCard()
    player.addCardTDeck(playerRandomCard)

    dealerRandomCard = deck.returnCard()
    dealer.addCardTDeck(dealerRandomCard)

dealer.printDeck()
print("0000000")
player.printDeck()
