
from card import Card
from constants import BLACKJACK, COMMANDS, MAX_BET, MIN_BET
from player import Player
from deck import Deck
from ranks import RANKS, SPECIAL_VALUES


class Dealer(Player):
    def __init__(self, id) -> None:
        super().__init__(id)
        self.hidden: Card = None

    def get_response(self, prompt, error):
        while True:
            try:
                response = prompt
                return
            except:
                print(error)

    def get_bet(self, player: Player):
        while True:
            try:
                response = float(input("Please place your bet. Minimum $" +
                                       str(MIN_BET) + ", maximum $ " + str(MAX_BET) + "\n"))
                break
            except:
                print("Please enter an integer or decimal")

        return player.place_bet(response)

    def get_player_action(self, player: Player, deck: Deck):
        while True:
            try:
                response = self.parse_command(
                    input("Would you like to hit or stand? [h / s] ").lower()
                )
                break
            except:
                print("Please enter a valid command")
        match response:
            case "hit":
                self.deal([player], deck)
                player.show_hand()
                self.print_hand_value(player)
            case "stand":
                print("Player "  + str(player.id) + " passes.\n")
            case "hand":
                player.show_hand()
                self.print_hand_value(player)
            case "cash":
                print("You have $" + str(player.cash) + " in your wallet")
            case "quit":
                raise SystemExit
        return response

    def parse_command(self, command):
        if command in COMMANDS.keys():
            return COMMANDS[command]
        else:
            raise Exception

    def print_hand(self, player_index, players):
        print("******************************\n")
        print()
        print("Player " + str(player_index+1) + "'s hand")
        print()
        players[player_index].show_hand()
        print()

    
    def print_hand_value(self, player):
        print("hand value: ", self.get_hand_value(player.hand), "\n")


    def print_all_hands(self, players):
        for i in range(len(players)):
            self.print_hand(i, players)
            self.print_hand_value(players[i])
        print("******************************\n")
        print("Dealer's hand\n")
        self.show_hand()
        self.print_hand_value(self)

    def show_hand(self):
        if self.hidden:
            print("Face down card\n")

        return super().show_hand()

    def deal(self, players: "list[Player]", deck: Deck, hidden=False):
        if hidden:
            self.hidden = deck.draw()
        else:
            for player in players:
                player.add_card(deck.draw())


    #Main function for determining the value of a hand. 
    #Aces are initially asummed to be low, and the highest possible value 
    #of the hand without going bust is computed
    def get_hand_value(self, hand: "list[Card]"):
        values = map(Card.get_value, hand)
        total_non_ace_value = 0
        num_aces = 0
        for card in hand:
            if RANKS[card.rank] == "Ace":
                num_aces += 1
            else:
                total_non_ace_value += card.get_value()
        # min value if each ace is 1
        min_value = total_non_ace_value + num_aces

        if min_value > BLACKJACK:
            return min_value

        max_without_bust = min_value
        for ace in range(num_aces):
            if max_without_bust + 10 <= BLACKJACK:
                max_without_bust += 10
            else:
                break

        return max_without_bust

        # values = []
        # for card in hand:
        #     values.append(card.get_value())
        # return values
