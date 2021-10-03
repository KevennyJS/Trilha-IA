from src.default.default import *

'''
funcionalidade: verifica se a peça pode se mover para a casa desejada
param: (Index da posição inicial, Index da posição final)
'''
def verificarmovimento(posicaoInicial, posicaoFinal):
    #quinas
    if posicaoInicial == 0:
        return condicaoMovimento(posicaoFinal, 1, 7)
    elif posicaoInicial == 8:
        return condicaoMovimento(posicaoFinal, 9, 15)
    elif posicaoInicial == 16:
        return condicaoMovimento(posicaoFinal, 17, 23)

    #meio direito
    elif posicaoInicial == 7:
        return condicaoMovimento(posicaoFinal, 0, 6, 15)
    elif posicaoInicial == 15:
        return condicaoMovimento(posicaoFinal, 7, 8, 23, 14)
    elif posicaoInicial == 23:
        return condicaoMovimento(posicaoFinal, 15, 16, 22)

    #meio esquerdo
    elif posicaoInicial == 19:
        return condicaoMovimento(posicaoFinal, 18, 20, 11)
    elif posicaoInicial == 11:
        return condicaoMovimento(posicaoFinal, 19, 10, 12, 3)
    elif posicaoInicial == 3:
        return condicaoMovimento(posicaoFinal, 2, 4, 11)

    #meio superior
    elif posicaoInicial == 1:
        return condicaoMovimento(posicaoFinal, 0, 2, 9)
    elif posicaoInicial == 9:
        return condicaoMovimento(posicaoFinal, 1, 8, 10, 17)
    elif posicaoInicial == 17:
        return condicaoMovimento(posicaoFinal, 16, 18, 9)

    #meio inferior
    elif posicaoInicial == 21:
        return condicaoMovimento(posicaoFinal, 22, 20, 13)
    elif posicaoInicial == 13:
        return condicaoMovimento(posicaoFinal, 14, 12, 21, 5)
    elif posicaoInicial == 5:
        return condicaoMovimento(posicaoFinal, 6, 4, 13)
    else:
        if posicaoFinal == posicaoInicial+1 or posicaoFinal == posicaoInicial-1:
            if tabuleiro[posicaoFinal] is None:
                return True
        return False

'''
funcionalidade: função utilizada pela função verificarmovimento, para verificar disponibilidade da movimentação
param: (Index inicial, primeiro Index da posição onde a movimentação é disponivel, ...)
'''
def condicaoMovimento(posicaoFinal, podeIrPara1, podeIrPara2, podeIrPara3 = None, podeIrPara4 = None):
    if podeIrPara3 is None:
        if posicaoFinal != podeIrPara1 and posicaoFinal != podeIrPara2:
            return False
    elif podeIrPara4 is None:
        if posicaoFinal != podeIrPara1 and posicaoFinal != podeIrPara2 and posicaoFinal != podeIrPara3:
            return False
    else:
        if posicaoFinal != podeIrPara1 and posicaoFinal != podeIrPara2 and posicaoFinal != podeIrPara3 and posicaoFinal != podeIrPara4:
            return False

    if tabuleiro[posicaoFinal] is None:
        return True
    else:
        return False

    return True