from card import Card
from constants import MAX_BET, MIN_BET
from player import Player
from deck import Deck


class Dealer(Player):
    def __init__(self) -> None:
        super().__init__()
        self.hidden:Card  = None
        
    def get_response(self):
        while True:
            try:
                response = float(input("Please place your bet. Minimum $" +
                                 str(MIN_BET) + ", maximum $ " + str(MAX_BET) + "\n"))
                return response
                
            except:
                print("Please enter an integer or decimal")
        
    def get_bet(self, player: Player):
        print()
        has_bet = False
        while not has_bet:
            response = self.get_response()
            has_bet = player.place_bet(response)

    def deal(self, players: "list[Player]", deck: Deck, hidden=False):
        if hidden:
            self.hidden += deck.draw()
        else:
            for player in players:
                player.add_card(deck.draw())
