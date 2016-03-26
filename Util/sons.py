from PPlay.sound import Sound


class Sons:
    portaAbrir = Sound("Sons\portaAbrindo.ogg")
    portaTravada = Sound("Sons/portaTravada.ogg")
    portaDestrava = Sound("Sons/portaDestrava.ogg")
    alavancaAtiva = Sound("Sons/alavancaAtiva.ogg")
    passo = Sound("Sons/passo.ogg")
    fundo = Sound("Sons/fundo.ogg")
    fundo.set_repeat(True)