from screenGame import ScreenGame


class ScreenManager:
    def __init__(self, screen):
        self.screen = screen # <--- parámetro
        self.screenGame = ScreenGame(self.screen) # <--- juego que necesita de parámetro una pant.

    def playGame(self):
        self.screenGame.loop() # <--- llamar al método loop
