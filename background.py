import pygame

class BackgroundMoving:
    def __init__(self, width, height):
        self.image_bg = pygame.image.load("imagenes/Bg.png")
        self.x = 0
        self.y = 0
        self.dx = 2
        self.dy = 1
        self.bg_width = self.image_bg.get_height()
        self.bg_height = self.image_bg.get_width()

    def update(self, screen):
        self.x -= self.dx
        self.y -= self.dy
        if self.x <= -self.bg_width:
            self.x = 0
        if self.y <= -self.bg_height:
            self.y = 0
        # Dibujar el fondo para crear el efecto de repetición
        screen.blit(self.image_bg, (self.x, self.y))
        screen.blit(self.image_bg, (self.x + self.bg_width, self.y))
        screen.blit(self.image_bg, (self.x, self.y + self.bg_height))
        screen.blit(self.image_bg, (self.x + self.bg_width, self.y + self.bg_height))

        # Cubrir cualquier espacio vacío en la pantalla
        if self.x < 0:
            screen.blit(self.image_bg, (self.x + self.bg_width, self.y))
            screen.blit(self.image_bg, (self.x + self.bg_width, self.y + self.bg_height))
        if self.y < 0:
            screen.blit(self.image_bg, (self.x, self.y + self.bg_height))
            screen.blit(self.image_bg, (self.x + self.bg_width, self.y + self.bg_height))
        if self.x < 0 and self.y < 0:
            screen.blit(self.image_bg, (self.x + self.bg_width, self.y + self.bg_height))