from rfi import RANKS, ORDER


def load_chart():
    with open('tables\easy_preflop_chart.csv') as f:
        chart = []
        for line in f:
            chart.append(line.strip().split(','))
    return chart


class Trainer:

    def __init__(self):
        self.decision = None
        self.player_position = None
        self.hand = None
        self.chart = load_chart()

    def set_inputs(self, hand, player_position, decision):
        self.hand = hand
        self.player_position = player_position
        self.decision = decision

    def _get_row_col(self):
        row, col = RANKS.index(self.hand.values[0]), RANKS.index(self.hand.values[1])
        if not self.hand.suited:
            row, col = col, row
        return row + 1, col + 1

    def get_position_for_hand(self):
        row, col = self._get_row_col()
        return self.chart[row][col]

    def is_player_decision_correct(self):
        index_player = ORDER.index(self.player_position)
        index_chart = ORDER.index(self.get_position_for_hand())
        player_fold_chart_fold = self.decision == 'f' and (index_chart == 5 or index_player < index_chart)
        player_raise_chart_raise = self.decision == 'r' and index_chart != 5 and index_player >= index_chart
        return player_fold_chart_fold or player_raise_chart_raise

    def print_chart(self):
        for row in self.chart:
            print(''.join([f'{cell:<4}' for cell in row]))
