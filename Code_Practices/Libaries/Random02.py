# using shuffle to randomly shuffle a list, and output that list.

from random import shuffle

cards = ["jack", "queen", "king"]
shuffle(cards)
for card in cards:
    print(card)