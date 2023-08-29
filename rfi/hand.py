from rfi import RANKS


class Hand:

    def __init__(self, *cards):
        self.cards = cards
        # sort cards by rank
        self.cards = sorted(self.cards, key=lambda x: RANKS.index(x.value))
        self.suited = self.check_suit()
        self.values = self.get_values()

    def check_suit(self):
        return self.cards[0].suit == self.cards[1].suit

    def get_values(self):
        return [card.value for card in self.cards]

    def __repr__(self):
        return f'{self.cards[0]} {self.cards[1]}'
