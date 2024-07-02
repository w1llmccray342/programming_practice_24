import random

def create_deck():
    default_deck = {}

    default_suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    default_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

    for suit in default_suits:
        for value in default_values:
            default_deck[suit] = value
            print(f"{value} of {suit}s")

    return default_deck

