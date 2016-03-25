from Janelas.floor1 import *
from Objetos.Comuns.parede import Parede
from Objetos.Interativos.chave import Chave
from Objetos.Interativos.movel import Movel
from Objetos.Interativos.nota import Nota
from Objetos.Interativos.porta import *
from Personagens.boneco import *
from Util.cores import *
from Util.mensagem import Mensagem


class Floor2:
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
    notas = None
    moveis = None
    ult = 0

    # Criação dos personagens
    wolf = None
    gang = None

    def __init__(self, console, wolf, gang):
        self.console = console

        # Inicialização dos elementos da janela
        self.fundo = GameImage("Imagens/Cenarios/1FLOOR/FUNDO.jpg")

        self.criaParedes()
        self.criaObjetosInterativos()

        # Inicialização dos personagens
        self.wolf = wolf
        self.gang = gang

    def play(self):
        self.rodando = True
        while self.rodando:
            Constantes.delta = self.console.delta()

            self.checaComandos()

            self.atualizaJanela()

    def criaParedes(self):
        letras = list(string.ascii_uppercase[:23])
        self.paredes = []
        for x in letras:
            self.paredes += [Parede("Imagens\Objetos\Paredes\FLOOR1/" + x + ".png")]
        posicoes = [[50, 50],
                    [50, 50],
                    [50, 200],
                    [50, 300],
                    [50, 500],
                    [125, 200],
                    [150, 200],
                    [225, 390],
                    [250, 200],
                    [250, 500],
                    [250, 550],
                    [325, 200],
                    [390, 200],
                    [400, 200],
                    [400, 275],
                    [400, 300],
                    [400, 500],
                    [400, 500],
                    [350, 550],
                    [500, 200],
                    [750, 50],
                    [650, 300],
                    [650, 300]]
        for i in range(len(self.paredes)):
            self.paredes[i].setXY(posicoes[i][0], posicoes[i][1])

    def criaObjetosInterativos(self):

        self.portas = []
        portaSalaDeVisita = Porta("V", 250, 450, False, None)
        portaSalaDeEstar = Porta("V", 400, 450, False, None)
        portaBanheiro = Porta("V", 400, 225, False, None)
        portaLavanderia = Porta("H", 75, 200, False, None)
        portaArmazem = Porta("H", 175, 200, False, None)
        portaCozinha = Porta("H", 340, 200, False, None)
        portaSalaDeJantar = Porta("H", 600, 300, False, None)
        self.portas += [portaSalaDeVisita, portaSalaDeEstar, portaBanheiro, portaLavanderia, portaArmazem, portaCozinha,
                        portaSalaDeJantar]

        self.moveis = []
        movelEscondido = Movel(450, 350, 500, 350, "MOVEL", self.console)
        self.moveis += [movelEscondido]

        self.notas = []
        notaLivro = Nota(400, 100, "LIVRO", self.console)
        self.notas += [notaLivro]

        self.escada = Sprite("Imagens\Objetos\Interativos\ESCADA.png")
        self.escada.x = 260
        self.escada.y = 350

    def checaComandos(self):
        self.console.resetaUlt()

        if self.console.apertou("1"):
            if self.dev:
                self.dev = False
            else:
                self.dev = True

        if self.console.apertou("ESC"):
            self.pausa()

        self.checaInteratividade()

        self.checaMovimento()

    def checaMovimento(self):

        objetosSolidos = []
        objetosSolidos.clear()
        objetosSolidos += self.paredes
        objetosSolidos += self.portas
        objetosSolidos += self.moveis

        if self.console.pressionou("W"):
            b = False
            for objeto in objetosSolidos:
                if self.wolf.colideNorte(objeto.sprite):
                    b = True
                    break
            if not b:
                self.wolf.andaNorte()

        if self.console.pressionou("S"):
            b = False
            for objeto in objetosSolidos:
                if self.wolf.colideSul(objeto.sprite):
                    b = True
                    break
            if not b:
                self.wolf.andaSul()

        if self.console.pressionou("A"):
            b = False
            for objeto in objetosSolidos:
                if self.wolf.colideOeste(objeto.sprite):
                    b = True
                    break
            if not b:
                self.wolf.andaOeste()

        if self.console.pressionou("D"):
            b = False
            for objeto in objetosSolidos:
                if self.wolf.colideLeste(objeto.sprite):
                    b = True
                    break
            if not b:
                self.wolf.andaLeste()

        if self.console.pressionou("UP"):
            b = False
            for objeto in objetosSolidos:
                if self.gang.colideNorte(objeto.sprite):
                    b = True
                    break
            if not b:
                self.gang.andaNorte()

        if self.console.pressionou("DOWN"):
            b = False
            for objeto in objetosSolidos:
                if self.gang.colideSul(objeto.sprite):
                    b = True
                    break
            if not b:
                self.gang.andaSul()

        if self.console.pressionou("LEFT"):
            b = False
            for objeto in objetosSolidos:
                if self.gang.colideOeste(objeto.sprite):
                    b = True
                    break
            if not b:
                self.gang.andaOeste()

        if self.console.pressionou("RIGHT"):
            b = False
            for objeto in objetosSolidos:
                if self.gang.colideLeste(objeto.sprite):
                    b = True
                    break
            if not b:
                self.gang.andaLeste()

    def checaInteratividade(self):

        if self.wolf.colidiu(self.escada) and self.gang.colidiu(self.escada):
            self.rodando = False

        if self.console.apertou("E"):
            movel = self.moveis[0]
            if self.wolf.colideLeste(movel.sprite):
                movel.empurra()

            for porta in self.portas:
                if self.wolf.colidiu(porta.sprite):
                    if not porta.travada:
                        porta.abre()
                    else:
                        if not len(self.wolf.inventario) == 0:
                            for objeto in self.wolf.inventario:
                                if isinstance(objeto, Chave):
                                    if porta.destrava(objeto.codigo):
                                        self.wolf.inventario.remove(objeto)
                                        Mensagem("Oh... A porta abriu.", "WOLF", self.console)
                            if porta.travada:
                                Mensagem("A porta esta trancada.", "WOLF", self.console)
                        else:
                            Mensagem("A porta esta trancada.", "WOLF", self.console)

        if self.console.apertou("L"):
            movel = self.moveis[0]
            if self.gang.colideLeste(movel.sprite):
                movel.empurra()

            for porta in self.portas:
                if self.gang.colidiu(porta.sprite):
                    if not porta.travada:
                        porta.abre()
                    else:
                        if not len(self.gang.inventario) == 0:
                            for objeto in self.wolf.inventario:
                                if isinstance(objeto, Chave):
                                    if porta.destrava(objeto.codigo):
                                        self.gang.inventario.remove(objeto)
                                        Mensagem("Oh... A porta abriu.", "GANG", self.console)
                            if porta.travada:
                                Mensagem("A porta esta trancada.", "GANG", self.console)
                        else:
                            Mensagem("A porta esta trancada.", "GANG", self.console)

    def pausa(self):

        while self.checaComandosPausado():
            self.console.janela.draw_text("Aperte O para sair e ESC para cancelar", self.console.janela.width * 0.2,
                                          self.console.janela.height / 2, 36,
                                          (0, 250, 250), "Arial", False, False)
            self.console.atualizaJanela()

    def desenhaAuxilio(self):
        for x in self.paredes:
            x.sprite.draw()
        self.wolf.desenhaAuxilio()
        self.gang.desenhaAuxilio()
        self.escada.draw()

    def atualizaJanela(self):
        self.fundo.draw()
        for porta in self.portas:
            porta.desenha()
        for movel in self.moveis:
            movel.desenha()
        if self.dev:
            self.desenhaAuxilio()
        self.wolf.desenha()
        self.wolf.desenhaInventario(Constantes.larguraJanela * 0.1)
        self.gang.desenha()
        self.gang.desenhaInventario(Constantes.larguraJanela * 0.8)
        self.console.atualizaJanela()

    def checaComandosPausado(self):
        self.console.resetaUlt()

        if self.console.apertou("ESC"):
            return False
        if self.console.apertou("O"):
            self.rodando = False
            return False
        return True
