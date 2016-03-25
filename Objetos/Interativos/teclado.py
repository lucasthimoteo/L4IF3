from PPlay.sprite import *

from Util.console import *


class Teclado:
    sprite = None
    console = None
    fundo = None
    insert = None
    novoCodigo = None
    codigo = None
    selecionador = None
    selecionado = None
    travado = True
    rodando = None

    def __init__(self, x, y, console):
        self.console = console

        self.codigo = ""

        self.sprite = Sprite("Imagens\Objetos\Interativos/COFRE.png")
        self.sprite.x = x
        self.sprite.y = y

        self.iniPosX = console.janela.width / 2
        self.iniPosY = console.janela.height / 2

        self.fundo = Sprite("Imagens\Objetos\Interativos\TECLADO/FUNDOTECLADO.png")
        self.fundo.x = self.iniPosX - self.fundo.width / 2
        self.fundo.y = self.iniPosY - self.fundo.height / 2

        self.insert = [0, 0, 0, 0]

        self.selecionador = Sprite("Imagens\Objetos\Interativos\TECLADO/SELECIONADOR.png")
        self.selecionador.x = self.fundo.x + 5
        self.selecionador.y = self.fundo.y + 5

        self.selecionado = 0

    def destrava(self, codigo, personagem):
        self.codigo = codigo
        self.novoCodigo = ""
        self.rodando = True
        while self.rodando:
            self.checaComandos(personagem)
            self.novoCodigo = ""
            for i in self.insert:
                self.novoCodigo += str(i)
            tecla1 = Sprite("Imagens/Objetos/Interativos/TECLADO/" + str(self.insert[0]) + ".png")
            tecla1.set_position(self.fundo.x + 5, self.fundo.y + 5)
            tecla2 = Sprite("Imagens/Objetos/Interativos/TECLADO/" + str(self.insert[1]) + ".png")
            tecla2.set_position(self.fundo.x + 105, self.fundo.y + 5)
            tecla3 = Sprite("Imagens/Objetos/Interativos/TECLADO/" + str(self.insert[2]) + ".png")
            tecla3.set_position(self.fundo.x + 205, self.fundo.y + 5)
            tecla4 = Sprite("Imagens/Objetos/Interativos/TECLADO/" + str(self.insert[3]) + ".png")
            tecla4.set_position(self.fundo.x + 305, self.fundo.y + 5)
            self.fundo.draw()
            tecla1.draw()
            tecla2.draw()
            tecla3.draw()
            tecla4.draw()
            self.selecionador.draw()
            self.console.atualizaJanela()
            if str(self.novoCodigo) == str(self.codigo):
                self.travado = False
                self.rodando = False

    def checaComandos(self,personagem):
        self.console.resetaUlt()

        if self.console.apertou(personagem.continuar):
            self.travado = True
            self.rodando = False
        if self.console.apertou(personagem.up) and self.insert[self.selecionado] < 9:
            self.insert[self.selecionado] += 1
        if self.console.apertou(personagem.down) and self.insert[self.selecionado] > 0:
            self.insert[self.selecionado] -= 1
        if self.console.apertou(personagem.left) and self.selecionado > 0:
            self.selecionado -= 1
            self.selecionador.x -= 100
        if self.console.apertou(personagem.right) and self.selecionado < 3:
            self.selecionado += 1
            self.selecionador.x += 100

    def desenha(self):
        self.sprite.draw()
