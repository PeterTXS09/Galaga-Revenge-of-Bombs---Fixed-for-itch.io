import pygame


class Score:
    def __init__(self):
        self.font = pygame.font.SysFont('Roboto', 20)
        self.score_text = None

    def draw(self, screen, sc):
        self.score_text = self.font.render('Score: ' + str(sc), True, (255, 100, 100))
        screen.blit(self.score_text, (0, 580))
