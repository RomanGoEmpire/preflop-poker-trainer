import random

from rfi import Trainer, Deck, ORDER, Statistics


def get_random_position():
    return random.choice(ORDER[:-1])


class Quizz:
    def __init__(self):
        self.Trainer = Trainer()
        self.statistics = Statistics()
        self.deck = Deck()
        self.hand = None
        self.player_position = None


    def initialize_quizz(self):
        self.hand = self.deck.deal()
        self.player_position = get_random_position()
