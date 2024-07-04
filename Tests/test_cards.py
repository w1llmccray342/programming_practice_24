import unittest
from Games.deck import Deck

class Test_Config(unittest.TestCase):

    def test_draw_card(self):

        my_deck = Deck.create_deck()

        draw_card_res = Deck.draw_card(my_deck, 2)
        draw_card_res_2 = Deck.draw_card(my_deck, 1)
        draw_card_res_3 = Deck.draw_card(my_deck, -1)

        self.assertEqual(True, draw_card_res == type(list))
        self.assertEqual(True, draw_card_res_2 == type(list))
        self.assertEqual(False, draw_card_res_3 == type(list))