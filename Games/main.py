import blackjack
from deck import Deck

def main():
  blackjack.game_loop()



if __name__ == '__main__':
 my_deck = Deck.create_deck()
 
 my_shuffled_deck = Deck.shuffle_deck(my_deck)
 #main()


