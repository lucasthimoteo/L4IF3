from Janelas.floor1 import *
from Objetos.Comuns.parede import Parede
from Objetos.Interativos.chave import Chave
from Objetos.Interativos.movel import Movel
from Objetos.Interativos.nota import Nota
from Objetos.Interativos.porta import *
from Objetos.Interativos.teclado import Teclado
from Personagens.boneco import *
from Util.cores import *
from Util.mensagem import Mensagem


class Floor2:
    console = None

    # Estados
    rodando = False
    pausado = False
    esc = False
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
    plataformas = None
    chaves = None
    notas = None
    moveis = None
    cofre = None
    objetosSolidos = None
    ult = 0

    # Criação dos personagens
    wolf = None
    gang = None

    def __init__(self, console, wolf, gang):
        self.console = console

        # Inicialização dos elementos da janela
        self.fundo = GameImage("Imagens/Cenarios/FLOOR2/FUNDO.jpg")

        self.criaParedes()
        self.criaForniture()
        self.criaObjetosInterativos()

        # Inicialização dos personagens
        self.wolf = wolf
        self.gang = gang

        self.chaves = []

        self.objetosSolidos = []

    def play(self):
        Sons.fundo.play()
        self.rodando = True
        while self.rodando:
            Constantes.delta = self.console.delta()

            self.checaComandos()

            self.notas[0].atualiza()

            self.atualizaJanela()

    def criaParedes(self):
        letras = list(string.ascii_uppercase[:16])
        self.paredes = []
        for x in letras:
            self.paredes += [Parede("Imagens\Objetos\Paredes\FLOOR2/" + x + ".png")]
        posicoes = [[50, 50],
                    [50, 50],
                    [50, 500],
                    [250, 50],
                    [250, 150],
                    [250, 400],
                    [250, 550],
                    [325, 200],
                    [400, 50],
                    [400, 250],
                    [400, 300],
                    [400, 460],
                    [400, 500],
                    [650, 300],
                    [750, 50],
                    [650, 300]]

        for i in range(len(self.paredes)):
            self.paredes[i].setXY(posicoes[i][0], posicoes[i][1])

    def criaForniture(self):
        letras = list(string.ascii_uppercase[:12])
        self.forniture = []
        for x in letras:
            self.forniture += [Parede("Imagens\Objetos\Forniture\FLOOR2/" + x + ".png")]
        posicoes = [[700, 60],
                    [550, 60],
                    [700, 200],
                    [410, 60],
                    [410, 250],
                    [410, 310],
                    [500, 450],
                    [550, 400],
                    [60, 60],
                    [60, 200],
                    [60, 400],
                    [350, 350]]
        for i in range(len(self.forniture)):
            self.forniture[i].setXY(posicoes[i][0], posicoes[i][1])

    def criaObjetosInterativos(self):

        self.portas = []
        portaEstudio = Porta("V", 250, 100, False, None)
        portaQuarto = Porta("V", 400, 200, False, None)
        portaBanheiro = Porta("H", 600, 300, False, None)
        portaSecreta = Porta("V", 400, 410, False, None)

        self.portas += [portaEstudio, portaQuarto, portaBanheiro, portaSecreta]

        self.moveis = []
        movelEscondido = Movel(410, 410, 410, 450, "MOVEL", self.console)
        self.moveis += [movelEscondido]

        self.notas = []
        notaLivro = Nota(300, 420, "LIVRO", self.console)
        self.notas += [notaLivro]

        self.escada = Sprite("Imagens\Objetos\Interativos\ESCADA.png")
        self.escada.x = 260
        self.escada.y = 380

        self.cofre = Teclado(200, 450, self.console)

    def checaComandos(self):
        self.console.resetaUlt()

        if self.console.apertou("L"):
            if self.dev:
                self.dev = False
            else:
                self.dev = True

        if self.console.apertou("ESC"):
            self.pausa()

        if self.wolf.colidiu(self.escada) and self.gang.colidiu(self.escada):
            self.rodando = False
        self.checaInteratividade(self.wolf)
        self.checaInteratividade(self.gang)

        self.objetosSolidos.clear()
        self.objetosSolidos += self.paredes + self.portas + self.moveis + [self.cofre] + self.forniture
        self.checaMovimento(self.wolf)
        self.checaMovimento(self.gang)

    def checaMovimento(self, personagem):

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

        if self.console.apertou(personagem.interact):
            if len(self.chaves) > 0:
                chave = self.chaves[0]
                if personagem.colidiu(chave.sprite):
                    personagem.pega(chave)

            movel = self.moveis[0]
            if personagem.colideSul(movel.sprite) and not movel.moveu:
                movel.empurra()
                Mensagem("Se moveu.", personagem, self.console)

            nota = self.notas[0]
            if personagem.colidiu(nota.sprite):
                nota.exibe(personagem.continuar)

            if personagem.colidiu(self.cofre.sprite) and self.cofre.travado:
                self.cofre.destrava(self.notas[0].codigo, personagem)
                if not self.cofre.travado:
                    Mensagem("Abriu!", personagem, self.console)
                    chave = Chave(self.cofre.sprite.x, self.cofre.sprite.y - 10, "chaveDourada")
                    self.chaves += [chave]

            for porta in self.portas:
                if personagem.colidiu(porta.sprite):
                    if not porta.travada:
                        Sons.portaAbrir.play()
                        porta.abre()
                    else:
                        if not len(personagem.inventario) == 0:
                            for objeto in personagem.inventario:
                                if isinstance(objeto, Chave):
                                    if porta.destrava(objeto.codigo):
                                        personagem.inventario.remove(objeto)
                                        Sons.portaDestrava.play()
                                        Mensagem("Oh... A porta abriu.", personagem, self.console)
                            if porta.travada:
                                Sons.portaDestrava.play()
                                Mensagem("A porta esta trancada.", personagem, self.console)
                        else:
                            Sons.portaDestrava.play()
                            Mensagem("A porta esta trancada.", personagem, self.console)

    def pausa(self):
        fundo = Sprite("Imagens\Cenarios\Mensagem\FUNDOMENSAGEM.jpg")
        fundo.x = 10
        fundo.y = 200
        while self.checaComandosPausado():
            fundo.draw()

            self.console.janela.draw_text("Aperte O para sair", fundo.x + 20, fundo.y + 50, 36, Cores.branco, "Arial",
                                          False, False)
            self.console.atualizaJanela()
        self.console.atualizaJanela()

    def desenhaAuxilio(self):
        for x in self.paredes:
            x.sprite.draw()
        self.wolf.desenhaAuxilio()
        self.gang.desenhaAuxilio()
        self.escada.draw()

    def atualizaJanela(self):
        self.fundo.draw()
        for forn in self.forniture:
            forn.sprite.draw()
        for porta in self.portas:
            porta.desenha()
        for movel in self.moveis:
            movel.desenha()
        for nota in self.notas:
            nota.desenha()
        self.cofre.desenha()
        for chave in self.chaves:
            chave.desenha()
        if self.dev:
            self.desenhaAuxilio()
        self.wolf.desenha()
        self.wolf.desenhaInventario(Constantes.larguraJanela * 0.1)
        self.gang.desenha()
        self.gang.desenhaInventario(Constantes.larguraJanela * 0.8)
        self.console.atualizaJanela()

    def checaComandosPausado(self):
        self.console.resetaUlt()

        if self.console.apertou("SPACE"):
            return False
        if self.console.apertou("O"):
            self.rodando = False
            self.esc = True
            return False
        return True
