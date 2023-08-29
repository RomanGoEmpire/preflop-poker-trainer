from rfi import Quizz


class TerminalQuizz(Quizz):
    def get_terminal_decision(self):
        decision = input(f'What is the correct play for {self.hand} (r,f)?\n').lower()
        if decision != 'r' and decision != 'f':
            print('Invalid input. Try again.')
            return self.get_terminal_decision()
        return decision

    def terminal_quizz(self):
        self.initialize_quizz()

        print(f'{self.player_position}')
        print(f'Hand: {self.hand}')
        # get the decision of the player
        decision = self.get_terminal_decision()
        self.Trainer.set_inputs(self.hand, self.player_position, decision)
        # the position the player should raise
        if self.Trainer.is_player_decision_correct():
            print('Correct!')
        else:
            print('Incorrect!')
            if self.Trainer.get_position_for_hand() == '-':
                print(f'You never play {self.hand}')
            else:
                print(f'You play {self.hand} at {self.Trainer.get_position_for_hand()}')