import pygame.image
from bullet import Bullet


class BulletType(Bullet):
    def __init__(self, x, y, b_type):
        self.name = b_type
        self.y_speed = 2 * b_type
        if self.name <= 9:
            self.name = '0' + str(self.name) + '.png'
        else:
            self.name = str(self.name) + '.png'
        super().__init__(x, y, self.y_speed)
        self.image = pygame.image.load('imagenes/B' + self.name)
        self.rect = self.image.get_rect()
