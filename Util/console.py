from PPlay.window import *
from Util.cores import *
from Util.constantes import *

class Console:
    janela = None
    teclado = None
    mouse = None
    ult = 0

    def __init__(self, largura, altura):
        self.janela = Window(largura, altura)
        self.teclado = self.janela.get_keyboard()


    def apertou(self,botao):
        if self.teclado.key_pressed(botao):
            if self.ult == 0:
                self.ult = 2
                return True
            if self.ult > 0:
                self.ult = 2
                return False
        return False

    def resetaUlt(self):
        if self.ult > 0:
            self.ult -= 1

    def pressionou(self, botao):
        return self.teclado.key_pressed(botao)

    def desenha(self, objeto):
        objeto.draw()

    def atualizaJanela(self):
        self.janela.update()

    def delta(self):
        return self.janela.delta_time()