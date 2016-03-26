import string
from PPlay.gameimage import GameImage

from Janelas.floor2 import Floor2
from Janelas.porao import *
from Objetos.Comuns.parede import *
from Objetos.Interativos.alavanca import *
from Objetos.Interativos.chave import *
from Objetos.Interativos.porta import *
from Personagens.boneco import *
from Util.mensagem import *
from Util.sons import *


class Floor1:
    # O console é aquela classe q faz o controle das janelas e dos outputs e inputs do jogo
    console = None

    # Estados  --  Esses estados servem para o controle d fluxo dos loops
    rodando = False
    pausado = False

    # Essa variavel so serve para ativar ou desativar o modo Developer do jogo. O mode Dev somente mostra algumas informaçoes a mais na tela para auxilio
    dev = False

    # Criacao elementos da janela -- Aqui sao todos os elementos e objetos q serao impressos na tela
    fundo = None  # Essa é a imagem d fundo da fase

    # Esse objetos nao sao interativos
    paredes = None  # aqui sao todas as paredes q compoem a fase. Serve para realizar as colisoes dos personagens com os paredes de forma mais eficiente
    forniture = None  # aqui sao todos os moveis da fase

    # Esses objetos sao interativos
    portas = None  # aqui sao todas as portas da fase
    alavancas = None  # aqui sao todas as alavancasa da fase
    notas = None  # aqui sao todas as notas... itens q podem ser visuzlizados por cima da tela... esse objeto nao é solido... o personagem pode passar por cima deles

    objetosSolidos = None  # aqui é a soma de todas as outras listas d objetos q sao solidos... ou seja... aqueles q o bonoco n pode passar atraves

    # Esses objetos Sprite q serao usados para colisoes e decidir as mudanças de fase.. Ex: escada é u Sprite q leva a para o segundo andar
    escada = None
    porao = None

    # Essas sao as instancias das fases acessiveis atraves da fase atual
    floor2 = None
    fporao = None

    # Criação dos 2 personagens
    wolf = None
    gang = None

    # __________________________________________________________________________________________________________________
    # Aqui temos  inicializaçao de todas as variaveis q foram declaradas a cima
    def __init__(self, console):
        # Inicializa o Console
        self.console = console

        # Inicialização dos elementos da janela
        self.fundo = GameImage("Imagens/Cenarios/FLOOR1/FUNDO.jpg")

        # Inicializa os objetos nao interativos
        self.criaParedes()
        self.criaForniture()

        # Inicaliza todos os objetos interativos
        self.criaObjetosInterativos()

        # Apos inicializado dos os objetos, aquels q forem solidos serao colocados aqui
        self.objetosSolidos = []

        # Inicialização dos personagens... a criaçao de personagem requer q seja dito quais sets d botoes sao usados
        self.wolf = Boneco("WOLF", 1)  # qsui esta sendo usado o set d botoes 1 para o personagem WOLF
        self.gang = Boneco("GANG", 2)

        # Ja inicializa as proximas fases acessiveis atraves dessa fase
        self.floor2 = Floor2(console, self.wolf, self.gang)
        self.fporao = Porao(console, self.wolf, self.gang)

        # neste ponto a tela da fase atual ja foi interiamente montada
        # A primeira fez q a fase FLOOR1 è iniciada uma sequencia da dialogos é iniciada
        self.atualizaJanela()
        Mensagem("AHH!!", self.gang, self.console)
        Mensagem("A porta se fechou atras de nos!", self.gang, self.console)
        Mensagem("E agora?! O que fazemos?!", self.gang, self.console)
        Mensagem("Eu nao sei... E a culpa disso é toda sua.", self.wolf, self.console)
        Mensagem("Eu avisei que nao era uma boa ideia entrar nessa casa.", self.wolf, self.console)
        Mensagem("De qualquer forma...", self.wolf, self.console)
        Mensagem("Deve haver um jeito de sair daqui.", self.wolf, self.console)
        Mensagem("Vamos procurar.", self.wolf, self.console)
        Mensagem("Sim... Vamos!", self.gang, self.console)

        # comando q de fato inicializa o jogo com a jogabilidade
        self.play()

    # _____________________________________________________________________________________________________________
    def play(self):
        self.rodando = True  # seta a varivel q gerecnia o loop principal dessa fase para True
        Sons.fundo.play()  # faz a chamada para a classe d Sons e inicia a musica d fundo dessa fase
        while self.rodando:
            Constantes.delta = self.console.delta()  # Joga o delta do jogo para um Classe global q sera acessada por todas as fase q precisarao fazer uso do msm delta q essa tela gerou

            # Nos proximos 2 IFs sao verificadas colisoes com os Sprites para decidir a mudanca das fases
            # Decide se ira para os egundo andar
            if self.wolf.colidiu(self.escada) and self.gang.colidiu(self.escada):
                self.floor2.play()
                if self.floor2.esc:
                    self.rodando = False
                else:
                    self.rodando = True
            # Decide se ira oara o porao
            if self.wolf.colidiu(self.porao) and self.gang.colidiu(self.porao):
                self.fporao.play()
                if self.fporao.esc:
                    self.rodando = False
                else:
                    self.rodando = True

            self.checaComandos()  # A partir dessa chamada serao efetuados das as checagens de jogabilidade da fase

            self.atualizaJanela()  # A partir dessa chamda serao feitas as exibiçoes do elemtnos na tela

    # ________________________________________________________________________________________________________________
    # Esse metodo foi chamado antes no __init__... aqui q serao Inicializadas as paredes da fase
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

    # ________________________________________________________________________________________________________________
    # Esse metodo foi chamado antes no __init__... aqui q serao Inicializadas os moveis da fase
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

    # ________________________________________________________________________________________________________________
    # Esse metodo foi chamado antes no __init__... aqui q serao Inicializadas todos os obejetos interativos da fase
    def criaObjetosInterativos(self):

        # Aqui sao criadas as portas
        self.portas = []  # de fato inicializa a variavel das portas
        portaEntrada = Porta("H", 300, 550, True, "impossivel")  # para iniciar uma porta é preciso dizer se sera uma porta Vertical("V") ou Horizontal("H")
        portaSalaDeVisita = Porta("V", 250, 450, False, None)    # tambem é preciso determinar a posiçao da porta
        portaSalaDeEstar = Porta("V", 400, 450, False, None)     # também é preciso dizer se a porta estara travada ou nao
        portaBanheiro = Porta("V", 400, 225, False, None)        # e por ultimo, se a porta for travada, inserio o codigo q ira destravar ela
        portaLavanderia = Porta("H", 75, 200, True, "chaveDourada")  # esse codigo pode vim na forma de uma chave ou de um evento externo qualquer
        portaArmazem = Porta("H", 175, 200, True, "alavancaLavanderia")  # como por exemplo uma alavanca q abre a porta
        portaCozinha = Porta("H", 340, 200, False, None)
        portaSalaDeJantar = Porta("H", 600, 300, False, None)
        self.portas += [portaSalaDeVisita, portaSalaDeEstar, portaBanheiro, portaLavanderia, portaArmazem, portaCozinha,
                        portaSalaDeJantar, portaEntrada]

        # Aqui sao criadas as alavancas da fase
        self.alavancas = []
        alavanca = Alavanca("L", 150 - 20, 250)
        self.alavancas += [alavanca]

        # Aqui sao criados os sprites usados para colisoes para entrar em outras fases
        self.escada = Sprite("Imagens\Objetos\Interativos\ESCADA.png")
        self.escada.x = 260
        self.escada.y = 210

        self.porao = Sprite("Imagens\Objetos\Interativos\PORAO.png")
        self.porao.x = 200
        self.porao.y = 250

    # _____________________________________________________________________________________________________________
    # Esse metodo checa todos os comando possiveis no jogo...
    def checaComandos(self):
        self.console.resetaUlt()  # Esse comando esta relacionado a utilizaçao do metodo console.apertou.
                                  # Esse metodo reconhece somente uma pressioanda d botao e para isso precisa deste restaUlt

        # Seta o desseta o modo Developer
        if self.console.apertou("L"):
            if self.dev:
                self.dev = False
            else:
                self.dev = True

        # Pausa o jogo
        if self.console.apertou("ESC"):
            self.pausa()

        # Faz a chamada do metodo q verifica se cada um dos personagens interagiu com algum dos objetos interativos da fase
        self.checaInteratividade(self.wolf)
        self.checaInteratividade(self.gang)

        # È e agora de fato q os objetos solidos sao colocados dentro da lista de objetos solidos...
        # Isso é ideal de se fazer so agora porque é logo antes de verificar colisoes dos personagens com os objetos solidos
        self.objetosSolidos.clear()
        self.objetosSolidos += self.paredes + self.portas + self.alavancas + self.forniture
        # Faz a chamda do metodo q se responsabiliza por movimentar os personagem  verificando as colisoes com objetos solidos
        self.checaMovimento(self.wolf)
        self.checaMovimento(self.gang)

    # ________________________________________________________________________________________________________________
    # Metodo q verifica se cada um dos personagens interagiu com algum dos objetos interativos da fase
    def checaInteratividade(self, personagem):

        if self.console.apertou(personagem.interact):  # verifica se o personage de fato a pertou o seu respectivo botao d interaçao

            # Verifica intetação com Alavancas
            alavanca = self.alavancas[0]
            if personagem.colidiu(alavanca.sprite):
                Sons.alavancaAtiva.play()
                alavanca.ativa()
                if self.portas[4].travada:
                    self.portas[4].destrava("alavancaLavanderia")
                    Mensagem("Parece que algo foi destravado", personagem, self.console)

            # Verifica interaçao com as portas
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
                                Sons.portaTravada.play()
                                Mensagem("A porta esta trancada.", personagem, self.console)
                        else:
                            Sons.portaTravada.play()
                            Mensagem("A porta esta trancada.", personagem, self.console)

    # ____________________________________________________________________________________________________________
    # Metodo q se responsabiliza por movimentar os personagem  verificando as colisoes com objetos solidos
    def checaMovimento(self, personagem):

        if self.console.pressionou(personagem.up):  # Verifica se boneco pode ir para cima e se possivel ele vai
            b = False
            for objeto in self.objetosSolidos:
                if personagem.colideNorte(objeto.sprite):
                    b = True
                    break
            if not b:
                personagem.andaNorte()

        if self.console.pressionou(personagem.down):  # Verifica se boneco pode ir para baixo e se possivel ele vai
            b = False
            for objeto in self.objetosSolidos:
                if personagem.colideSul(objeto.sprite):
                    b = True
                    break
            if not b:
                personagem.andaSul()

        if self.console.pressionou(personagem.left):  # Verifica se boneco pode ir para esquerda e se possivel ele vai
            b = False
            for objeto in self.objetosSolidos:
                if personagem.colideOeste(objeto.sprite):
                    b = True
                    break
            if not b:
                personagem.andaOeste()

        if self.console.pressionou(personagem.right):  # Verifica se boneco pode ir para direita e se possivel ele vai
            b = False
            for objeto in self.objetosSolidos:
                if personagem.colideLeste(objeto.sprite):
                    b = True
                    break
            if not b:
                personagem.andaLeste()

    # _____________________________________________________________________________________________________________
    # Metodo q exibe os elementos na tela
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

    # _____________________________________________________________________________________________________________
    # Metodo q so exibe os elemntos do modoDeveloper
    def desenhaAuxilio(self):
        for x in self.paredes:
            x.sprite.draw()
        self.escada.draw()
        self.porao.draw()
        self.wolf.desenhaAuxilio()
        self.gang.desenhaAuxilio()

    # ______________________________________________________________________________________________________________
    # Metodo responsavel pare efetuar a pausa
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

    def checaComandosPausado(self):
        self.console.resetaUlt()

        if self.console.apertou("SPACE"):
            return False
        if self.console.apertou("O"):
            self.rodando = False
            return False
        return True
