import verificarMoinho

def main():
    jogador = 0
    pecasJogador1 = 8
    pecasJogador2 = 8

    tabuleiro = [None for _ in range(24)]

    while True:
        print(f"Jogador {jogador}\n\n")

        print(f"{tabuleiro} \n\n")

        pecaEscolhida = int(input("Digite o campo escolhido: "))

        if(tabuleiro[pecaEscolhida] == None):
            tabuleiro[pecaEscolhida] = jogador

            if jogador == 0:
                jogador = 1
                pecasJogador1 -= 1
            else:
                jogador = 0
                pecasJogador2 -= 1
        else:
            print("O campo escolhido já possui uma peça, por favor, escolha outro campo.")





if __name__ == "__main__":

    main()