import unittest
from Tests import test_blackjack, test_cards

suite = unittest.TestLoader().loadTestsFromModule(test_blackjack)
unittest.TextTestRunner(verbosity=2).run(suite)

suite = unittest.TestLoader().loadTestsFromModule(test_cards)
unittest.TextTestRunner(verbosity=2).run(suite)