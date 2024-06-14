import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        __slots__ = ['x', 'y', 'speed'] # ---> fixed size array
        super().__init__()
        self.image = None
        self.x = x
        self.y = y
        self.speed = speed
        self.rect = None

    def update(self):
        self.y -= self.speed
        if self.y <= 0:
            self.remove()
            self.kill()
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image, [self.x, self.y, self.image.get_width(), self.image.get_height()])


