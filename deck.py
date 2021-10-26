
from card import Card
from random import shuffle

suits = ["Hearts", "Diamonds", "Spades", "Clubs"]


class Deck:
    def __init__(self, deck=None):
        self.cards = []
        if deck is None:
            self.create()
        else:
            self.cards = deck



    def show(self):
        for card in self.cards:
            card.show()

    def create(self):
        for suit in suits:
            for i in range(1, 14):
                self.cards.append(Card(suit, i))

    def shuffle(self):
        shuffle(
            self.cards
        )
    #remove the top card of the deck
    #dealing to player is handled in player class
    #deck acts as a stack, so the first card in the list is removed first
    def draw(self):
        return self.cards.pop(0)

    def combineDecks(decks):
        new_cards = []
        for d in decks:
            new_cards.extend(d.cards)
        return new_cards

    # def combineDecks(decks: list[Deck]):
    #     []

        # for suit in suits:
        #     print("f")
