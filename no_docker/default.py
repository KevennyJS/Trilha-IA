tabuleiro = [None for _ in range(24)]

def convPlay(index):
    if tabuleiro[index] == 0:
        return 'P'
    elif tabuleiro[index] == 1:
        return 'B'
    else:
        return 'X'


def exibirTabuleiro():
    print(f"""
    {convPlay(0)}------------------------------{convPlay(1)}------------------------------{convPlay(2)}
    |0                             |1                             |2
    |                              |                              |
    |         {convPlay(8)}--------------------{convPlay(9)}--------------------{convPlay(10)}         |
    |         |8                   |9                   |10       |
    |         |                    |                    |         |
    |         |         {convPlay(16)}----------{convPlay(17)}----------{convPlay(18)}         |         |
    |         |         |16         17        |18       |         |
    |         |         |                     |         |         |
    {convPlay(7)}---------{convPlay(15)}---------{convPlay(23)}                     {convPlay(19)}---------{convPlay(11)}---------{convPlay(3)}
    |7        |15       |23                   |19       |11       |3
    |         |         |                     |         |         |
    |         |         {convPlay(22)}----------{convPlay(21)}----------{convPlay(20)}         |         |
    |         |          22        |21         20       |         |
    |         |                    |                    |         |
    |         {convPlay(14)}--------------------{convPlay(13)}--------------------{convPlay(12)}         |
    |          14                  |13                    12      |
    |                              |                              |
    {convPlay(6)}------------------------------{convPlay(5)}------------------------------{convPlay(4)}
     6                              5                              4
    """)