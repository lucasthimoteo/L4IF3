from Janelas.floor1 import *
from cores import *


class Menu:
    console = None

    # Estados
    rodando = False

    # Predefiniçao das fontes
    tamanho = 24
    spacing = 30
    cor = Cores.preto
    fonte = "Arial"

    # Criação do Fundo
    fundo = None

    # Criação das Opçoes
    opcoes = []
    selecionado = 0
    select = None
    iniPosX = 0
    iniPosY = 0
    ult = 0

    # Inicializa o Menu
    def __init__(self, console):
        self.console = console

        self.fundo = GameImage("Imagens/Cenarios/Menu/FUNDO.jpg")

        self.opcoes = [Sprite("Imagens/Cenarios/Menu/NOVOJOGO.PNG"), Sprite("Imagens/Cenarios/Menu/SAIR.PNG")]
        self.select = Sprite("Imagens/Cenarios/Menu/SELECIONADOR.PNG")
        self.iniPosX = console.janela.width / 2
        self.iniPosY = console.janela.height * 0.6
        for i in range(len(self.opcoes)):
            self.opcoes[i].x = self.iniPosX - self.opcoes[i].width / 2
            self.opcoes[i].y = self.iniPosY - self.opcoes[i].height / 2 + (self.opcoes[i].height + self.spacing) * i
        self.select.x = self.iniPosX - self.select.width / 2
        self.select.y = self.iniPosY - self.select.height / 2

        self.play()

    def play(self):
        self.rodando = True

        while self.rodando:
            self.checaComandos()

            self.atualizaJanela()

    def atualizaJanela(self):

        self.fundo.draw()
        for opcao in self.opcoes:
            opcao.draw()
        self.select.draw()
        self.console.janela.update()

    def apertou(self, com):

        if self.console.teclado.key_pressed(com):
            if self.ult == 0:
                self.ult = 2
                return True
            if self.ult > 0:
                self.ult = 2
                return False
        return False

    def checaComandos(self):
        if self.ult > 0:
            self.ult -= 1

        if self.apertou("UP") and self.selecionado > 0:
            self.select.y -= self.select.height + self.spacing
            self.selecionado -= 1

        if self.apertou("DOWN") and self.selecionado < len(self.opcoes) - 1:
            self.select.y += self.select.height + self.spacing
            self.selecionado += 1

        if self.apertou("ESC"):
            self.rodando = False

        if self.apertou("ENTER"):
            if self.selecionado == 0:
                Floor1(self.console)
            if self.selecionado == 1:
                self.rodando = False
