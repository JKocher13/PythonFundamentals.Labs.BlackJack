import unittest
import classes
import functions



class TestFunctions(unittest.TestCase):
    def __int__(self):
        pass

    def test_determine_winner(self):
        self.assertEqual(functions.determine_winner(21,21), "You both hit 21! Push")
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

    def test_hand(self):
        player1 = classes.Dealer_player()
        player2 = classes.Dealer_player()
        self.assertEqual(classes.Dealer_player.hand(player1,("10", "Spades"), ("A","Hearts")),
                         [("10", "Spades"), ("A","Hearts")])
        self.assertEqual(classes.Dealer_player.hand(player2, ("8", "Diamonds"), ("K", "Clubs")),
                         [("8", "Diamonds"), ("K", "Clubs")])

    def test_calc_score(self):






if __name__ == '__main__':
    unittest.main()