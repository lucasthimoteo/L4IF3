from PPlay.gameimage import *
import string

from Objetos.Comuns.parede import Parede
from Objetos.Interativos.alavanca import *
from Objetos.Interativos.chave import Chave
from Objetos.Interativos.plataforma import *
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
    paredes = None
    portas = None
    alavancas = None
    plataformas = None
    chaves = None
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
        self.paredes = []
        for x in letras:
            self.paredes += [Parede("Imagens/Cenarios/1FLOOR/" + x + ".png")]
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
            self.paredes[i].setXY(posicoes[i][0], posicoes[i][1])

    def criaObjetosInterativos(self):
        self.portas = []
        porta = Porta("H", 500, 500, False, None)
        portaChave = Porta("V",600,500,True,"123456")
        self.portas += [porta]
        self.portas += [portaChave]
        self.alavancas = []
        alavanca = Alavanca("O", 250, 300)
        self.alavancas += [alavanca]
        self.plataformas = []
        plataforma = Plataforma(350, 250)
        self.plataformas += [plataforma]
        self.chaves = []
        chave = Chave(200, 300, "123456")
        self.chaves += [chave]

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
            for alavanca in self.alavancas:
                if self.wolf.colidiu(alavanca.sprite):
                    alavanca.ativa()

            for porta in self.portas:
                if self.wolf.colidiu(porta.sprite):
                    if not porta.travada:
                        porta.abre()
                    else:
                        if not len(self.wolf.inventario) == 0:
                            for objeto in self.wolf.inventario:
                                if isinstance(objeto,Chave):
                                    if porta.destrava(objeto.codigo):
                                        self.wolf.inventario.remove(objeto)
                                        print("Porta destravada")
                            if porta.travada:
                                print("Porta trancada")
                        else:
                            print("Porta trancada")

            for chave in self.chaves:
                if self.wolf.colidiu(chave.sprite):
                    self.wolf.pega(chave)

        if self.apertou("L"):
            for alavanca in self.alavancas:
                if self.gang.colidiu(alavanca.sprite):
                    alavanca.ativa()

            for porta in self.portas:
                if self.gang.colidiu(porta.sprite):
                    if not porta.travada:
                        porta.abre()
                    else:
                        if not len(self.gang.inventario) == 0:
                            for objeto in self.gang.inventario:
                                if isinstance(objeto,Chave):
                                    if porta.destrava(objeto.codigo):
                                        self.gang.inventario.remove(objeto)
                                        print("Porta destravada")
                            if porta.travada:
                                print("Porta trancada")
                        else:
                            print("Porta trancada")

            for chave in self.chaves:
                if self.gang.colidiu(chave.sprite):
                    self.gang.pega(chave)

        self.checaMovimento()

    def checaMovimento(self):

        for plat in self.plataformas:
            if self.wolf.colidiu(plat.sprite) or self.gang.colidiu(plat.sprite):
                plat.ativa()
            else:
                plat.desativa()

        objetosSolidos = []
        objetosSolidos.clear()
        objetosSolidos += self.paredes
        objetosSolidos += self.portas
        objetosSolidos += self.alavancas

        if self.console.teclado.key_pressed("W"):
            b = False
            for objeto in objetosSolidos:
                if self.wolf.colideNorte(objeto.sprite):
                    b = True
                    break
            if not b:
                self.wolf.andaNorte(self.delta)

        if self.console.teclado.key_pressed("S"):
            b = False
            for objeto in objetosSolidos:
                if self.wolf.colideSul(objeto.sprite):
                    b = True
                    break
            if not b:
                self.wolf.andaSul(self.delta)

        if self.console.teclado.key_pressed("A"):
            b = False
            for objeto in objetosSolidos:
                if self.wolf.colideOeste(objeto.sprite):
                    b = True
                    break
            if not b:
                self.wolf.andaOeste(self.delta)

        if self.console.teclado.key_pressed("D"):
            b = False
            for objeto in objetosSolidos:
                if self.wolf.colideLeste(objeto.sprite):
                    b = True
                    break
            if not b:
                self.wolf.andaLeste(self.delta)

        if self.console.teclado.key_pressed("UP"):
            b = False
            for objeto in objetosSolidos:
                if self.gang.colideNorte(objeto.sprite):
                    b = True
                    break
            if not b:
                self.gang.andaNorte(self.delta)

        if self.console.teclado.key_pressed("DOWN"):
            b = False
            for objeto in objetosSolidos:
                if self.gang.colideSul(objeto.sprite):
                    b = True
                    break
            if not b:
                self.gang.andaSul(self.delta)

        if self.console.teclado.key_pressed("LEFT"):
            b = False
            for objeto in objetosSolidos:
                if self.gang.colideOeste(objeto.sprite):
                    b = True
                    break
            if not b:
                self.gang.andaOeste(self.delta)

        if self.console.teclado.key_pressed("RIGHT"):
            b = False
            for objeto in objetosSolidos:
                if self.gang.colideLeste(objeto.sprite):
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
            x.sprite.draw()
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
        for porta in self.portas:
            porta.desenha()
        for alavanca in self.alavancas:
            alavanca.desenha()
        for plat in self.plataformas:
            plat.desenha()
        for chave in self.chaves:
            chave.desenha()
        if self.dev:
            self.desenhaAuxilio()
        self.wolf.desenha()
        self.wolf.desenhaInventario(20)
        self.gang.desenha()
        self.gang.desenhaInventario(420)
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
