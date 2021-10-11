from default import tabuleiro


# 1 = um perdeu
# 0 = zero perdeu
# 2 = ninguém perdeu
def verificarJogo():
    #guarda quantidade de peças de cada tipo
    quantidade_de_um = tabuleiro.count(1)
    quantidade_de_zero = tabuleiro.count(0)

    #retorna o estado atual do game, caso alguém tenha perdido ou não
    if quantidade_de_um < 3:
        return 1
    elif quantidade_de_zero < 3:
        return 0
    else:
        return 2
