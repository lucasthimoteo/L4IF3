from PPlay.sprite import *

from Util.constantes import *
from Util.sons import Sons


class Boneco:
    # Criaçao das variaveis
    sprite = None
    nome = None

    up = None
    down = None
    left = None
    right = None
    interact = None
    continuar = None
    back = None

    velocidade = Constantes.velocidadeBoneco
    iniPosX = 300
    iniPosY = 500
    inventario = None

    # Criacao dos colisores
    colisorNorte = None
    colisorSul = None
    colisorOeste = None
    colisorLeste = None

    def __init__(self, personagem, controle):
        # Inicializacao das variaveis
        self.sprite = Sprite("Imagens\Personagens/" + personagem + ".png",4)
        self.sprite.set_total_duration(1000)
        self.nome = personagem
        self.sprite.x = self.iniPosX
        self.sprite.y = self.iniPosY
        self.inventario = []

        if controle == 1:
            self.up = "W"
            self.down = "S"
            self.left = "A"
            self.right = "D"
            self.interact = "E"
            self.continuar = "SPACE"
            self.back = "ESC"
        if controle == 2:
            self.up = "8"
            self.down = "5"
            self.left = "4"
            self.right = "6"
            self.interact = "7"
            self.continuar = "0"
            self.back = "ESC"

        # Inicializacao dos colisores
        self.colisorNorte = Sprite("Imagens/Personagens/HORIZONTAL.png")
        self.colisorNorte.x = self.sprite.x + 1
        self.colisorNorte.y = self.sprite.y - 1
        self.colisorSul = Sprite("Imagens/Personagens/HORIZONTAL.png")
        self.colisorSul.x = self.sprite.x + 1
        self.colisorSul.y = self.sprite.y + self.sprite.height + 1
        self.colisorOeste = Sprite("Imagens/Personagens/VERTICAL.png")
        self.colisorOeste.x = self.sprite.x - 1
        self.colisorOeste.y = self.sprite.y + 1
        self.colisorLeste = Sprite("Imagens/Personagens/VERTICAL.png")
        self.colisorLeste.x = self.sprite.x + self.sprite.width + 1
        self.colisorLeste.y = self.sprite.y + 1

    def desenha(self):
        self.sprite.draw()

    def desenhaAuxilio(self):
        self.colisorNorte.draw()
        self.colisorSul.draw()
        self.colisorOeste.draw()
        self.colisorLeste.draw()

    def andaNorte(self):
        self.sprite.update()
        Sons.passo.play()
        self.sprite.y -= self.velocidade * Constantes.delta
        self.colisorNorte.y -= self.velocidade * Constantes.delta
        self.colisorSul.y -= self.velocidade * Constantes.delta
        self.colisorOeste.y -= self.velocidade * Constantes.delta
        self.colisorLeste.y -= self.velocidade * Constantes.delta

    def andaSul(self):
        self.sprite.update()
        Sons.passo.play()
        self.sprite.y += self.velocidade * Constantes.delta
        self.colisorNorte.y += self.velocidade * Constantes.delta
        self.colisorSul.y += self.velocidade * Constantes.delta
        self.colisorOeste.y += self.velocidade * Constantes.delta
        self.colisorLeste.y += self.velocidade * Constantes.delta

    def andaOeste(self):
        self.sprite.update()
        Sons.passo.play()
        self.sprite.x -= self.velocidade * Constantes.delta
        self.colisorNorte.x -= self.velocidade * Constantes.delta
        self.colisorSul.x -= self.velocidade * Constantes.delta
        self.colisorOeste.x -= self.velocidade * Constantes.delta
        self.colisorLeste.x -= self.velocidade * Constantes.delta

    def andaLeste(self):
        self.sprite.update()
        Sons.passo.play()
        self.sprite.x += self.velocidade * Constantes.delta
        self.colisorNorte.x += self.velocidade * Constantes.delta
        self.colisorSul.x += self.velocidade * Constantes.delta
        self.colisorOeste.x += self.velocidade * Constantes.delta
        self.colisorLeste.x += self.velocidade * Constantes.delta

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

    def colidiu(self, objeto):
        return self.colideNorte(objeto) or self.colideSul(objeto) or self.colideOeste(objeto) or self.colideLeste(objeto)

    def pega(self,objeto):
        self.inventario+=[objeto]
        objeto.pegado()

    def desenhaInventario(self,iniPosX):
        spacing = 20
        for i in range(len(self.inventario)):
            self.inventario[i].sprite.y = 20
            self.inventario[i].sprite.x = iniPosX + spacing*i
            self.inventario[i].sprite.draw()