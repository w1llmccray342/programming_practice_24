import unittest
from Games.deck import Deck

class Test_Config(unittest.TestCase):

    def test_draw_card(self):
        draw_card_res = Deck.draw_card(2)
        draw_card_res_2 = Deck.draw_card(1)
        draw_card_res_3 = Deck.draw_card(-1)

        self.assertEqual(True, Deck.draw_card(2) == type(list))
        self.assertEqual(True, Deck.draw_card(1) == type(list))
        self.assertEqual(False, Deck.draw_card(-1) == type(list))