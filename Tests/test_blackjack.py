import unittest
from Games.blackjack import find_sum_of_cards
class Test_Config(unittest.TestCase):

    def test_blackjack_sum_of_cards(self):
        my_cards = ["2 Of Hearts", "3 Of Hearts"] 
        ival = 0

        self.assertEqual(5, find_sum_of_cards(ival, my_cards))