from Janelas.floor1 import *
from Objetos.Comuns.parede import Parede
from Objetos.Interativos.chave import Chave
from Objetos.Interativos.movel import Movel
from Objetos.Interativos.nota import Nota
from Objetos.Interativos.porta import *
from Objetos.Interativos.plataforma import *
from Objetos.Interativos.teclado import Teclado
from Personagens.boneco import *
from Util.cores import *
from Util.mensagem import Mensagem


class Porao:
    console = None

    # Estados
    rodando = False
    pausado = False
    esc = False
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
    plataformas = None
    notas = None
    detectorPorta = None
    detectorInimigo = None
    inimigoAtivo = None
    inimigo = None
    objetosSolidos = None

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

        self.objetosSolidos = []

    def play(self):
        self.rodando = True
        while self.rodando:
            Constantes.delta = self.console.delta()

            self.checaComandos()

            self.notas[0].atualiza()

            self.atualizaJanela()

    def criaParedes(self):
        letras = list(string.ascii_uppercase[:7])
        self.paredes = []
        for x in letras:
            self.paredes += [Parede("Imagens\Objetos\Paredes\PORAO/" + x + ".png")]
        posicoes = [[100, 150],
                    [100, 150],
                    [100, 400],
                    [350, 150],
                    [350, 240],
                    [350, 300],
                    [350, 300]]

        for i in range(len(self.paredes)):
            self.paredes[i].setXY(posicoes[i][0], posicoes[i][1])

    def criaObjetosInterativos(self):

        self.portas = []
        portaCorredor = Porta("V", 350, 250, True, "plataformas")
        self.portas += [portaCorredor]

        self.notas = []
        nota = Nota(200, 350, "BEMVINDO", self.console)
        self.notas += [nota]

        self.plataformas=[]
        plataforma1 = Plataforma(320,160)
        plataforma2 = Plataforma(320,370)
        self.plataformas += [plataforma1,plataforma2]

        self.detectorPorta = Sprite("Imagens\Objetos\Interativos\DETECTOR.png")
        self.detectorPorta.x = 400
        self.detectorPorta.y = 250

        self.detectorInimigo = Sprite("Imagens\Objetos\Interativos\DETECTOR.png")
        self.detectorInimigo.x = 450
        self.detectorInimigo.y = 250

        self.inimigo = Sprite("Imagens\Objetos\Interativos\INIMIGO.png")
        self.inimigo.x = 700
        self.inimigo.y = 250

    def checaComandos(self):
        self.console.resetaUlt()

        if self.console.apertou("L"):
            if self.dev:
                self.dev = False
            else:
                self.dev = True

        if self.console.apertou("ESC"):
            self.pausa()

        if self.wolf.colidiu(self.detectorPorta) and self.gang.colidiu(self.detectorPorta) and self.portas[0].aberta:
            self.portas[0].abre()
            self.portas[0].aberta = False
            self.portas[0].travada = True

        if self.wolf.colidiu(self.detectorInimigo) and self.gang.colidiu(self.detectorInimigo):
            self.inimigoAtivo = True

        self.checaInteratividade(self.wolf)
        self.checaInteratividade(self.gang)

        self.objetosSolidos.clear()
        self.objetosSolidos += self.paredes + self.portas
        self.checaMovimento(self.wolf)
        self.checaMovimento(self.gang)

    def checaMovimento(self, personagem):

        if self.inimigoAtivo:
            self.inimigo.x-=Constantes.velocidadeBoneco * 1.5 * Constantes.delta

        if self.inimigo.x < self.wolf.sprite.x + self.wolf.sprite.width+5 or self.inimigo.x < self.gang.sprite.x + self.gang.sprite.width+5:
            self.pausa()

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

    def checaInteratividade(self, personagem):


        if personagem.colidiu(self.plataformas[0].sprite):
            self.plataformas[0].ativa()
            if self.plataformas[1].estado and self.portas[0].travada:
                self.portas[0].destrava("plataformas")
                Mensagem("Uma porta foi aberta", personagem, self.console)
        else:
            self.plataformas[0].desativa()

        if personagem.colidiu(self.plataformas[1].sprite):
            self.plataformas[1].ativa()
        else:
            self.plataformas[1].desativa()

        if self.console.apertou(personagem.interact):
            nota = self.notas[0]
            if personagem.colidiu(nota.sprite):
                nota.exibe(personagem.continuar)


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
        self.detectorPorta.draw()
        self.detectorInimigo.draw()
        self.wolf.desenhaAuxilio()
        self.gang.desenhaAuxilio()

    def atualizaJanela(self):
        self.fundo.draw()
        for porta in self.portas:
            porta.desenha()
        for nota in self.notas:
            nota.desenha()
        for plat in self.plataformas:
            plat.desenha()
        if self.inimigoAtivo:
            self.inimigo.draw()
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
            self.esc = True
            return False
        return True
