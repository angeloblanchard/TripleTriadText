from Card import Card
import random


class CardList:

    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        with open('cards.txt', 'r') as f:
            f.readline()
            for line in f:
                card = line.split(",")
                values = [card[0], card[1], card[2], card[3]]  # Card Values-> Top, Left, Right, Bottom
                self.cards.append(Card(card[4], 1, values))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()
