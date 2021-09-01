<p align="center">
  <img alt="Repository size" src="https://img.shields.io/github/repo-size/rickweb3/projeto-ia-trilha">
  <a href="https://github.com/rickweb3/projeto-ia-trilha/commits/master">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/rickweb3/projeto-ia-trilha">
  </a>
</p>



<h4 align="center"> 
	🚧 Jogo Trilha (Python) - Em construção 🚀 🚧
</h4>



## Sobre o projeto
O projeto Trilha está sendo desenvolvido por: <a href="https://github.com/rickweb3">Henrique Prado</a>, <a href="https://github.com/LilianeCosta767">Liliane Costa</a> na disciplina Inteligência Artificial do curso Sistemas de Informação da Universidade Federal de Sergipe - Campus Itabaiana.<br/>



## Objetivo do projeto
O objetivo deste projeto é aplicar o mecanismo de busca "[nome do mecanismo de busca]" como cérebro do jogador adversário (máquina)
do jogo de tabuleiro Trilha de forma funcional e relevante.<br/>



## Objetivo e regras do jogo de tabuleiro Trilha
O objetivo do jogo é remover as peças inimigas até que restem no máximo duas. <br/>
Em qualquer fase do jogo, quando um jogador forma uma linha horizontal ou vertical com três de suas peças (chamada de <<moinho>>)
sobre o tabuleiro, tem o direito de escolher uma peça inimiga em qualquer posição do tabuleiro para remover, desde que essa peça não
faça parte de um <<moinho>> inimigo.<br/>

	
## Como jogar
Temos três fases no jogo: Início do jogo, Movimentação das peças e Movimentação livre das peças.	

- <b>Início do jogo</b>: cada jogador escolhe uma cor e recebe nove peças com a respectiva cor. Os jogadores vão colocando as peças alternadamente nas posições de suas preferências (de forma semelhante à montagem inicial do jogo da velha). Tanto os cantos dos quadrados quanto os pontos médios de seus lados são posições iniciais (e de jogo) válidas.

- <b>Movimentação das peças</b>: após um jogador ficar com todas as suas peças no tabuleiro, começa a fase de movimentação das peças. As peças desse jogador podem se movimentar vertical ou horizontalmete uma casa, desde que não haja nenhuma peça no local. As peças não pulam casas vazias ou com peças, como o cavalo do Xadrez, sendo possível o movimento em apenas uma casa vazia por rodada.

- <b>Movimentação livre das peças</b>: após um jogador ficar com  apenas três peças no tabuleiro, começa a fase de movimentação livre das peças. As peças desse jogador passam a se movimentar livremente pelo tabuleiro, ignorando demais peças ou espaços vazios, podendo ser posicionadas em qualquer casa vaiza do tabuleiro.<br/>


## Final de jogo
O jogo termina com uma dessas três possibilidades:
- Se um dos jogadores ficar com apenas duas peças, ocasionando uma derrota;
- Se não houver mais nenhuma jogada válida, ocasionando em empate e
- Se ambos os jogadores estiverem com apenas três peças e, em 10 jogadas, não houver vencedor, onde é declarado empate.

---
