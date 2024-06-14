import asyncio
from background import BackgroundMoving
from player import Player
from status import Status
from score import Score
from enemySpawner import EnemySpawner
from collisionDetector import CollisionDetector
import pygame


class ScreenGame:
    def __init__(self, screen):
        # pygame.init()  # <--- recrear el contenido de pantalla
        # screen = pygame.display.set_mode((800, 600))  # <--- crear una pantalla 800 x 600
        # pygame.display.set_caption("Galaga Refactorized - Revenge of Bombs")  # título
        # musica:
        pygame.mixer.init()
        pygame.mixer.music.load("music/bg_music.mp3")
        pygame.mixer.music.play(-1) # <--- loop
        # juego
        self.screen = screen
        self.bg = BackgroundMoving(screen.get_width(), screen.get_height()) # infinito
        self.enemy_spawner = EnemySpawner() # generar los enemigos/bombas
        self.collision_detector = CollisionDetector() # colisionado bomba - misil
        self.player = Player(screen.get_height(), screen.get_width()) # posición
        self.status = Status() # <--- cant. de vidas
        self.score = Score() # <--- puntos
        self.score_number = 0 # <--- 0
        self.finished = False # <--- finalizado
        self.clock = pygame.time.Clock() # <--- iniciamos un reloj para la tasa de refresco

    def playGame(self):
        self.player.update()
        self.player.get_bullet_manager().update()
        self.enemy_spawner.update()
        self.enemy_spawner.draw(self.screen)
        self.player.draw(self.screen)
        self.player.get_bullet_manager().draw(self.screen) # dibujar las balas
        if self.collision_detector.check_collisions(self.enemy_spawner.get_enemies(), self.player.get_bullet_manager().get_bullets()):
            self.score_number += 1
        if self.score_number % 5 == 0:
            self.enemy_spawner.change_difficulty()
        if self.score_number % 15 == 0:
            self.player.get_bullet_manager().increase_type()
        self.status.draw(self.screen, self.player.get_lives())
        self.score.draw(self.screen, self.score_number)

    def get_finished(self):
        return self.finished

    def set_finished(self, val):
        self.player.lives = 0
        self.finished = val

    def get_result(self):
        return self.player.is_alive()

    def get_score(self):
        return self.score_number

    def loop(self):
        while not self.get_finished():
            self.clock.tick(20)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.set_finished(True)
            self.screen.fill((0, 0, 0))# pintar el fondo 0,0,0
            self.bg.update(self.screen)
            self.playGame()
            if not self.player.is_alive():
                # print('Score final: ' + str(self.score_number))
                self.set_finished(True)
            pygame.display.update()
