import verificarMoinho
from default import *
from verificarMovimento import verificarmovimento


def main():
    print(verificarmovimento(15, 23))

    # #iniciando tabuleiro
    # jogador = 0
    # pecasJogador1 = 8
    # pecasJogador2 = 8
    #
    # while True:
    #     print(f"Jogador {jogador}\n\n")
    #
    #     print(f"{tabuleiro} \n\n")
    #
    #     pecaEscolhida = int(input("Digite o campo escolhido: "))
    #
    #     if pecasJogador1 > 0 and pecasJogador2 > 0:
    #         if tabuleiro[pecaEscolhida] is None:
    #             tabuleiro[pecaEscolhida] = jogador
    #             if jogador == 0:
    #                 jogador = 1
    #                 pecasJogador1 -= 1
    #             else:
    #                 jogador = 0
    #                 pecasJogador2 -= 1
    #         else:
    #             print("O campo escolhido já possui uma peça, por favor, escolha outro campo.")
    #     else:
    #         print("s")
    #         #todo implementar movimentação de peças





if __name__ == "__main__":

    main()