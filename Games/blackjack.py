from deck import *
import os
# Add an option to split the deck



def det_ace_best_value(ival):
    if ival <= 10:
        best_val = 11
    else:
        best_val = 1
    
    return best_val

def ante(chips):
    pass

def continue_op():
    continue_opt = input("Press Y to continue or N to close the program: ")
    continue_opt.upper()

    if continue_opt == "Y":
        os.system("clear")
        return True
    else:
        return False


# This will break on a second loop as it resets sum_of_cards, we need to take an initial value
def find_sum_of_cards(ival, hand):
    sum_of_cards = ival
    my_hand = hand

    print(f"Current hand value is at {sum_of_cards}")
    
    # Iterate through the list
    # Extract only the first element
    # We are looking at BOTH string values
    for cards in my_hand:

        # Extract the first element of Cards in this case the index of "0" should give us 6
        print(f"Cards present are... {cards}")
        print(type(cards))
 
      
        if "10" == cards[0:2] or cards[0] in ["J", "Q", "K"]:
            my_int_temp_value = 10
            
        elif "A" == cards[0]:
            # Needs to be some conditional logic for A since this is either 1 or 11 depending. Maybe a function, for now keep this at "11"
         my_int_temp_value = det_ace_best_value(sum_of_cards)
           
        else:
         my_int_temp_value = int(cards[0])
        
    sum_of_cards += my_int_temp_value
                
    print(my_int_temp_value)
                
    print(type(my_int_temp_value))
    print(f"Adding {cards} to {my_hand} we get... {sum_of_cards}")
        
    return sum_of_cards

def my_stats(score_ai, score_human, ai_hand, player_hand):
    print(f"Dealer has a... {ai_hand}")
    print(f"Dealer is at {score_ai} score.")
    print(f"Player has...{player_hand}")
    print(f"Player is at {score_human} score.")
    print("What would you like to do?")


def player_options():
    print("1. Hit")
    print("2. Stand")
    print("3. Double Down")
    print("4. Split")

def create_deck_blackjack():
    deck = Deck
    game_deck = deck.create_deck()

    return game_deck

def check_scores_set_win(game_state, ai_score, player_score):
    player_win = False
    ai_win = False
    game_over = game_state

    if ai_score > player_score and not ai_score > 21 and not ai_score == 21:
        print("The house always wins!")
        ai_win = True
  
    elif ai_score < player_score and not player_score > 21 and not player_score == 21:
        print("Heey that's what we like to see")
        player_win = True

    elif ai_score == 21:
        print("Tough luck.")
        ai_win = True

    elif player_score == 21:
        print("Blackjack! You win!")
        player_win = False

    return player_win, ai_win, game_over

    

# Player hits the desired number of times
def hit_fn(deck, hand):
    
    new_card = Deck.draw_card(deck, 1)[0]
    print(f"Hand is {hand}")
    
    for x in new_card:
        hand.append(x)
    print(f"New hand is {hand}")

    return hand, deck
   


    
# Player can no longer hit AI is forced to hit.
def stand_fn(deck):
    pass

# Player doubles down ANTE for a single card, call hit fn once here and append that to player_score
# Return is 1.25 times for ANTE
def double_down_fn(deck):

    pass

# If two of the same card then we call this function instead
def split(deck):
    pass 



def player_options_handler(deck, score_ai, score_human, ai_hand, player_hand, chips):

    inner_game_running = True
    
    while inner_game_running == True:
       

        os.system("clear")

        my_stats(score_ai, score_human, ai_hand, player_hand)

        # After counting check to make sure that player_score is not above 21 and ai_score is not above 21 every round

        player_options()
    
        player_option = int(input("Please select one of the following options listed: "))
        
        # We need another conditional statement to determine what we should be using for our options on each hand. If we see certain cards we should split accordingly. Hit, stand, double down, and split are always available
        # Do all player moves here.
        # Do all ai moves here
        # os.system("clear")
        if player_option == 1:
            print(type(player_hand), player_hand)
            # Overwrite player_hand
            ow_list = hit_fn(deck, player_hand)  
            ow_list = list(ow_list)
            player_hand = ow_list[0]
            deck = ow_list[1]

            score_human = find_sum_of_cards(score_human, player_hand)
        
        elif player_option == 2: 
            stand_fn()
        
        elif player_option == 3:
            double_down_fn(chips)
        
        inner_game_running = continue_op()




# Blackjack game loop, player should have 21 to win.
def game_loop():

    # Deck should draw the first card it sees and assign it to player.
    game_running = True

    # Chips to start with
    player_chips = 400

    player_score = 0
    ai_score = 0
    
    while game_running:
        

        game_deck = create_deck_blackjack()

        first_draw = True

        # 165 thru 187 can probably be collapsed to a function
        if first_draw:
            x = 2
            first_draw = False
        else:
            x = 1

        player_hand = Deck.draw_card(game_deck, x)
        print(game_deck)
        print(type(player_hand))
        print(player_hand[0:1])
                
                
                # Breaks at this point but what is the reason for it?
                # List index is out of range
        ai_hand = Deck.draw_card(game_deck, x)

        player_hand = list(player_hand[0])
        ai_hand = list(ai_hand[0])


            # Turn this to a function
        player_score = find_sum_of_cards(player_score, player_hand)
        ai_score = find_sum_of_cards(ai_score, ai_hand)

        print(player_hand, ai_hand, player_score, ai_score)
    
      

        player_options_handler(game_deck, ai_score, player_score, ai_hand, player_hand, player_chips)
        


            

    


    
    
   