import ranks


class Card:
    def __init__(self, suit, rank) -> None:
        self.suit = suit
        self.rank = rank

    def show(self):
        print(ranks.RANKS[self.rank] + " of " + self.suit +'\n')
    def get_value(self):
        rank = self.rank
        if rank in ranks.SPECIAL_VALUES.keys():
           return ranks.SPECIAL_VALUES[rank]
        else:
            return rank
        

