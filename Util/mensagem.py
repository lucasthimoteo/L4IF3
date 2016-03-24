from PPlay.sprite import *

from Util.console import *


class Mensagem:
    console = None
    fundo = None
    narrador = None
    ult = 0

    def __init__(self, texto, narrador,console):
        self.console = console
        self.fundo = Sprite("Imagens\Cenarios\Mensagem\FUNDOMENSAGEM.jpg")
        self.fundo.x=10
        self.fundo.y=390

        self.narrador = Sprite("Imagens\Cenarios\Mensagem/"+ narrador + ".png")
        self.narrador.x=self.fundo.x+20
        self.narrador.y=self.fundo.y+20

        while self.checaComandos():
            self.fundo.draw()
            self.narrador.draw()
            self.console.janela.draw_text(texto, self.narrador.x+self.narrador.width+20, self.narrador.y+20, 26, (255, 255, 255), "Arial", True, False)
            self.console.atualizaJanela()

    def checaComandos(self):
        self.console.resetaUlt()

        if self.console.apertou("SPACE"):
            return False
        return True

