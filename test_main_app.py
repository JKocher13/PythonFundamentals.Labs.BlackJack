import unittest
import classes
import functions


class TestFunctions(unittest.TestCase):
    def __int__(self):
        pass

    def test_determine_winner(self):
        self.assertEqual(functions.determine_winner(21, 21), "You both hit 21! Push")
        self.assertEqual(functions.determine_winner(18, 14), "Player wins with 18")
        self.assertEqual(functions.determine_winner(13, 18), "Dealer wins with 18")
        self.assertEqual(functions.determine_winner(40, 18), "You went bust, you lose")
        self.assertEqual(functions.determine_winner(18, 18), "You both had the same score of 18 Push!")
        self.assertEqual(functions.determine_winner(18, 22), "Dealer went bust! You win!")

    def test_dealer_goes(self):
        self.assertEqual(functions.dealer_goes(21, "dealer"), "dealer")
        self.assertEqual(functions.dealer_goes(20, "dealer"), "dealer")
        self.assertEqual(functions.dealer_goes(22, "dealer"), None)

    def test_first_deal(self):
        pass

    def test_hit_or_stand_q(self):
        pass

    def test_hitting(self):
        pass

    def test_player_moves(self):
        pass

    def test_check_for_black_jack(self):
        pass

    def test_dealer_moves(self):
        pass

    def test_announce_deal(self):
        pass


class TestCards(unittest.TestCase):
    def __int__(self):
        pass

    def test__card_init(self):
        card = classes.Card(0, 0)
        assert isinstance(card, classes.Card)
        assert isinstance(card, object)


class Test_Deck(unittest.TestCase):
    def test__deck_init(self):
        deck = classes.Deck()
        assert isinstance(deck, classes.Deck)
        assert isinstance(deck, object)

    def test_deal(self):
        deck = classes.Deck()
        card1 = deck.deal()
        card2 = deck.deal()
        card3 = deck.deal()
        assert isinstance(card1, classes.Card)
        assert isinstance(card1, object)
        assert isinstance(card2, classes.Card)
        assert isinstance(card2, object)
        assert isinstance(card3, classes.Card)
        assert isinstance(card3, object)


class test_Dealer_player(unittest.TestCase):
    def __int__(self):
        pass

    def setUp(self):
        self._player1 = classes.Dealer_player()
        self._player2 = classes.Dealer_player()
        self._player3 = classes.Dealer_player()
        self._player4 = classes.Dealer_player()
        self._player5 = classes.Dealer_player()
        self._card1 = classes.Card("Hearts", "8")
        self._card2 = classes.Card("Spades", "J")
        self._card3 = classes.Card("Clubs", "10")
        self._card4 = classes.Card("Diamonds", "2")
        self._card5 = classes.Card("Clubs", "K")
        self._card6 = classes.Card("Hearts", "A")



    def test_hand(self):
        self.assertEqual(classes.Dealer_player.hand(self._player1, (4 , 5),(5,6)),[(4,5),(5,6)])
        self.assertIsInstance(classes.Dealer_player.hand(self._player2,self._card1,self._card2),list)

    def test_calc_score(self):
        self._player3.cards.append(self._card1)
        self._player3.cards.append(self._card2)
        self._player4.cards.append(self._card5)
        self._player4.cards.append(self._card6)
        self._player5.cards.append(self._card5)
        self._player5.cards.append(self._card6)
        self._player5.cards.append(self._card4)
        self.assertEqual(classes.Dealer_player.calc_score(self._player3), 18)
        self.assertEqual(classes.Dealer_player.calc_score(self._player4), 21)
        self.assertEqual(classes.Dealer_player.calc_score(self._player5), 13)

    def test_hit(self):
        self._player5.cards.append(self._card5)
        self._player5.cards.append(self._card6)
        self._player3.cards.append(self._card1)
        self._player3.cards.append(self._card2)
        self._player4.cards.append(self._card6)
        self._player5.cards.append(self._card4)
        self.assertEqual(classes.Dealer_player.hit(self._player5, self._card1), 4)
        self.assertEqual(classes.Dealer_player.hit(self._player3, self._card1), 3)
        self.assertEqual(classes.Dealer_player.hit(self._player4, self._card1), 2)

if __name__ == '__main__':
    unittest.main()
