import random

import numpy
from src.default import moinhos
from src.funcoes.verificarJogo import verificarJogo
from src.funcoes.verificarMovimento import *


def proximoJogador(jogador=None):
    if jogador == 0:
        return 1
    else:
        return 0


def main():
    changePlayer = False
    movimentarPara = 0
    jogador = 0
    listaMoinhosContidos = []
    pecasJogador1 = 8
    pecasJogador2 = 8
    contador_movimentor_endgame = 0
    bloquearVerificacao = False
    while True:
        changePlayer = False
        print(f"Jogador {jogador}\n\n")
        print(f"{tabuleiro} \n\n")

        if pecasJogador1 > 0 and pecasJogador2 > 0:  # se ainda houver peças para serem jogadas pelos usuarios
            if jogador == 0:
                pecaEscolhida = int(input("Digite o campo escolhido: "))
                if tabuleiro[pecaEscolhida] is None and pecaEscolhida < 24:
                    if jogador == 0:
                        tabuleiro[pecaEscolhida] = jogador
                        pecasJogador1 -= 1
                        changePlayer = True
                else:
                    bloquearVerificacao = True
                    print("O campo escolhido já possui uma peça, por favor, escolha outro campo.")
            else:
                while True:
                    pecaEscolhida = iaEscolha = random.randint(0, 23)
                    if (tabuleiro[iaEscolha] is None):
                        tabuleiro[iaEscolha] = jogador
                        pecasJogador2 -= 1
                        changePlayer = True
                        break

        else:
            pecaEscolhida = int(input("Selecione a peça que deseja movimentar: "))
            movimentarPara = int(input("Digite o campo para onde deseja movimentar: "))
            if tabuleiro[pecaEscolhida] == jogador:
                # verifica se o jogador atual tem 3 peças, para poder movimentar para qualquer lugar do mapa e se o campo para onde ele vai está vazio
                if tabuleiro.count(jogador) == 3 and tabuleiro[movimentarPara] is None:
                    if contador_movimentor_endgame < 10 and tabuleiro.count(1) == 3 and tabuleiro.count(0) == 3:
                        tabuleiro[movimentarPara] = jogador  # salva a nova posição da peça
                        tabuleiro[pecaEscolhida] = None  # limpa a posição antiga da peça
                        contador_movimentor_endgame += 1
                        changePlayer = True  # muda o jogador
                        status_do_game = verificarJogo()  # verifica se alguém venceu
                        if status_do_game != 2:
                            if status_do_game == 1:
                                print("Jogador 2 Venceu")
                            else:
                                print("Jogador 1 Venceu")
                            exit()
                    elif contador_movimentor_endgame == 10:
                        print("Fim de jogo! Empate.")
                        exit()
                    else:
                        tabuleiro[pecaEscolhida] = None
                        tabuleiro[movimentarPara] = jogador
                        status_do_game = verificarJogo()  # verifica se alguém venceu
                        if status_do_game != 2:
                            if status_do_game == 1:
                                print("Jogador 2 Venceu")
                            else:
                                print("Jogador 1 Venceu")
                            exit()
                elif verificarmovimento(pecaEscolhida, movimentarPara) and tabuleiro[movimentarPara] is None:  # movimentação comum
                    tabuleiro[movimentarPara] = tabuleiro[pecaEscolhida]  # salva a nova posição da peça
                    tabuleiro[pecaEscolhida] = None  # limpa a posição antiga da peça
                    changePlayer = True #muda o jogador
                    status_do_game = verificarJogo() #verifica se alguém venceu
                    if status_do_game != 2:
                        if status_do_game == 1:
                            print("Jogador 2 Venceu")
                        else:
                            print("Jogador 1 Venceu")
                        exit()
                else:
                    bloquearVerificacao = True
                    print("Você não pode mover para uma casa onde já possue peças")
            else:
                bloquearVerificacao = True
                print("Essa peça não é sua, por favor, escolha outra")

        if bloquearVerificacao is False:
            listaMoinhosContidos = []  # limpando a lsita de moinhos que contem a peça selecionada
            for element in moinhos.moinhos:  # procurar combinações que possuam a nova posição da peça
                if pecasJogador1 > 0 and pecasJogador2 > 0:
                    if element.__contains__(pecaEscolhida):
                        listaMoinhosContidos.append(element)
                else:
                    if element.__contains__(movimentarPara):
                        listaMoinhosContidos.append(element)
            for filtered in listaMoinhosContidos:  # verificando se entre as separadas, alguma da "match" de moinho
                if tabuleiro[filtered[0]] == jogador and tabuleiro[int(filtered[1])] == jogador and tabuleiro[int(filtered[2])] == jogador:
                    print("===================MOINHO====================")
                    if jogador == 0:
                        pecaRemover = int(input("Selecione uma peça do adversario para remover: "))
                        if tabuleiro[pecaRemover] != jogador and tabuleiro[pecaRemover] != None:
                            tabuleiro[pecaRemover] = None
                    else:
                        while True:
                            aleatorio = random.randint(0,23)
                            if(tabuleiro[aleatorio] == 0):
                                tabuleiro[aleatorio] = None
                                print(f"A IA removeu a peça {aleatorio}")
                                break

            if changePlayer:
                jogador = proximoJogador(jogador)
        bloquearVerificacao = False


if __name__ == "__main__":
    main()
