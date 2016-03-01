from PPlay.window import *
class Console:
    janela=None
    teclado=None
    mouse=None

    def __init__(self,largura,altura):
        self.janela = Window(largura,altura)
        self.teclado = self.janela.get_keyboard()
        self.mouse = self.janela.get_mouse()
