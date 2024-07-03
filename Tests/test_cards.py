import unittest
from Games.deck import draw_card

class Test_Config(unittest.TestCase):

    def test_draw_card(self):
        draw_card_res = draw_card(2)
        draw_card_res_2 = draw_card(1)
        draw_card_res_3 = draw_card(-1)

        self.assertEqual(True, draw_card(2) == type(list))
        self.assertEqual(True, draw_card(1) == type(list))
        self.assertEqual(False, draw_card(-1) == type(list))