from PPlay.gameimage import *
import string
from Personagens.boneco import *
from cores import *
from Objetos.Interativos.porta import *


class Floor1:
    console = None

    # Estados
    rodando = False
    pausado = False
    dev = True  # developer

    # Predefiniçao das fontes
    tamanho = 24
    spacing = 30
    cor = Cores.preto
    fonte = "Arial"

    # Criacao elementos da janela
    fundo = None
    delta = None
    paredes = []
    objetosInterativos = []
    ult = 0

    # Criação dos personagens
    wolf = None
    gang = None

    def __init__(self, console):
        self.console = console

        # Inicialização dos elementos da janela
        self.fundo = GameImage("Imagens/Cenarios/1FLOOR/FUNDO.jpg")
        self.criaParedes()
        self.criaObjetosInterativos()

        # Inicialização dos personagens
        self.wolf = Boneco("Imagens/Personagens/WOLF.png")
        self.gang = Boneco("Imagens/Personagens/GANG.png")

        self.play()

    def play(self):
        self.rodando = True
        while self.rodando:
            self.delta = self.console.janela.delta_time()
            Constantes.delta = self.delta

            self.checaComandos()

            self.atualizaJanela()

    def criaParedes(self):
        letras = list(string.ascii_uppercase[:14])
        for x in letras:
            self.paredes += [Sprite("Imagens/Cenarios/1FLOOR/" + x + ".png")]
        posicoes = [[50, 80],
                    [50, 90],
                    [310, 90],
                    [50, 570],
                    [310, 520],
                    [480, 520],
                    [60, 370],
                    [240, 370],
                    [320, 260],
                    [460, 260],
                    [480, 260],
                    [490, 360],
                    [690, 360],
                    [740, 90]]
        for i in range(len(self.paredes)):
            self.paredes[i].x = posicoes[i][0]
            self.paredes[i].y = posicoes[i][1]

    def criaObjetosInterativos(self):
        porta = Porta("V",500,500)
        self.objetosInterativos += [porta]

    def checaComandos(self):
        if self.ult > 0:
            self.ult -= 1

        if self.apertou("1"):
            if self.dev:
                self.dev = False
            else:
                self.dev = True

        if self.apertou("ESC"):
            self.pausa()

        if self.apertou("E"):
            for objeto in self.objetosInterativos:
                if self.wolf.colideNorte(objeto.sprite) or self.wolf.colideSul(objeto.sprite) or self.wolf.colideOeste(objeto.sprite) or self.wolf.colideLeste(objeto.sprite):
                    objeto.ativa()

        self.checaMovimento()

    def checaMovimento(self):

        if self.console.teclado.key_pressed("W"):
            b = False
            for parede in self.paredes:
                if self.wolf.colideNorte(parede):
                    b = True
                    break
            for objeto in self.objetosInterativos:
                if self.wolf.colideNorte(objeto.sprite):
                    b = True
                    break
            if not b:
                self.wolf.andaNorte(self.delta)

        if self.console.teclado.key_pressed("S"):
            b = False
            for parede in self.paredes:
                if self.wolf.colideSul(parede):
                    b = True
                    break
            for objeto in self.objetosInterativos:
                if self.wolf.colideSul(objeto.sprite):
                    b = True
                    break
            if not b:
                self.wolf.andaSul(self.delta)

        if self.console.teclado.key_pressed("A"):
            b = False
            for parede in self.paredes:
                if self.wolf.colideOeste(parede):
                    b = True
                    break
            for objeto in self.objetosInterativos:
                if self.wolf.colideOeste(objeto.sprite):
                    b = True
                    break
            if not b:
                self.wolf.andaOeste(self.delta)

        if self.console.teclado.key_pressed("D"):
            b = False
            for parede in self.paredes:
                if self.wolf.colideLeste(parede):
                    b = True
                    break
            for objeto in self.objetosInterativos:
                if self.wolf.colideLeste(objeto.sprite):
                    b = True
                    break
            if not b:
                self.wolf.andaLeste(self.delta)

        if self.console.teclado.key_pressed("UP"):
            b = False
            for parede in self.paredes:
                if self.gang.colideNorte(parede):
                    b = True
                    break
            if not b:
                self.gang.andaNorte(self.delta)

        if self.console.teclado.key_pressed("DOWN"):
            b = False
            for parede in self.paredes:
                if self.gang.colideSul(parede):
                    b = True
                    break
            if not b:
                self.gang.andaSul(self.delta)

        if self.console.teclado.key_pressed("LEFT"):
            b = False
            for parede in self.paredes:
                if self.gang.colideOeste(parede):
                    b = True
                    break
            if not b:
                self.gang.andaOeste(self.delta)

        if self.console.teclado.key_pressed("RIGHT"):
            b = False
            for parede in self.paredes:
                if self.gang.colideLeste(parede):
                    b = True
                    break
            if not b:
                self.gang.andaLeste(self.delta)

    def pausa(self):

        while self.checaComandosPausado():
            self.console.janela.draw_text("Aperte O para sair e ESC para cancelar", self.console.janela.width * 0.2,
                                          self.console.janela.height / 2, 36,
                                          (0, 250, 250), "Arial", False, False)
            self.console.janela.update()

    def desenhaAuxilio(self):
        for x in self.paredes:
            x.draw()
        self.wolf.desenhaAuxilio()
        self.gang.desenhaAuxilio()

    def apertou(self, com):
        if self.console.teclado.key_pressed(com):
            if self.ult == 0:
                self.ult = 2
                return True
            if self.ult > 0:
                self.ult = 2
                return False
        return False

    def atualizaJanela(self):
        self.fundo.draw()
        for objeto in self.objetosInterativos:
            objeto.desenha()
        if self.dev:
            self.desenhaAuxilio()
        self.wolf.desenha()
        self.gang.desenha()
        self.console.janela.update()

    def checaComandosPausado(self):
        if self.ult > 0:
            self.ult -= 1

        if self.apertou("ESC"):
            return False
        if self.apertou("O"):
            self.rodando = False
            return False
        return True
