import string
from PPlay.gameimage import *

from Objetos.Comuns.parede import Parede
from Objetos.Interativos.alavanca import *
from Objetos.Interativos.chave import Chave
from Objetos.Interativos.nota import Nota
from Objetos.Interativos.plataforma import *
from Objetos.Interativos.porta import *
from Personagens.boneco import *
from Util.cores import *
from Util.mensagem import Mensagem


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
    notas = None
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

        self.atualizaJanela()
        # Mensagem("AHH!!", "GANG", self.console)
        # Mensagem("A porta se fechou atras de nos!", "GANG", self.console)
        # Mensagem("E agora?! O que fazemos?!", "GANG", self.console)
        # Mensagem("Eu nao sei... E a culpa disso é toda sua.", "WOLF", self.console)
        # Mensagem("Eu avisei que nao era uma boa ideia entrar nessa casa.", "WOLF", self.console)
        # Mensagem("De qualquer forma...", "WOLF", self.console)
        # Mensagem("Deve haver um jeito de sair daqui.", "WOLF", self.console)
        # Mensagem("Vamos procurar.", "WOLF", self.console)
        # Mensagem("Sim... Vamos!", "GANG", self.console)
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
                    [225, 200],
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
        difPorta = 5
        portaSalaDeVisita = Porta("V", 250-difPorta, 450, False, None)
        portaSalaDeEstar = Porta("V", 400-difPorta, 450, False, None)
        portaBanheiro = Porta("V", 400-difPorta, 225, False, None)
        portaLavanderia = Porta("H", 75, 200-difPorta, False, None)
        portaArmazem = Porta("H", 175, 200-difPorta, False, None)
        portaCozinha = Porta("H", 340, 200-difPorta, False, None)
        portaSalaDeJantar = Porta("H", 600, 300-difPorta, False, None)
        self.portas += [portaSalaDeVisita,portaSalaDeEstar,portaBanheiro,portaLavanderia,portaArmazem,portaCozinha,portaSalaDeJantar]

        self.alavancas = []
        alavanca = Alavanca("L", 500-20, 225)
        self.alavancas += [alavanca]

        self.plataformas = []
        plataforma = Plataforma(450, 350)
        self.plataformas += [plataforma]

        self.chaves = []
        chave = Chave(100, 350, "123456")
        self.chaves += [chave]

        self.notas = []
        notaLivro = Nota(400,100,"LIVRO",self.console)
        self.notas+=[notaLivro]

    def checaComandos(self):
        self.console.resetaUlt()

        if self.console.apertou("1"):
            if self.dev:
                self.dev = False
            else:
                self.dev = True

        if self.console.apertou("ESC"):
            self.pausa()

        if self.console.apertou("E"):
            for alavanca in self.alavancas:
                if self.wolf.colidiu(alavanca.sprite):
                    alavanca.ativa()

            for nota in self.notas:
                if self.wolf.colidiu(nota.sprite):
                    nota.exibe()

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

            for chave in self.chaves:
                if self.wolf.colidiu(chave.sprite):
                    self.wolf.pega(chave)

        if self.console.apertou("L"):
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
                                if isinstance(objeto, Chave):
                                    if porta.destrava(objeto.codigo):
                                        self.gang.inventario.remove(objeto)
                                        Mensagem("Ah... A porta se abriu!.", "GANG", self.console)
                            if porta.travada:
                                Mensagem("Droga... A porta esta trancada.", "GANG", self.console)
                        else:
                            Mensagem("Droga... A porta esta trancada.", "GANG", self.console)

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
        for nota in self.notas:
            nota.desenha()
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
