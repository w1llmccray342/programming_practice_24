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

def game_active():
    game_on = True

    return game_on

# Function to scan the player's hand and assign cards value should differ for 
def assign_value():
    pass

# Function to remove a played card from the deck.
def remove_card():
    pass

# Function to draw a given number of cards from a newly created deck
def draw_card(nums):

    # Call create_deck to create the first deck.

    # Need to see if deck is empty, if it is, we make another deck.
    # Can probably just reset the state of the game though to make this easier.
    create_deck()

    while True:

        drawn_cards = []
    
        my_deck = create_deck()

        print(my_deck)

        for card in range(nums):
            my_draw = random.randint(0, 3)
            my_second_draw = random.randint(0, 12)

        # Add drawn cards to drawn cards list
            drawn_cards.append(my_deck[my_draw][my_second_draw])   

        print(drawn_cards)
        return drawn_cards