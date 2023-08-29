import pygame

from rfi import Quizz


class VisualQuizz(Quizz):

    def __init__(self):
        super().__init__()
        self.window_size = (1200, 700)
        self.card_width = 300

    def start_quizz(self):
        # pygame setup
        pygame.init()
        screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption('Poker Trainer')
        font = pygame.font.SysFont('Arial', 40)
        clock = pygame.time.Clock()
        running = True

        background_color = (0, 0, 0)
        cards_offset = int(self.window_size[0] / 2 + - self.card_width), int(self.window_size[1] * 0.1)
        # logic
        self.initialize_quizz()
        card_images = self.get_card_images()
        has_decided = False
        decision = None

        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:
                running = False
            # fill background
            screen.fill(background_color)
            # show cards
            for i, card_image in enumerate(card_images):
                screen.blit(card_image, (cards_offset[0] + i * (self.card_width + 10), cards_offset[1]))
            # show position
            position_text = font.render(f'{self.player_position}', True, (255, 255, 255))
            screen.blit(position_text, (20, 20))
            # if key is pressed change background color
            if not has_decided:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_f]:
                    decision = 'f'
                    has_decided = True
                elif keys[pygame.K_r]:
                    decision = 'r'
                    has_decided = True
            if has_decided:
                self.Trainer.set_inputs(self.hand, self.player_position, decision)
                if self.Trainer.is_player_decision_correct():
                    background_color = (56,102,65)
                else:
                    background_color = (188,71,73)
            # if spacebar is pressed get new hand
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and has_decided:
                card_images, has_decided, decision, background_color = self.reset_visual_quizz()

            pygame.display.flip()
            clock.tick(30)  # limits FPS to 30
        pygame.quit()

    def _update_image(self, image, width):
        size = image.get_size()
        scale = width / size[0]
        image = pygame.transform.scale(image, (width, int(size[1] * scale)))
        return image

    def get_card_images(self):
        card_images = []
        for card in self.hand.cards:
            card_file_name = f'{card.value}_{card.suit}.svg'
            card_image = pygame.image.load(f'images\\cards\\{card_file_name}')
            card_image = self._update_image(card_image, self.card_width)
            card_images.append(card_image)
        return card_images

    def reset_visual_quizz(self):
        self.initialize_quizz()
        card_images = self.get_card_images()
        has_decided = False
        decision = None
        background_color = (0, 0, 0)
        return card_images, has_decided, decision, background_color
