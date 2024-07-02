import random

def create_deck():
    default_deck = {}

    default_suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    default_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

    for suit in default_suits:
        for value in default_values:
            default_deck.update({suit: value})
            

    print(default_deck)

    return default_deck


def draw_card(nums):
    my_draw = random.randint(0, 52)
    pass