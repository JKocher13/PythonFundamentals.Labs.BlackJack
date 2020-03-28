import classes


class Deal():
    def __int__(self, cards, score):
        self.cards = []
        self.score = 0

    def hand(self):
        x1 = classes.Deck.deal()
        x2 = classes.Deck.deal()
        self.cards.lst.append(x1, x2)

    def calc_score(self):
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
        return self.score

    def hit(self):
        x3 = classes.Deck.deal()
        self.cards.append(x3)
        print(x3.value + " of " + x3.suit)
        self.calc_score()
        print("Your score is " + self.score)
        return self.score

    def stand(self):
        self.calc_score()
        print("Your ending score is " + self.score)


class dealer_moves(Deal):
    def __int__(self, cards, score):
        super().__init__(cards, score)

    def moves(self):
        print("Dealers first card is" + self.cards[0].value + " of " + self.cards[0].suit)
        print("Dealers first second is" + self.cards[1].value + " of " + self.cards[1].suit)
        while self.score < 17:
            print("Hit")
            self.hit()


class player_moves(Deal):
    def __int__(self, cards, score):
        super().__init__(cards, score)

    pass


