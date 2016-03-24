from PPlay.sprite import *


class Porta:
    sprite = None
    spriteV = None
    spriteH = None
    iniPosX = 0
    iniPosY = 0
    codigo = None
    travada = None
    aberta = False
    delay = 0

    def __init__(self, orientacao, iniPosx, iniPosY, travada, codigo):
        self.travada = travada
        self.codigo = codigo
        self.iniPosX = iniPosx
        self.iniPosY = iniPosY
        self.spriteV = Sprite("Imagens/Objetos/Interativos/PORTAV.png")
        self.spriteV.x = self.iniPosX
        self.spriteV.y = self.iniPosY
        self.spriteH = Sprite("Imagens/Objetos/Interativos/PORTAH.png")
        self.spriteH.x = self.iniPosX
        self.spriteH.y = self.iniPosY
        if orientacao == "V":
            self.sprite = self.spriteV
        if orientacao == "H":
            self.sprite = self.spriteH

    def abre(self):
        self.aberta = True
        if self.sprite == self.spriteH:
            self.sprite = self.spriteV
        else:
            self.sprite = self.spriteH

    def destrava(self, codigo):
        if self.codigo == codigo:
            self.travada = False
            return True
        else:
            return False

    def desenha(self):
        self.sprite.draw()
