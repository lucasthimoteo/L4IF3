from PPlay.sprite import *



class Chave:
    sprite = None
    iniPosX = 0
    iniPosY = 0
    estado = False
    codigo = None
    delay = 0

    def __init__(self, iniPosx, iniPosY,codigo):
        self.iniPosX = iniPosx
        self.iniPosY = iniPosY
        self.sprite = Sprite("Imagens/Objetos/Interativos/CHAVE.png")
        self.sprite.x = self.iniPosX
        self.sprite.y = self.iniPosY
        self.codigo = codigo


    def pegado(self):
        self.estado = True


    def desenha(self):
        if not self.estado:
            self.sprite.draw()
