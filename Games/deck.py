import random

def create_deck():
    default_deck = []
    

    default_suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    default_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]

    for suit in default_suits:
        default_list = []
        for value in default_values:
            temp_value = (f"{value} Of {suit}")
            default_list.append(temp_value)

        default_deck.append(default_list)

            

    return default_deck


def draw_card(nums):

    drawn_cards = []
    
    my_deck = create_deck()

    print(my_deck)

    for card in range(nums):
        my_draw = random.randint(0, 3)
        my_second_draw = random.randint(0, 12)

        # Add drawn cards to drawn cards list
        drawn_cards.append(my_deck[my_draw][my_second_draw])   

    print(drawn_cards)
    print(my_deck)