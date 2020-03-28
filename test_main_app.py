import unittest
import classes
import main_app
import dealer_and_player



class TestFunctions(unittest.TestCase):
    def __int__(self):
        pass

    def test_determine_winner(self):
        self.assertEqual(main_app.determine_winner(21, 21), "Push")

if __name__ == '__main__':
    unittest.main()