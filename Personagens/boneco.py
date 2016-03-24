from PPlay.sprite import *
from Constantes.constantes import *

class Boneco:
    # Criaçao das variaveis
    boneco = None
    velocidade = Constantes.velocidadeBoneco
    iniPosX = 400
    iniPosY = 400

    # Criacao dos colisores
    colisorNorte = None
    colisorSul = None
    colisorOeste = None
    colisorLeste = None

    def __init__(self, caminho):
        # Inicializacao das variaveis
        self.boneco = Sprite(caminho)
        self.boneco.x = self.iniPosX
        self.boneco.y = self.iniPosY

        # Inicializacao dos colisores
        self.colisorNorte = Sprite("Imagens/Personagens/HORIZONTAL.png")
        self.colisorNorte.x = self.boneco.x + 1
        self.colisorNorte.y = self.boneco.y - 1
        self.colisorSul = Sprite("Imagens/Personagens/HORIZONTAL.png")
        self.colisorSul.x = self.boneco.x + 1
        self.colisorSul.y = self.boneco.y + self.boneco.height + 1
        self.colisorOeste = Sprite("Imagens/Personagens/VERTICAL.png")
        self.colisorOeste.x = self.boneco.x - 1
        self.colisorOeste.y = self.boneco.y + 1
        self.colisorLeste = Sprite("Imagens/Personagens/VERTICAL.png")
        self.colisorLeste.x = self.boneco.x + self.boneco.width + 1
        self.colisorLeste.y = self.boneco.y + 1

    def desenha(self):
        self.boneco.draw()

    def desenhaAuxilio(self):
        self.colisorNorte.draw()
        self.colisorSul.draw()
        self.colisorOeste.draw()
        self.colisorLeste.draw()

    def andaNorte(self, delta):
        self.boneco.y -= self.velocidade * delta
        self.colisorNorte.y -= self.velocidade * delta
        self.colisorSul.y -= self.velocidade * delta
        self.colisorOeste.y -= self.velocidade * delta
        self.colisorLeste.y -= self.velocidade * delta

    def andaSul(self, delta):
        self.boneco.y += self.velocidade * delta
        self.colisorNorte.y += self.velocidade * delta
        self.colisorSul.y += self.velocidade * delta
        self.colisorOeste.y += self.velocidade * delta
        self.colisorLeste.y += self.velocidade * delta

    def andaOeste(self, delta):
        self.boneco.x -= self.velocidade * delta
        self.colisorNorte.x -= self.velocidade * delta
        self.colisorSul.x -= self.velocidade * delta
        self.colisorOeste.x -= self.velocidade * delta
        self.colisorLeste.x -= self.velocidade * delta

    def andaLeste(self, delta):
        self.boneco.x += self.velocidade * delta
        self.colisorNorte.x += self.velocidade * delta
        self.colisorSul.x += self.velocidade * delta
        self.colisorOeste.x += self.velocidade * delta
        self.colisorLeste.x += self.velocidade * delta

    def colideNorte(self, objeto):
        if self.colisorNorte.collided(objeto):
            return True
        else:
            return False

    def colideSul(self, objeto):
        if self.colisorSul.collided(objeto):
            return True
        else:
            return False

    def colideOeste(self, objeto):
        if self.colisorOeste.collided(objeto):
            return True
        return False

    def colideLeste(self, objeto):
        if self.colisorLeste.collided(objeto):
            return True
        return False
