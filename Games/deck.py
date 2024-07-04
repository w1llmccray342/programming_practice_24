import random


class Deck: 
    def __init__(self) -> None:
        pass
   
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

        print(default_deck)
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
    def draw_card(deck, nums):

        # Call create_deck to create the first deck.

        # Need to see if deck is empty, if it is, we make another deck.
        # Can probably just reset the state of the game though to make this easier.

        while True:

            drawn_cards = []

            print(deck)

            for card in range(nums):
                my_draw = random.randint(0, 3)
                my_second_draw = random.randint(0, 12)

            # Add drawn cards to drawn cards list
                drawn_cards.append(deck[my_draw][my_second_draw])   

            # Remove drawn cards from list.
                drawn_cards.remove(deck[my_draw][my_second_draw])


            print(drawn_cards)
            print(deck[my_draw][my_second_draw]) #Should print out nothing
            return drawn_cards, deck