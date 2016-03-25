from PPlay.sprite import *

from Util.constantes import Constantes


class Nota:
    sprite = None
    nota = None
    console = None
    iniPosX = 0
    iniPosY = 0
    delay = 0

    def __init__(self, iniPosx, iniPosY, nome, console):
        self.console = console
        self.iniPosX = iniPosx
        self.iniPosY = iniPosY
        self.sprite = Sprite("Imagens/Objetos/Interativos/" + nome + ".png")
        self.sprite.x = self.iniPosX
        self.sprite.y = self.iniPosY

        self.nota = Sprite("Imagens/Objetos/Interativos/" + nome + "NOTA.png")
        self.nota.x=Constantes.larguraJanela/2-self.nota.width/2
        self.nota.y=Constantes.alturaJanela/2-self.nota.height/2

    def exibe(self):
        while self.checaComandos():
            self.nota.draw()
            self.console.atualizaJanela()

    def desenha(self):
        self.sprite.draw()

    def checaComandos(self):
        self.console.resetaUlt()

        if self.console.apertou("SPACE"):
            return False
        return True
