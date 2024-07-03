import unittest
from Tests import test_blackjack

suite = unittest.TestLoader().loadTestsFromModule(test_blackjack)
unittest.TextTestRunner(verbosity=2).run(suite)