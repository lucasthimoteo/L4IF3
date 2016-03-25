from PPlay.sprite import *

from Util.console import *


class Mensagem:
    console = None
    fundo = None
    spritePersonagem = None
    personagem = None
    ult = 0

    def __init__(self, texto, personagem, console):
        self.console = console
        self.personagem = personagem
        self.fundo = Sprite("Imagens\Cenarios\Mensagem\FUNDOMENSAGEM.jpg")
        self.fundo.x=10
        self.fundo.y=390

        self.spritePersonagem = Sprite("Imagens\Cenarios\Mensagem/" + self.personagem.nome + ".png")
        self.spritePersonagem.x= self.fundo.x + 20
        self.spritePersonagem.y= self.fundo.y + 20

        while self.checaComandos():
            self.fundo.draw()
            self.spritePersonagem.draw()
            self.console.janela.draw_text(texto, self.spritePersonagem.x + self.spritePersonagem.width + 20, self.spritePersonagem.y + 20, 26, Cores.branco, "Arial", True, False)
            self.console.atualizaJanela()

    def checaComandos(self):
        self.console.resetaUlt()

        if self.console.apertou(self.personagem.continuar):
            return False
        return True

