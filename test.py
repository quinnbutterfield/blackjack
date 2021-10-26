from deck import Deck
d = Deck()
d.shuffle()

d1 = Deck()

decks = [d, d1]

combinedDecks = []
for d in decks:
    combinedDecks.append(d.cards)

print(combinedDecks)