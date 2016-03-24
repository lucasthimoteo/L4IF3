from PPlay.sprite import *



class Plataforma:
    sprite = None
    spriteF = None
    spriteT = None
    iniPosX = 0
    iniPosY = 0
    estado = False
    delay = 0

    def __init__(self, iniPosx, iniPosY):
        self.iniPosX = iniPosx
        self.iniPosY = iniPosY
        self.spriteF = Sprite("Imagens/Objetos/Interativos/PLATAFORMAF.png")
        self.spriteF.x = self.iniPosX
        self.spriteF.y = self.iniPosY
        self.spriteT = Sprite("Imagens/Objetos/Interativos/PLATAFORMAT.png")
        self.spriteT.x = self.iniPosX
        self.spriteT.y = self.iniPosY
        self.sprite = self.spriteF


    def ativa(self):
        self.estado = True
        self.sprite = self.spriteT

    def desativa(self):
        self.estado = False
        self.sprite = self.spriteF

    def desenha(self):
        self.sprite.draw()
