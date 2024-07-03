import unittest
from Games.deck import draw_card

class Test_Config(unittest.TestCase):

    def test_draw_card(self):
        draw_card_res = draw_card(2)

        self.assertEqual(draw_card_res, draw_card(2) == draw_card_res)