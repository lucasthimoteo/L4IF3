from PPlay.sprite import *


class Parede:
    sprite = None

    def __init__(self, caminho):
        self.sprite = Sprite(caminho)

    def setXY(self, x, y):
        self.sprite.x = x
        self.sprite.y = y
