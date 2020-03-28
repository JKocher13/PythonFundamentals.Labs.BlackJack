import classes


class Dealer_player():
    def __init__(self):
        self.cards = []
        self.score = 0


    def hand(self,card1, card2):
        self.cards.append(card1)
        self.cards.append(card2)

    def calc_score(self):
        aces = False
        self.score = 0
        for card in self.cards:
            if card.value.isnumeric():
                self.score += int(card.value)
            elif card.value == "A":
                aces = True
                self.score += 11
            else:
                self.score   += 10

        if self.score >= 22 and aces == True:
            self.score -= 10

    def hit(self,card3):
        x3 = card3
        self.cards.append(x3)
        print(x3.value + " of " + x3.suit)
        self.calc_score()


