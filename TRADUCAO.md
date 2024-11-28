# Introdução
Este jogo de labirinto foi desenvolvido em Python utilizando a biblioteca Pygame, aplicando princípios de programação orientada a objetos (OOP) para modularidade e escalabilidade. O jogo desafia os jogadores a navegar por labirintos cada vez mais complexos, superar obstáculos como monstros e portas trancadas e usar chaves estrategicamente para progredir. O sistema de pontuação recompensa os jogadores com base na velocidade de conclusão, incentivando a rejogabilidade e a melhoria de habilidades.

# Recursos
Níveis:

20 níveis pré-definidos com dificuldade crescente.
Monstros, portas e chaves são introduzidos a partir do nível 10.
Geração procedural de layouts de labirintos para garantir variedade no design.
Elementos do Jogo:

Monstros: Representados como pontos rosa, movem-se aleatoriamente e encerram o jogo ao colidir com o jogador.
Portas: Representadas como pontos dourados, bloqueiam o caminho do jogador e exigem chaves para serem abertas.
Chaves: Representadas como pontos amarelos, cada chave corresponde a uma porta.
Sistema de Pontuação:

Baseado na velocidade com que o jogador completa cada nível.
Conclusão mais rápida resulta em pontuações mais altas, incentivando eficiência.
Power-ups:

Aumentos temporários de velocidade (recurso opcional) são espalhados em alguns níveis para melhorar o movimento do jogador.
Mensagens:

Exibição em tempo real de mensagens para eventos, como pegar chaves, desbloquear portas ou colidir com monstros.
# Jogabilidade
Objetivo: Navegar pelo labirinto do ponto inicial até a linha de chegada, evitando monstros e desbloqueando portas com chaves.

Regras:

Evite monstros; a colisão resulta em "Game Over".
Colete chaves para desbloquear portas e progredir.
Complete o nível no menor tempo possível para maximizar a pontuação.
Progressão:

Níveis 1-9: Navegação simples no labirinto.
Níveis 10-20: Introdução de monstros, portas e chaves para maior complexidade.
# Detalhes Técnicos
Linguagem de Programação: Python

Biblioteca: Pygame

Arquitetura do Jogo:

Design orientado a objetos com classes para Jogador, Monstro, Porta, Chave e Labirinto.
Loop de jogo baseado em eventos, lidando com entradas do usuário, colisões e progressão de níveis.
Classes Principais:

Jogador: Gerencia movimento, detecção de colisões e interação com elementos do jogo.
Monstro: Implementa lógica de movimento aleatório e comportamento de colisão.
Labirinto: Gera e renderiza dinamicamente o layout do labirinto para cada nível.
Porta e Chave: Controlam posicionamento e mecânica de desbloqueio.
Gráficos:

Sprites simples em 2D para os elementos do jogo.
Representação codificada por cores para fácil diferenciação:
Rosa: Monstros
Amarelo: Chaves
Dourado: Portas
Som e Animações:

Recurso opcional: Música de fundo e efeitos sonoros para interações (ex.: pegar uma chave, desbloquear uma porta).
Animação de explosão ao colidir com um monstro.
# Instalação e Configuração
Dependências:

Python 3.10 ou superior
Biblioteca Pygame (pip install pygame)
Executando o Jogo:

Clone o repositório ou baixe os arquivos do jogo.
Execute o script principal:
bash
Copiar código
python maze_game.py  
Configuração:

As configurações de dificuldade podem ser ajustadas modificando a velocidade dos monstros ou a complexidade do labirinto no código.
Níveis do jogo são facilmente expansíveis adicionando novos layouts de labirinto.
# Melhorias Futuras
Geração procedural de layouts de labirintos para níveis infinitos.
Ranking online para acompanhar as pontuações dos jogadores.
Modo multiplayer para jogabilidade cooperativa ou competitiva.
Power-ups adicionais, como invisibilidade para evitar monstros.
7. Agradecimentos
Este jogo foi desenvolvido como um projeto para explorar as capacidades do Python no desenvolvimento de jogos. Ele combina mecânicas de resolução de problemas com uma jogabilidade envolvente, proporcionando uma experiência agradável para jogadores de todas as idades.
