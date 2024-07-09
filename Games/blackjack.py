from deck import *
import os
# Add an option to split the deck



def det_ace_best_value(ival):
    return 11 if ival <= 10 else 1

def ante(chips):
    pass

def continue_op():
    continue_opt = input("Press Y to continue or N to close the program: ").upper()

    if continue_opt == "Y":
        os.system("clear")
        return True
    else:
        return False


# This will break on a second loop as it resets sum_of_cards, we need to take an initial value
def find_sum_of_cards(ival, hand):
    sum_of_cards = ival
    

    print(f"Current hand value is at {sum_of_cards}")
    
    # Iterate through the list
    # Extract only the first element
    # We are looking at BOTH string values
    for cards in hand:

        # Extract the first element of Cards in this case the index of "0" should give us 6
        print(f"Cards present are... {cards}")
        print(type(cards))

        print(f"Card strings present {cards[0:2]}")

      
        if cards[0:2] == "10" or cards[0] in ["J", "Q", "K"]:
            my_int_temp_value = 10
            
        elif cards[0] == "A":
         my_int_temp_value = det_ace_best_value(sum_of_cards)
           
        else:
         my_int_temp_value = int(cards[0])
        
        sum_of_cards += my_int_temp_value
        
    return sum_of_cards

def my_stats(score_ai, score_human, ai_hand, player_hand):

    print(f"Dealer is showing a... {ai_hand[0]}")
    print(f"DEBUG: Dealer is at {score_ai} score.")
    print(f"Player has...{player_hand}")
    print(f"Player is at {score_human} score.")
    print("What would you like to do?")


def player_options(player_cannot_hit):

    if player_cannot_hit != True:
        print("1. Hit")
        print("2. Stand")
        print("3. Double Down")
        print("4. Split")

    else:
        print("2. Stand")
        print("3. Double Down")
        print("4. Split")

def create_deck_blackjack():
    deck = Deck
    game_deck = deck.create_deck()

    return game_deck

def check_scores_end_game(player_cnt_hit, ai_cnt_hit, ai_score, player_score):

    if player_score > 21:
        print("You bust! The house always wins!")
        return True, False, True
   
    elif ai_score > 21:
        print("Dealer busts! You win!")
        return True, True, False
   
    elif player_score == 21:
        print("Blackjack! You win!")
        return True, True, False
   
    elif ai_score == 21:
        print("Dealer has Blackjack! The house always wins!")
        return True, False, True
    
    elif player_cnt_hit == True and ai_cnt_hit  == True and player_score > ai_score:
        print("Player wins the Hand!")
        return True, True, False
    
    elif player_cnt_hit == True and ai_cnt_hit == True and ai_score > player_score:
        print("Dealer wins the Hand!")
        return True, False, True
    
    return False, False, False

    

# Player hits the desired number of times
def hit_fn(deck, hand):
    
    new_card, deck = Deck.draw_card(deck, 1)
    hand.append(new_card[0])
    return hand, deck
   


    
# Player can no longer hit AI is forced to hit.
def stand_fn(deck, hand):
    new_hand, deck = hit_fn(deck, hand)
    return new_hand, deck


# Player doubles down ANTE for a single card, call hit fn once here and append that to player_score
# Return is 1.25 times for ANTE
def double_down_fn(deck):

    pass

# If two of the same card then we call this function instead
def split(deck):
    pass 

def count_cards_left_in_deck(deck):
        count = 0

        for cards in deck:
            
            for x in cards:
                count += 1

        
        if count == 0:
            print("Deck is empty, creating a new deck!")
            deck = Deck.create_deck()
        else:
            print(f"Cards remaining in deck: {count}")
    
        return deck


def player_options_handler(deck, score_ai, score_human, ai_hand, player_hand, chips):

    inner_game_running = True
    player_cannot_hit = False
    ai_cnt_hit = False

    
    while inner_game_running == True:

        # Clear some junk:
        os.system("clear")
        
        
        deck = count_cards_left_in_deck(deck)
        my_stats(score_ai, score_human, ai_hand, player_hand)
        player_options(player_cannot_hit)



        try:
            player_option = int(input("Please select one of the following options listed: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue
        
        # We need another conditional statement to determine what we should be using for our options on each hand. If we see certain cards we should split accordingly. Hit, stand, double down, and split are always available
        # Do all player moves here.
        # Do all ai moves here
       
        if player_option == 1 and player_cannot_hit != True:
            player_hand, deck = hit_fn(deck, player_hand)
            score_human = find_sum_of_cards(0, player_hand)
        
        elif player_option == 2 or player_cannot_hit == True:
            print("No more cards.")
            player_cannot_hit = True
            
            # Dealer must stand on soft 17 but hit on anything below a 16
            while score_ai <= 16:
                ai_hand, deck = stand_fn(deck, ai_hand)
                score_ai = find_sum_of_cards(0, ai_hand)
            
            if score_ai == 17:
                ai_cnt_hit = True
        
        elif player_option == 3:
            print("Doubling down")
            player_cannot_hit = True
            double_down_fn(chips)

        os.system("clear")
        my_stats(score_ai, score_human, ai_hand, player_hand)


        game_over, player_win, ai_win = check_scores_end_game(player_cannot_hit, ai_cnt_hit, score_ai, score_human)
        if game_over:
            if player_win:
                # Do this
                # Increase chips
                pass
            if ai_win:
                # Do this
                # Decrese chips
                pass
            inner_game_running = False

    return deck, inner_game_running







# Blackjack game loop, player should have 21 to win.
def game_loop():
    game_running = True
    player_chips = 400
    
    while game_running:
        game_deck = create_deck_blackjack()
        
        player_hand, game_deck = Deck.draw_card(game_deck, 2)
        ai_hand, game_deck = Deck.draw_card(game_deck, 2)

        player_hand = list(player_hand)
        ai_hand = list(ai_hand)

        player_score = find_sum_of_cards(0, player_hand)
        ai_score = find_sum_of_cards(0, ai_hand)

        print(player_hand, ai_hand, player_score, ai_score)
        
        game_deck, _ = player_options_handler(game_deck, ai_score, player_score, ai_hand, player_hand, player_chips)
        game_running = continue_op()


            

    


    
    
   