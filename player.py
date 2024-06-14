import pygame
from pygame.locals import  K_RIGHT, K_LEFT, K_UP, K_DOWN, K_SPACE
from bulletManager import BulletManager

class Player(pygame.sprite.Sprite):
    def __init__(self,  height_screen, width_screen = 800):
        pygame.sprite.Sprite.__init__(self)  # <-- llamada del constructor
        self.image = pygame.image.load('imagenes/rocket.png')  # imagen
        SCALE_FACTOR = 0.5
        self.image = pygame.transform.scale_by(self.image, SCALE_FACTOR)
        self.width_screen_limit = width_screen - self.image.get_width()
        self.height_screen_limit = height_screen - self.image.get_height()
        self.default_x = width_screen // 2
        self.default_y = height_screen - 100
        self.bullet_manager = BulletManager()
        self.x = self.default_x
        self.y = self.default_y
        self.lives = 3
        self.rect = self.image.get_rect()  # rectángulo de posicion/colision
        self.rect.topleft = (self.x, self.y)  # colocarlo en la posicion x,y

    def update(self):
        if self.is_alive():
            keys = pygame.key.get_pressed()
            if keys[K_SPACE]:
                self.shoot()
            if keys[K_RIGHT]:
                self.x += 10
            elif keys[K_LEFT]:
                self.x -= 10
            if keys[K_UP]:
                self. y -= 10
            elif keys[K_DOWN]:
                self.y += 10
            if self.x < 0 or self.x > self.width_screen_limit:
                self.x = self.default_x
                self.lives -= 1
            if self.y < 0 or self.y > self.height_screen_limit:
                self.y = self.default_y
                self.lives -= 1
            self.rect.topleft = (self.x, self.y)

    def get_lives(self):
        return self.lives
    def is_alive(self):
        return self.lives != 0

    def draw(self, screen):
        if self.is_alive():
            screen.blit(self.image, [self.x, self.y, self.image.get_width(), self.image.get_height()])

    def shoot(self):
        self.bullet_manager.spawn_bullet(self.x + 15, self.y - 50)

    def get_bullet_manager(self):
        return self.bullet_manager
