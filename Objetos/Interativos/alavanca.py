from PPlay.sprite import *


class Alavanca:
    sprite = None
    spriteD = None
    spriteE = None
    iniPosX = 0
    iniPosY = 0
    estado = False
    delay = 0

    def __init__(self, posicao, iniPosx, iniPosY):
        self.iniPosX = iniPosx
        self.iniPosY = iniPosY
        if posicao == "N":
            self.spriteE = Sprite("Imagens/Objetos/Interativos/ALAVANCANE.png")
            self.spriteE.x = self.iniPosX
            self.spriteE.y = self.iniPosY
            self.spriteD = Sprite("Imagens/Objetos/Interativos/ALAVANCAND.png")
            self.spriteD.x = self.iniPosX
            self.spriteD.y = self.iniPosY
            self.sprite = self.spriteE
        if posicao == "S":
            self.spriteE = Sprite("Imagens/Objetos/Interativos/ALAVANCASE.png")
            self.spriteE.x = self.iniPosX
            self.spriteE.y = self.iniPosY
            self.spriteD = Sprite("Imagens/Objetos/Interativos/ALAVANCASD.png")
            self.spriteD.x = self.iniPosX
            self.spriteD.y = self.iniPosY
            self.sprite = self.spriteE
        if posicao == "O":
            self.spriteE = Sprite("Imagens/Objetos/Interativos/ALAVANCAOE.png")
            self.spriteE.x = self.iniPosX
            self.spriteE.y = self.iniPosY
            self.spriteD = Sprite("Imagens/Objetos/Interativos/ALAVANCAOD.png")
            self.spriteD.x = self.iniPosX
            self.spriteD.y = self.iniPosY
            self.sprite = self.spriteE
        if posicao == "L":
            self.spriteE = Sprite("Imagens/Objetos/Interativos/ALAVANCALE.png")
            self.spriteE.x = self.iniPosX
            self.spriteE.y = self.iniPosY
            self.spriteD = Sprite("Imagens/Objetos/Interativos/ALAVANCALD.png")
            self.spriteD.x = self.iniPosX
            self.spriteD.y = self.iniPosY
            self.sprite = self.spriteE

    def ativa(self):
        self.estado = True
        if self.sprite == self.spriteD:
            self.sprite = self.spriteE
        else:
            self.sprite = self.spriteD


    def desenha(self):
        self.sprite.draw()
