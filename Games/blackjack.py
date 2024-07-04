from deck import *
# Add an option to split the deck

def det_ace_best_value(ival):
    pass

def ante(chips):
    pass

# This will break on a second loop as it resets sum_of_cards, we need to take an initial value
def find_sum_of_cards(ival, hand, score):
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


def player_options_handler():
    player_option = 0

    player_option = input("Please select one of the following options listed: ")
    
    if player_option == 1:
        hit_fn()
    elif player_option == 2: 
        stand_fn()
    elif player_option == 3:
        double_down_fn()


def player_options():
    print("1. Hit")
    print("2. Stand")
    print("3. Double Down")

    player_options_handler()

def hit_fn():
    pass
    

def stand_fn():
    pass

def double_down_fn():
    pass



# Blackjack game loop, player should have 21 to win.
def game_loop():
    # Deck should draw the first card it sees and assign it to player.
    game_running = True

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

            player_score = find_sum_of_cards(player_score, player_hand)
            ai_score = find_sum_of_cards(ai_score, ai_hand)

     

            print(f"Dealer has a... {ai_hand[0]} and {ai_hand[1]}")
            print(f"Dealer is at {ai_score} score.")
            print(f"Player has...{player_hand[0]} and {player_hand[1]}")
            print(f"Player is at {player_score} score.")

            print("What would you like to do?")
            player_options()


            game_running = False
    


    
    
   