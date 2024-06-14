import pygame
from screenManager import ScreenManager

pygame.init()  # <--- recrear el contenido de pantalla
screen = pygame.display.set_mode((800, 600))  # <--- crear una pantalla 800 x 600
pygame.display.set_caption("Galaga Refactorized - Revenge of Bombs")  # título

screenManager = ScreenManager(screen)  # un objeto que recibe de parámetro screen
screenManager.playGame()  # método
