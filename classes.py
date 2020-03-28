import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


class Deck:
    def __init__(self):
        self.cards = [Card(s, v) for s in ["Spades", "Clubs", "Hearts", "Diamonds"]
					  for v in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]]

    def deal(self):
        x = self.cards.pop(self.cards.index(random.choice(self.cards)))
        return x


