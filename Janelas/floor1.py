import string
from PPlay.gameimage import *

from Janelas.floor2 import Floor2
from Janelas.porao import Porao
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
    dev = False  # developer

    # Predefiniçao das fontes
    tamanho = 24
    spacing = 30
    cor = Cores.preto
    fonte = "Arial"

    # Criacao elementos da janela
    fundo = None
    delta = None
    paredes = None
    forniture = None
    portas = None
    alavancas = None
    alavancaPortaCozinha = None
    plataformas = None
    chaves = None
    notas = None
    escada = None
    porao = None
    objetosSolidos = None
    ult = 0

    # Criação dos personagens
    wolf = None
    gang = None

    floor2=None
    fporao = None

    def __init__(self, console):
        self.console = console

        # Inicialização dos elementos da janela
        self.fundo = GameImage("Imagens/Cenarios/1FLOOR/FUNDO.jpg")

        self.criaParedes()
        self.criaForniture()
        self.criaObjetosInterativos()

        # Inicialização dos personagens
        self.wolf = Boneco("WOLF",1)
        self.gang = Boneco("GANG",2)

        self.floor2 = Floor2(console,self.wolf,self.gang)
        self.fporao = Porao(console,self.wolf,self.gang)

        self.objetosSolidos = []

        # Mensagem("AHH!!", "GANG", self.console)
        # Mensagem("A porta se fechou atras de nos!", "GANG", self.console)
        # Mensagem("E agora?! O que fazemos?!", "GANG", self.console)
        # Mensagem("Eu nao sei... E a culpa disso é toda sua.", "WOLF", self.console)
        # Mensagem("Eu avisei que nao era uma boa ideia entrar nessa casa.", "WOLF", self.console)
        # Mensagem("De qualquer forma...", "WOLF", self.console)
        # Mensagem("Deve haver um jeito de sair daqui.", "WOLF", self.console)
        # Mensagem("Vamos procurar.", "WOLF", self.console)
        # Mensagem("Sim... Vamos!", "GANG", self.console)

        self.play()


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

    def criaForniture(self):
        letras = list(string.ascii_uppercase[:20])
        self.forniture = []
        for x in letras:
            self.forniture += [Parede("Imagens\Objetos\Forniture\FLOOR1/" + x + ".png")]
        posicoes = [[60, 60],
                    [100, 60],
                    [160, 280],
                    [60, 310],
                    [100, 350],
                    [60, 385],
                    [110, 400],
                    [100, 470],
                    [200, 315],
                    [410, 315],
                    [530, 410],
                    [610, 415],
                    [620, 480],
                    [460, 275],
                    [465, 215],
                    [589, 120],
                    [550, 140],
                    [670, 135],
                    [605, 90],
                    [605, 254]]
        for i in range(len(self.forniture)):
            self.forniture[i].setXY(posicoes[i][0], posicoes[i][1])


    def criaObjetosInterativos(self):
        self.portas = []
        portaEntrada = Porta("H",300,550,True,"impossivel")
        portaSalaDeVisita = Porta("V", 250, 450, False, None)
        portaSalaDeEstar = Porta("V", 400, 450, False, None)
        portaBanheiro = Porta("V", 400, 225, False, None)
        portaLavanderia = Porta("H", 75, 200, True, "chaveDourada")
        portaArmazem = Porta("H", 175, 200, True, "alavancaLavanderia")
        portaCozinha = Porta("H", 340, 200, False, None)
        portaSalaDeJantar = Porta("H", 600, 300, False, None)
        self.portas += [portaSalaDeVisita, portaSalaDeEstar, portaBanheiro, portaLavanderia, portaArmazem, portaCozinha,
                        portaSalaDeJantar,portaEntrada]

        self.alavancas = []
        alavanca = Alavanca("L", 150 - 20, 250)
        self.alavancas += [alavanca]

        self.escada = Sprite("Imagens\Objetos\Interativos\ESCADA.png")
        self.escada.x = 260
        self.escada.y = 210

        self.porao = Sprite("Imagens\Objetos\Interativos\PORAO.png")
        self.porao.x = 200
        self.porao.y = 250


    def checaComandos(self):
        self.console.resetaUlt()

        if self.console.apertou("I"):
            if self.dev:
                self.dev = False
            else:
                self.dev = True

        if self.console.apertou("ESC"):
            self.pausa()

        if self.wolf.colidiu(self.escada) and self.gang.colidiu(self.escada):
            self.floor2.play()
            if self.floor2.esc:
                self.rodando = False
            else:
                self.rodando = True

        if self.wolf.colidiu(self.porao) and self.gang.colidiu(self.porao):
            self.fporao.play()
            if self.fporao.esc:
                self.rodando = False
            else:
                self.rodando = True


        self.checaInteratividade(self.wolf)
        self.checaInteratividade(self.gang)


        self.objetosSolidos.clear()
        self.objetosSolidos += self.paredes+self.portas+self.alavancas+self.forniture
        self.checaMovimento(self.wolf)
        self.checaMovimento(self.gang)


    def checaMovimento(self,personagem):


        if self.console.pressionou(personagem.up):
            b = False
            for objeto in self.objetosSolidos:
                if personagem.colideNorte(objeto.sprite):
                    b = True
                    break
            if not b:
                personagem.andaNorte()

        if self.console.pressionou(personagem.down):
            b = False
            for objeto in self.objetosSolidos:
                if personagem.colideSul(objeto.sprite):
                    b = True
                    break
            if not b:
                personagem.andaSul()

        if self.console.pressionou(personagem.left):
            b = False
            for objeto in self.objetosSolidos:
                if personagem.colideOeste(objeto.sprite):
                    b = True
                    break
            if not b:
                personagem.andaOeste()

        if self.console.pressionou(personagem.right):
            b = False
            for objeto in self.objetosSolidos:
                if personagem.colideLeste(objeto.sprite):
                    b = True
                    break
            if not b:
                personagem.andaLeste()



    def checaInteratividade(self,personagem):


        if self.console.apertou(personagem.interact):

            alavanca = self.alavancas[0]
            if personagem.colidiu(alavanca.sprite):
                alavanca.ativa()
                if self.portas[4].travada:
                    self.portas[4].destrava("alavancaLavanderia")
                    Mensagem("Parece que algo foi destravado", personagem, self.console)

            for porta in self.portas:
                if personagem.colidiu(porta.sprite):
                    if not porta.travada:
                        porta.abre()
                    else:
                        if not len(personagem.inventario) == 0:
                            for objeto in personagem.inventario:
                                if isinstance(objeto, Chave):
                                    if porta.destrava(objeto.codigo):
                                        personagem.inventario.remove(objeto)
                                        Mensagem("Oh... A porta abriu.", personagem, self.console)
                            if porta.travada:
                                Mensagem("A porta esta trancada.", personagem, self.console)
                        else:
                            Mensagem("A porta esta trancada.", personagem, self.console)



    def pausa(self):
        while self.checaComandosPausado():
            self.console.janela.draw_text("Aperte O para sair e ESC para cancelar", self.console.janela.width * 0.2,
                                          self.console.janela.height / 2, 36,
                                          (0, 250, 250), "Arial", False, False)
            self.console.atualizaJanela()


    def desenhaAuxilio(self):
        for x in self.paredes:
            x.sprite.draw()
        self.escada.draw()
        self.porao.draw()
        self.wolf.desenhaAuxilio()
        self.gang.desenhaAuxilio()


    def atualizaJanela(self):
        self.fundo.draw()
        for porta in self.portas:
            porta.desenha()
        for alavanca in self.alavancas:
            alavanca.desenha()
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
