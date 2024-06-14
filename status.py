import pygame


class Status:
    def __init__(self):
        self.font = pygame.font.SysFont('Roboto', 20)
        self.life_text = None

    def draw(self, screen, lifes):
        self.life_text = self.font.render('Vidas: ' + str(lifes), True, (255, 100, 100))
        screen.blit(self.life_text, (0, 0))
