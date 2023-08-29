import random

from rfi import RANKS, Card, Hand


class Deck:
    def __init__(self):
        self.cards = self.create_deck()

    def create_deck(self):
        cards = []
        for suit in ['s', 'h', 'd', 'c']:
            for value in RANKS:
                cards.append(Card(suit, value))
        random.shuffle(cards)
        return cards

    def __str__(self):
        return f'{self.cards}'

    def deal(self):
        if len(self.cards) < 2:
            self.cards = self.create_deck()
        return Hand(self.cards.pop(), self.cards.pop())
