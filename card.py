from ranks import ranks


class Card:
    def __init__(self, suit, rank) -> None:
        self.suit = suit
        self.rank = rank

    def show(self):
        print(ranks[self.rank] + " of " + self.suit +'\n')
