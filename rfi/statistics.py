class Statistics:

    def __init__(self):
        self.games = 0
        self.correct = 0
        self.raised = 0
        self.folded = 0

    def update(self, is_correct, is_fold):
        self.games += 1
        if is_correct:
            self.correct += 1
        if is_fold:
            self.folded += 1
        else:
            self.raised += 1

    def get_accuracy(self):
        return self.correct / self.games * 100

    def get_fold_percentage(self):
        return self.folded / self.games * 100

    def get_raise_percentage(self):
        return self.raised / self.games * 100






