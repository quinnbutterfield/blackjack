from card import Card
import constants


class Player:
    def __init__(self, id) -> None:
        self.hand = []
        self.bet = 0
        self.cash = constants.STARTING_CASH
        self.id = id

    def add_card(self, card: Card):
        self.hand.append(card)

    def place_bet(self, bet: float) -> bool:
        if bet > self.cash:
            print("You don't have that much money!")
            return False
        if bet > constants.MAX_BET:
            print("You can only bet $" + str(constants.MAX_BET) + "!")
            return False
        if bet < constants.MIN_BET:
            print("You must bet at least $" + str(constants.MIN_BET) + "!")
            return False
        else:
            self.cash-=bet
            self.bet+=bet
            print("You bet $" + str(bet)+"\n")
            return True

        

    def show_hand(self):
        for card in self.hand:
            card.show()
        
       
