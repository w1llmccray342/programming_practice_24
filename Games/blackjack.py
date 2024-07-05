from .deck import *
from os import system
# Add an option to split the deck

def det_ace_best_value(ival):
    if ival <= 10:
        best_val = 11
    else:
        best_val = 1
    
    return best_val

def ante(chips):
    pass

# This will break on a second loop as it resets sum_of_cards, we need to take an initial value
def find_sum_of_cards(ival, hand):
    sum_of_cards = ival
    
    # Iterate through the list
    # Extract only the first element
    # We are looking at BOTH string values
    for cards in hand:
        # Extract the first element of Cards in this case the index of "0" should give us 6
        print(cards)
        print(type(cards))

            # We splice that to the
        my_temp_value = cards[0]
        my_int_temp_value = 0
      

        my_extract_value = str(my_temp_value)
            
        print(my_temp_value)
            
            # We use conditional statements to check and assign a value
           
        if my_extract_value == "10" or my_extract_value[0] in ["J", "Q", "K"]:
            my_int_temp_value = 10
           
        elif my_extract_value[0] == "A":
                # Needs to be some conditional logic for A since this is either 1 or 11 depending. Maybe a function, for now keep this at "11"
            det_ace_best_value(ival)
            
        else:
            my_int_temp_value = int(my_extract_value[0])

        sum_of_cards += my_int_temp_value
            
        print(my_int_temp_value)
            
        print(type(my_int_temp_value))
    
    return sum_of_cards

def my_stats(w, x, y, z):
    print(f"Dealer has a... {w[0]} and {w[1]}")
    print(f"Dealer is at {x} score.")
    print(f"Player has...{y[0]} and {y[1]}")
    print(f"Player is at {z} score.")
    print("What would you like to do?")




def player_options_handler(w):

    inner_game_running = True
    system('cls')


    while inner_game_running:
        my_stats()

        player_options()
    
        player_option = input("Please select one of the following options listed: ")
        
        # We need another conditional statement to determine what we should be using for our options on each hand.
        if player_option == 1:
            system('cls')
            hit_fn()
        elif player_option == 2: 
            system('cls')
            stand_fn()
        elif player_option == 3:
            system('cls')
            double_down_fn()


def player_options():
    print("1. Hit")
    print("2. Stand")
    print("3. Double Down")

def create_deck_blackjack():
    deck = Deck
    game_deck = deck.create_deck()

    return game_deck


# Player hits the desired number of times
def hit_fn(w):
    
    game_deck = create_deck_blackjack()
    first_hand = True

    if first_hand:
        x = 2
        first_hand = False
    
    else: 
        x = 1
    
    my_draw = Deck.draw_card(x, game_deck)
    my_score = find_sum_of_cards(w, my_draw)

    return my_draw, my_score
    
   


    
# Player can no longer hit AI is forced to hit.
def stand_fn(deck):
    pass

# Player doubles down ANTE for a single card, call hit fn once here and append that to player_score
# Return is 1.25 times for ANTE
def double_down_fn(deck):
    hit_fn(deck)

    pass

# If two of the same card then we call this function instead
def split(deck):
    pass 



# Blackjack game loop, player should have 21 to win.
def game_loop():
    # Deck should draw the first card it sees and assign it to player.
    game_running = True

    # Chips to start with
    player_chips = 400

    player_score = 0
    ai_score = 0

    # Fn to determine if deck is empty

    my_deck_is_empty = True
    first_draw = True

    if my_deck_is_empty == True:
       
        deck = Deck
        game_deck = deck.create_deck()
    
        while game_running:

            if first_draw:
                player_hand = deck.draw_card(game_deck, 2)
                print(game_deck)
                print(type(player_hand))
                print(player_hand[0:1])
                
                
                # Breaks at this point but what is the reason for it?
                # List index is out of range
                ai_hand = deck.draw_card(game_deck, 2)
                first_draw = False

            player_hand = list(player_hand[0])
            ai_hand = list(ai_hand[0])


            # Turn this to a function
            player_score = find_sum_of_cards(player_score, player_hand)
            ai_score = find_sum_of_cards(ai_score, ai_hand)

            player_options_handler(game_deck, ai_hand, ai_score, player_hand, player_score, game_running)



            

    


    
    
   