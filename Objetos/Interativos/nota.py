from PPlay.sprite import *
from random import randint

from Util.constantes import Constantes
from Util.cores import Cores


class Nota:
    nome = None
    sprite = None
    nota = None
    console = None
    codigo = None
    iniPosX = 0
    iniPosY = 0
    delay = 0

    def __init__(self, iniPosx, iniPosY, nome, console):
        self.nome = nome
        self.console = console
        self.iniPosX = iniPosx
        self.iniPosY = iniPosY
        self.sprite = Sprite("Imagens/Objetos/Interativos/" + nome + ".png")
        self.sprite.x = self.iniPosX
        self.sprite.y = self.iniPosY

        self.nota = Sprite("Imagens/Objetos/Interativos/" + nome + "NOTA.png")
        self.nota.x = Constantes.larguraJanela / 2 - self.nota.width / 2
        self.nota.y = Constantes.alturaJanela / 2 - self.nota.height / 2
        if nome == "LIVRO":
            self.codigo = randint(1000, 9999)
            self.delay=Constantes.delayNota

    def atualiza(self):
        if self.delay>0:
            self.delay-=1
        else:
            self.delay = Constantes.delayNota
            self.codigo = randint(1000,9999)


    def exibe(self,continuar):
        while self.checaComandos(continuar):
            self.nota.draw()
            if self.nome == "LIVRO":
                self.console.janela.draw_text(str(self.codigo)[0], self.nota.x+self.nota.width*0.15, self.nota.y+ self.nota.height*0.20, 26, Cores.vermelho, "Arial", True, False)
                self.console.janela.draw_text(str(self.codigo)[1], self.nota.x+self.nota.width*0.65, self.nota.y+ self.nota.height*0.20, 26, Cores.vermelho, "Arial", True, False)
                self.console.janela.draw_text(str(self.codigo)[2], self.nota.x+self.nota.width*0.15, self.nota.y+ self.nota.height*0.45, 26, Cores.vermelho, "Arial", True, False)
                self.console.janela.draw_text(str(self.codigo)[3], self.nota.x+self.nota.width*0.65, self.nota.y+ self.nota.height*0.45, 26, Cores.vermelho, "Arial", True, False)
            self.console.atualizaJanela()

    def desenha(self):
        self.sprite.draw()

    def checaComandos(self,continuar):
        self.console.resetaUlt()

        if self.console.apertou(continuar):
            return False
        return True
