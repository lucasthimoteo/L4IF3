from PPlay.sprite import *


class Movel:
    sprite = None
    console = None
    moveu = False
    iniPosX = 0
    iniPosY = 0
    fimPosX = 0
    fimPosY = 0

    def __init__(self, iniPosx, iniPosY, fimPosX, fimPosY, nome, console):
        self.console = console
        self.iniPosX = iniPosx
        self.iniPosY = iniPosY
        self.fimPosX = fimPosX
        self.fimPosY = fimPosY
        self.sprite = Sprite("Imagens/Objetos/Interativos/" + nome + ".png")
        self.sprite.x = self.iniPosX
        self.sprite.y = self.iniPosY

    def empurra(self):
        self.moveu = True
        self.sprite.x = self.fimPosX
        self.sprite.y = self.fimPosY

    def desenha(self):
        self.sprite.draw()
