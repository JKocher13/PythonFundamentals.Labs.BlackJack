import classes

class Deal():
    def __int__(self, cards, score):
        self.cards = []
        self.score = 0

    def deal(self):
        x1 = classes.Deck.deal()
        x2 = classes.Deck.deal()
        self.cards.lst.append(x1,x2)

    def score(self):
        aces = False
        for card in self.cards:
            if card.value.isnumeric():
                self.score =+ int(card.value)
            elif card.value == "A":
                aces = True
                self.score =+ 11
            else:
                self.score =+ 10

        if self.score > 21 and aces == True:
            self.score -= 10

