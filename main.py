import pygame
from screenGame import ScreenGame
from screenResult import ScreenResult
# init:
pygame.init()  # <--- recrear el contenido de pantalla
screen = pygame.display.set_mode((800, 600))  # <--- crear una pantalla 800 x 600
pygame.display.set_caption("Galaga Refactorized - Revenge of Bombs")  # título

sg = ScreenGame(screen)
sr = None
show_finish = True

while True:
    sg.clock.tick(20)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sg.set_finished(True)
    sg.screen.fill((0, 0, 0))  # pintar el fondo 0,0,0
    if sg.player.is_alive():
        sg.bg.update(sg.screen)
        sg.playGame()
    if not sg.player.is_alive() and show_finish == True:
        # print('Score final: ' + str(self.score_number))
        sg.set_finished(True)
        show_finish = False
        sr = ScreenResult(800, 600, False, score=sg.get_score())
    if sg.get_score() == 1000:
        sr = ScreenResult(800, 600, True, score=sg.get_score())
        sg.set_finished(True)
        show_finish = False
    if not show_finish:
        sr.draw(screen)
    pygame.display.update()
