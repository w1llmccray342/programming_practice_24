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

    def check_if_empty(deck, suit_index):
        
        if (all(len(deck[suit_index]) == 0)):
            print("Deck is empty, creating a new deck!")
            deck = Deck.create_deck()

        return deck

    # Function to draw a given number of cards from a newly created deck
    def draw_card(deck, nums):

        # Call create_deck to create the first deck.

        # Need to see if deck is empty, if it is, we make another deck.
        # Can probably just reset the state of the game though to make this easier.

        drawn_cards = []
        print(f"Current deck length is {len(deck)}")

        
        for _ in range(nums):
            while  True:
                suit_index = random.randint(0, 3)
                if deck[suit_index]:
                    break

            Deck.check_if_empty() 
           

            card_index = random.randint(0, len(deck[suit_index]) - 1)
            drawn_card = deck[suit_index].pop(card_index)
            drawn_cards.append(drawn_card)        
        
        print(drawn_cards, "Were removed from the deck!")
        return drawn_cards, deck
