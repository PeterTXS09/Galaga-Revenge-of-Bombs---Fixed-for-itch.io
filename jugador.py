import pygame                    # <--- juegos
from pygame.locals import *      # <--- deteccioón de teclas
from disparo import Disparo      # <--- disparo
from pantalla_ganaste import Ganaste
from pantalla_perdiste import Perdiste

class Jugador(pygame.sprite.Sprite):
    def __init__(self, ypos):
        pygame.sprite.Sprite.__init__(self) # <-- llamada del constructor
        self.ganaste = Ganaste(800, 600)
        self.perdiste = Perdiste(800, 600)
        self.imagen = pygame.image.load('imagenes/nave.png') # imagen
        self.x = 400
        self.y = ypos
        self.disparos = [] # lista vacía
        self.fuente = pygame.font.SysFont('Arial', 25)
        self.vidas = 3
        self.vivo = True
        self.ganar = False
        self.rect = self.imagen.get_rect() # rectángulo de posicion/colision
        self.rect.topleft = (self.x, self.y) # colocarlo en la posicion x,y

    def update(self):
        keys = pygame.key.get_pressed() # <--- obtener la tecla presionada
        if keys[K_RIGHT]: # <--- derecha en 3 unidades
            self.x += 10
        elif keys[K_LEFT]: # <--- izquierda en 3 unidades
            self.x -= 10 # hasta ahora solo actualizamos el valor de X
        if self.x < 0 or self.x > 800 - 60:
            self.x = 400
            self.vidas -= 1

        if self.vidas <= 0:
            self.vivo = False

        # mover la imagen para que se mueva a X, Y
        self.rect.topleft = (self.x, self.y)

        if keys[K_SPACE]:
            # agregar un elemento a la lista
            self.disparos.append(Disparo(self.x + self.imagen.get_width() // 2, self.y, 20))

    def draw(self, screen):
        if self.vivo:
            screen.blit(self.imagen, [self.x, self.y, self.imagen.get_width(), self.imagen.get_height()])
            self.vidas_texto = self.fuente.render('Vidas: ' + str(self.vidas), True, (255, 100, 100))
            screen.blit(self.vidas_texto, (0, 0))

            for d in self.disparos:
                d.draw(screen)
        elif self.vivo == False and self.ganar == False:
            self.perdiste.draw(screen)
            # self.texto = (self.fuente.render('Game Over',True,(255, 100, 100)))
            # screen.blit(self.texto, (400, 300))
        if self.ganar:
            # screen.fill((0, 0, 0))
            self.ganaste.draw(screen)
            # self.texto = (self.fuente.render('You Win', True, (0, 255, 0)))
            # screen.blit(self.texto, (400, 300))

