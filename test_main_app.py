import unittest
import unittest.mock
import classes
import functions
import sys
import unittest
import io
from unittest import mock
from unittest.mock import patch


class TestFunctions(unittest.TestCase):
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
        self._player1.hand(self._card6, self._card3)
        text_trap = io.StringIO()
        sys.stdout = text_trap
        self._player1.calc_score()
        self._player2.hand(self._card4, self._card1)
        self._player2.calc_score()

    def test_determine_winner(self):
        with mock.patch("time.sleep"):
            self.assertEqual(functions.determine_winner(21, 21), "You both hit 21! Push")
            self.assertEqual(functions.determine_winner(18, 14), "Player wins with 18")
            self.assertEqual(functions.determine_winner(13, 18), "Dealer wins with 18")
            self.assertEqual(functions.determine_winner(40, 18), "You went bust, you lose")
            self.assertEqual(functions.determine_winner(18, 18), "You both had the same score of 18 Push!")
            self.assertEqual(functions.determine_winner(18, 22), "Dealer went bust! You win!")

    def test_dealer_goes(self):
        text_trap = io.StringIO()
        sys.stdout = text_trap
        self._player1.calc_score()
        self.assertEqual(functions.dealer_goes(21, "dealer"), "dealer")
        self.assertEqual(functions.dealer_goes(20, "dealer"), "dealer")
        self.assertEqual(functions.dealer_goes(22, "dealer"), None)

    def test_first_deal(self):
        x = functions.first_deal()
        self.assertIsInstance(x, list)
        self.assertIsInstance(x[0], tuple)
        self.assertIsInstance(x[0][0], object)
        self.assertIsInstance(x[0][0].suit, str)
        self.assertIsInstance(x[0][0].value, str)

    ths_input_try1 = "hit"
    ths_input_try2 = "stand"
    ths_input_try3 = "asd"

    @patch('builtins.input', return_value=ths_input_try1)
    def test_hit_or_stand_q1(self, mock_input):
        self.assertEqual(functions.hit_or_stand_q(), "hit")

    @patch('builtins.input', return_value=ths_input_try2)
    def test_hit_or_stand_q2(self, mock_input):
        self.assertEqual(functions.hit_or_stand_q(), "stand")

    def test_hitting(self):
        with unittest.mock.patch("functions.hit_or_stand_q", return_value="hit"):
            with mock.patch("functions.player_moves") as pm_patch:
                functions.hitting(self._player2)
                self.assertTrue(pm_patch.called)

    @patch("functions.hitting")
    def test_player_moves(self, hitting_mock):
        self.assertEqual(functions.player_moves(self._player1), "Congrats your at 21, let\'s see what the dealer has!")
        functions.player_moves(self._player2)
        self.assertTrue(hitting_mock.called)

    def test_check_for_black_jack(self):
        self.assertEqual(functions.check_for_black_jack(self._player1, self._player2), False)
        self.assertEqual(functions.check_for_black_jack(self._player2, self._player1), False)
        self.assertEqual(functions.check_for_black_jack(self._player2, self._player2), True)

    def test_dealer_moves(self):
        text_trap = io.StringIO()
        sys.stdout = text_trap
        with mock.patch("time.sleep"):
            self.assertEqual(functions.dealer_moves(self._player1, self._player2), 21)
            self.assertLess(self._player2.score, functions.dealer_moves(self._player2, self._player1))


class TestCards(unittest.TestCase):
    def __int__(self):
        pass

    def test__card_init(self):
        card = classes.Card(0, 0)
        assert isinstance(card, classes.Card)
        assert isinstance(card, object)


class test_Deck(unittest.TestCase):
    def __int__(self):
        pass

    def test__deck(self):
        deck = classes.Deck()
        self.assertIsInstance(deck, classes.Deck)
        self.assertIsInstance(deck, object)

    def test_deal(self):
        deck = classes.Deck()
        card1 = deck.deal()
        card2 = deck.deal()
        card3 = deck.deal()
        self.assertIsInstance(card1, classes.Card)
        self.assertIsInstance(card1, object)
        self.assertIsInstance(card2, classes.Card)
        self.assertIsInstance(card2, object)
        self.assertIsInstance(card3, classes.Card)
        self.assertIsInstance(card3, object)


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
        self.assertEqual(classes.Dealer_player.hand(self._player1, (4, 5), (5, 6)), [(4, 5), (5, 6)])
        self.assertIsInstance(classes.Dealer_player.hand(self._player2, self._card1, self._card2), list)

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
        text_trap = io.StringIO()
        sys.stdout = text_trap
        self._player5.cards.append(self._card5)
        self._player5.cards.append(self._card6)
        self._player3.cards.append(self._card3)
        self._player3.cards.append(self._card2)
        self._player4.cards.append(self._card6)
        self._player5.cards.append(self._card4)
        self.assertEqual(classes.Dealer_player.hit(self._player5, self._card1), 4)
        self.assertEqual(classes.Dealer_player.hit(self._player3, self._card1), 3)
        self.assertEqual(classes.Dealer_player.hit(self._player4, self._card1), 2)


if __name__ == '__main__':
    unittest.main()
