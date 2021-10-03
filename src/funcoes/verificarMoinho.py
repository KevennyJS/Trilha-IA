from src.default.moinhos import *

def verificarMoinho(moinhoParametro):
    moinhoOrdenado = list(moinhoParametro)
    moinhoOrdenado.sort()
    return moinhos.__contains__(moinhoOrdenado)

