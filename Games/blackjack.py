from Games import deck
# Add an option to split the deck
def player_options():
    print("1. Hit")
    print("2. Stand")
    print("3. Double Down")

# This will break on a second loop as it resets sum_of_cards, we need to take an initial value
def find_sum_of_cards(ival, hand):
    sum_of_cards = ival
    
    # Iterate through the list
    # Extract only the first element
    for cards in hand:
        # Extract the first element of Cards in this case the index of "0" should give us 6
        for x in cards:

            my_temp_value = x[0:1]
            
            print(my_temp_value)
            
            if "10" in my_temp_value:
                my_int_temp_value = 10
           
            elif "J" in my_temp_value or "Q" in my_temp_value or "K" in my_temp_value:
                my_int_temp_value = 10
           
            elif my_temp_value[1] == "A":
                # Needs to be some conditional logic for A since this is either 1 or 11 depending. Maybe a function, for now keep this at "11"
                my_int_temp_value = 11
            
            else:
                my_int_temp_value = int(my_temp_value[1])

            my_int_temp_value += sum_of_cards
    
    return sum_of_cards


def game_handle_options():
    pass


# Blackjack game loop, player should have 21 to win.
def game_loop():
    # Deck should draw the first card it sees and assign it to player.
    game_running = True
    
    player_score = 0
    ai_score = 0

    while game_running == True:

        first_draw = True

        while first_draw == True:
            player_hand = deck.draw_card(2)
            ai_hand = deck.draw_card(2)
            first_draw = False

        player_current_score = find_sum_of_cards(player_score, player_hand)
        ai_current_score = find_sum_of_cards(ai_score, ai_hand)

        player_score += player_current_score
        ai_score += ai_current_score

        print(f"Dealer has... {ai_hand}")
        print(f"Dealer is at {ai_score} score")
        print(f"Player has...{player_hand}")
        print(f"Player is at {player_score} score")

        # Handle options down here:


        # Conditions to end the game.