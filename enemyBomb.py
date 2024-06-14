from enemy import Enemy
import pygame
import random


class EnemyBomb(Enemy):
    def __init__(self, x, dy):
        __slots__ = ['name', 'dir']
        super().__init__(x, dy)
        self.name = str(random.randint(1, 5))
        self.dir = 'imagenes/M' + self.name + '.png'
        self.imagen = pygame.image.load(self.dir)
        self.rect = self.imagen.get_rect()
        self.rect.topleft = (self.x, self.y)
