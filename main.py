#!/usr/bin/env python
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
players = [Player(i) for i in range(constants.NUM_PLAYERS)]
dealer = Dealer(constants.NUM_PLAYERS)
standing_players = []
busted_players = []


def game():
    global players, dealer, standing_players, busted_players
    # get initial bets
    for player in players:
        id = player.id
        print("Player " + str(id) + "'s turn!")
        bet_placed = False
        while not bet_placed:
            bet_placed = dealer.get_bet(players[id])
        


    print("Shuffling " + str(constants.NUM_DECKS) + " Decks!")

    # shuffle the decks together
    masterDeck = Deck(Deck.combineDecks(decks))
    masterDeck.shuffle()





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

    dealer.print_all_hands(players)

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
                player = players[i]
                player.cash += player.bet
                player.bet = 0
                # player is done with the hand
                del players[i]
            print("Stand off! Bet returned to player " + str(i+1) + "\n")

    # if dealer doesn't have blackjack, return 1.5x bet

    elif len(naturals) > 0:
        for i in naturals:
            player = players[i]
            payout = player.bet * 1.5
            player.cash += payout
            player.bet = 0
            del players[i]
            print("Player " + str(i+1) +
                " Blackjack! Paid out 1.5x bet ($" + str(payout) + ")"  "\n")
            standing_players.append(players.pop(i))



    dealer_bust = False

    #loop through players
    
    dealer_hand_value = 0


    while len(players) > 0:
        player = players[0]
        id = player.id
        print("Player " + str(id) + "'s turn")
        dealer.print_hand_value(player)

        response = None
        while response != "stand":
            if dealer.get_hand_value(player.hand) > constants.BLACKJACK:
                print("Player " + str(player.id) + " has gone bust and lost their bet of " + str(player.bet))
                print()
                player.bet = 0
                busted_players.append(players.pop(0))
            
                break
            elif dealer.get_hand_value(player.hand) == constants.BLACKJACK:
                print("Player " + str(player.id) + " has blackjack! ")
                print()
                busted_players.append(players.pop(0))
            
                break
            response = dealer.get_player_action(players[0], masterDeck)
            if response == "stand":
            
                standing_players.append(players.pop(0))
                break

    #check dealer's hand and make final determination
    if dealer.hidden:
        dealer.hand.append(dealer.hidden)
        dealer.hidden = None

            
    while not dealer_bust:
        dealer_hand_value = dealer.get_hand_value(dealer.hand)
        if dealer_hand_value >= 17:
            print("Dealer stands\n")
            break
        else:
            dealer.deal([dealer], masterDeck)
            print("Dealer hits\n")
            dealer.show_hand()
            dealer.print_hand_value(dealer)
            if(dealer.get_hand_value(dealer.hand) > constants.BLACKJACK):
                dealer_bust = True

    if dealer_bust:
        print("The Dealer has gone bust!")
        for player in standing_players:
            player_hand_value = dealer.get_hand_value(player.hand) 
            print("Player " + str(player.id) + " wins "  + str(player.bet) + "." )
            player.cash += player.bet * 2
    elif not dealer_bust:
        for player in standing_players:
            player_hand_value = dealer.get_hand_value(player.hand) 

            if player_hand_value > dealer_hand_value:
                    print("Player " + str(player.id) + " wins $"  + str(player.bet * 2) )
                    player.cash += player.bet * 2
                    player.bet = 0
            elif player_hand_value == dealer_hand_value:
                    print("Player " + str(player.id) + " has the same hand value as the dealer and their bet of "  + str(player.bet) + " is returned." )
                    player.cash += player.bet
                    player.bet = 0
            elif player_hand_value < dealer_hand_value:
                    print("The dealer wins with " + str(dealer_hand_value) + " points.")

    print("Final Reults\n")
    for player in standing_players:
        print("Player " + str(player.id) + ": $" + str(player.cash) )
    for player in busted_players:
        print("Player " + str(player.id) + ": $" + str(player.cash)  )
    for player in players:
        print("Player " + str(player.id) + ": $" + str(player.cash)  )
    
        #pay standing players their bets



game()
