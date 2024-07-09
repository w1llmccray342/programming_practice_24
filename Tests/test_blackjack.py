import unittest
from Games.blackjack import find_sum_of_cards, det_ace_best_value, check_scores_end_game
class Test_Config(unittest.TestCase):

    def test_blackjack_sum_of_cards(self):
        my_cards = ["2 Of Hearts", "3 Of Hearts"] 
        ival = 0

        self.assertEqual(5, find_sum_of_cards(ival, my_cards))

    def test_blackjack_det_ace_best_value(self):

        for x in range(1, 21):
            if x <= 10:
                self.assertEqual(11, det_ace_best_value(x))
                print(x, "Best value is 11!")
            else:
                self.assertEqual(1, det_ace_best_value(x))
                print(x, "Best value is 1!")