from card import Card
from deck import Deck
from player import Player
from dealer import Dealer
import constants


decks = [Deck() for i in range(constants.NUM_DECKS)]




print(
    """
                                            Welcome To


     /$$$$$$$  /$$        /$$$$$$   /$$$$$$  /$$   /$$    /$$$$$  /$$$$$$   /$$$$$$  /$$   /$$
    | $$__  $$| $$       /$$__  $$ /$$__  $$| $$  /$$/   |__  $$ /$$__  $$ /$$__  $$| $$  /$$/
    | $$  \ $$| $$      | $$  \ $$| $$  \__/| $$ /$$/       | $$| $$  \ $$| $$  \__/| $$ /$$/ 
    | $$$$$$$ | $$      | $$$$$$$$| $$      | $$$$$/        | $$| $$$$$$$$| $$      | $$$$$/  
    | $$__  $$| $$      | $$__  $$| $$      | $$  $$   /$$  | $$| $$__  $$| $$      | $$  $$  
    | $$  \ $$| $$      | $$  | $$| $$    $$| $$\  $$ | $$  | $$| $$  | $$| $$    $$| $$\  $$ 
    | $$$$$$$/| $$$$$$$$| $$  | $$|  $$$$$$/| $$ \  $$|  $$$$$$/| $$  | $$|  $$$$$$/| $$ \  $$
    |_______/ |________/|__/  |__/ \______/ |__/  \__/ \______/ |__/  |__/ \______/ |__/  \__/
                                                                                          
                                                                                          
                                                                                          
    """
)

#instatiate players and dealer
players = [Player() for i in range(constants.NUM_PLAYERS)]
dealer = Dealer()

#get initial bets
for i in range(constants.NUM_PLAYERS):
    print("Player " + str(i+1) + "'s turn!")
    dealer.get_bet(players[i])
   

     
    
print("Shuffling " + str(constants.NUM_DECKS) + " Decks!")

#shuffle the decks together
masterDeck = Deck(Deck.combineDecks(decks))
masterDeck.shuffle()




#deal the initial cards
print("Dealing first card!\n")
dealer.deal(
    players, masterDeck
)

dealer.deal(
    [dealer], masterDeck
)

for i in range(constants.NUM_PLAYERS):
    print("Player " + str(i+1) + "'s hand")
    players[i].show_hand()

print("Dealer's hand\n")
dealer.show_hand()



