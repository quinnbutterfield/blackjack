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

# instatiate players and dealer
players = [Player() for i in range(constants.NUM_PLAYERS)]
dealer = Dealer()

# get initial bets
for i in range(constants.NUM_PLAYERS):
    print("Player " + str(i+1) + "'s turn!")
    bet_placed = False
    while not bet_placed:
        bet_placed = dealer.get_bet(players[i])


print("Shuffling " + str(constants.NUM_DECKS) + " Decks!")

# shuffle the decks together
masterDeck = Deck(Deck.combineDecks(decks))
masterDeck.shuffle()


def print_hand(player_index):
    print("******************************\n")
    print()
    print("Player " + str(player_index+1) + "'s hand")
    print()
    players[player_index].show_hand()
    print()


def print_all_hands():
    for i in range(len(players)):
        print_hand(i)
        dealer.print_hand_value(players[i])
    print("******************************\n")
    print("Dealer's hand\n")
    dealer.show_hand()
    dealer.print_hand_value(dealer)


# deal the initial cards
print("Dealing first card!\n")
dealer.deal(
    players, masterDeck
)

dealer.deal(
    [dealer], masterDeck
)


# deal more cards
print("Dealing second card!\n")
dealer.deal(
    players, masterDeck
)
dealer.deal(
    [dealer], masterDeck, hidden=True
)

print_all_hands()

# calculate hand values
hand_values = list(map(lambda p: dealer.get_hand_value(p.hand), players))

# check for naturals

naturals = [i for i, value in enumerate(
    hand_values) if value == constants.BLACKJACK]

# check dealer's hand if at least one person was dealt blackjack
# and their face up card is a 10 or A

dealer_visible_value = dealer.get_hand_value(dealer.hand)


if len(naturals) > 0 & dealer_visible_value == (10 or 11):
    if dealer.hidden.get_value() + dealer_visible_value == constants.BLACKJACK:
        dealer.hand.append(dealer.hidden)
        dealer.hidden = None
        dealer.show_hand()
        for i in naturals:
            p = players[i]
            p.cash += p.bet
            p.bet = 0
            # player is done with the hand
            del players[i]
        print("Stand off! Bet returned to player " + str(i+1) + "\n")
# if dealer doesn't have blackjack, return 1.5x bet
elif len(naturals) > 0:
    for i in naturals:
        p = players[i]
        payout = p.bet * 1.5
        p.cash += payout
        p.bet = 0
        del players[i]
        print("Player " + str(i+1) +
              " Blackjack! Paid out 1.5x bet ($" + str(payout) + ")"  "\n")

print(players)
print(hand_values)

print(naturals)


#loop through players

i = 0
while len(players) > 0:
    print("i is ", i)
    print("Player " + str(i+1) + "'s turn")
    player = players[0]
    response = None
    while response != "stand":
        if dealer.get_hand_value(player.hand) > 21:
            print("Player " + str(i+1) + " has gone bust and lost their bet of " + str(player.bet))
            player.bet = 0
            del players[0]
            i+=1
            break
        response = dealer.get_player_action(players[0], masterDeck)
        if response == "stand":
             i+=1
             del players[0]
             break

