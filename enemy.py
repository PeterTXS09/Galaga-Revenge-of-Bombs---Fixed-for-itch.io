import pygame
import random


class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, dy):
        super().__init__()
        __slots__ = ('x', 'y', 'dx', 'dy')
        self.x = x
        self.y = -60
        self.dx = 0
        # self.dy = 0.1
        self.dy = dy
        self.imagen = None
        self.sprite_size = 32
        self.rect = None

    def update(self):
        self.x += self.dx
        self.y += self.dy
        if self.y >= 600:
            self.kill()
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.imagen, [self.x, self.y, self.imagen.get_width(), self.imagen.get_height()])