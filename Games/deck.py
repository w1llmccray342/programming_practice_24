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
        i = 0

        drawn_cards = []
        removed_cards = []
        new_deck = deck


        while i < nums:
            my_draw = random.randint(0, 3)
            my_second_draw = random.randint(0, 12)

            for i in range(nums):
                removed_cards.append(new_deck[my_draw][my_second_draw])
                drawn_cards.append(new_deck[my_draw][my_second_draw])
                del(new_deck[my_draw][my_second_draw]) 

                
                
            print(new_deck) #Should print out nothing
            print(drawn_cards)
            print(f"Here are the removed cards: {removed_cards}")

            i += 1    
        
        return drawn_cards, list(new_deck)