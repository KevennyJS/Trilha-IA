import moinhos
import verificarMoinho
from default import *
from verificarMovimento import *



def proximoJogador(jogador=None):
    if jogador == 0:
        return 1
    else:
       return 0


# verificarmovimento(15, 23)
def main():
    changePlayer = False
    movimentarPara = 0
    jogador = 0
    listaMoinhosContidos = []
    pecasJogador1 = 8
    pecasJogador2 = 8
    while True:
        changePlayer = False
        print(f"Jogador {jogador}\n\n")
        print(f"{tabuleiro} \n\n")


        #se ainda houver peças para serem jogadas pelos usuarios
        if pecasJogador1 > 0 and pecasJogador2 > 0:
            pecaEscolhida = int(input("Digite o campo escolhido: "))
            if tabuleiro[pecaEscolhida] is None:
                tabuleiro[pecaEscolhida] = jogador
                if jogador == 0:
                    pecasJogador1 -= 1
                    changePlayer = True
                else:
                    pecasJogador2 -= 1
                    changePlayer = True
            else:
                print("O campo escolhido já possui uma peça, por favor, escolha outro campo.")
        else:
            pecaEscolhida = int(input("Selecione a peça escolhida: "))
            movimentarPara = int(input("Digite o campo para onde deseja movimentar: "))
            if tabuleiro[pecaEscolhida] == jogador:
                print(verificarmovimento(pecaEscolhida, movimentarPara))
                if verificarmovimento(pecaEscolhida, movimentarPara):
                    tabuleiro[movimentarPara] = tabuleiro[pecaEscolhida]
                    tabuleiro[pecaEscolhida] = None
                    changePlayer = True
            else:
                print("Essa peça não é sua, por favor, escolha outra")

        #limpando a lsita de moinhos que contem a peça selecionada
        listaMoinhosContidos = []
        #procurar combinações que possuam a nova posição da peça
        for element in moinhos.moinhos:
            if pecasJogador1 > 0 and pecasJogador2 > 0:
                if element.__contains__(pecaEscolhida):
                    listaMoinhosContidos.append(element)
            else:
                if element.__contains__(movimentarPara):
                    listaMoinhosContidos.append(element)

        #verificando se entre as separadas, alguma da "match" de moinho
        for filtered in listaMoinhosContidos:
            if tabuleiro[filtered[0]] == jogador and tabuleiro[int(filtered[1])] == jogador and tabuleiro[int(filtered[2])] == jogador:
                print("===================MOINHO====================")
                pecaRemover = int(input("Selecione uma peça do adversario para remover: "))
                if tabuleiro[pecaRemover] != jogador and tabuleiro[pecaRemover] != None:
                    tabuleiro[pecaRemover] = None

        if changePlayer:
            jogador = proximoJogador(jogador)


if __name__ == "__main__":
    main()
