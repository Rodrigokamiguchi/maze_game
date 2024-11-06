import pygame
import sys
import random
import design

class Desafio:
    def __init__(self):
        self.labirinto = [['1' for _ in range(design.LABIRINTO_LARGURA)] for _ in range(design.LABIRINTO_ALTURA)]

    def criar_labirinto(self):
        start_x, start_y = random.randrange(1, design.LABIRINTO_LARGURA, 2), random.randrange(1, design.LABIRINTO_ALTURA, 2)
        self.labirinto[start_y][start_x] = '0'
        self.desenhar_labirinto(start_x, start_y)
        return self.labirinto

    def desenhar_labirinto(self, x, y):
        direcoes = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(direcoes)

        for dx, dy in direcoes:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 < nx < design.LABIRINTO_LARGURA and 0 < ny < design.LABIRINTO_ALTURA and self.labirinto[ny][nx] == '1':
                self.labirinto[y + dy][x + dx] = '0'
                self.labirinto[ny][nx] = '0'
                self.desenhar_labirinto(nx, ny)

class Game:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption(design.TITULO_JOGO)
        self.fonte = pygame.font.Font(None, 36)
        self.nivel = 1  # Nivel inicial
        self.pontuacao = 0 # Inciar pontuação
        self.iniciar_novo_nivel()

    def iniciar_novo_nivel(self):
        self.tempo_inicio = pygame.time.get_ticks() # Incia o tempo ao começar o nivel
        self.tempo_nivel = pygame.time.get_ticks() # Incia o tempo do nivel
        self.desafio = Desafio()
        self.labirinto = self.desafio.criar_labirinto()
        self.jogador_pos = [1, 1]
        self.objetivo_pos = [design.LABIRINTO_ALTURA - 2, design.LABIRINTO_LARGURA - 2]
        self.possui_chave = False
        
        # Gerar portas e monstros apenas a partir do nível 10
        if self.nivel >= 10:
            self.portas = self.gerar_portas()
            self.monstros = self.gerar_monstros()
            self.chaves = [self.gerar_posicao_valida() for _ in range(len(self.portas))]
        else:
            self.portas = []
            self.monstros = []
            self.chaves = []

    def gerar_posicao_valida(self):
        while True:
            x, y = random.randrange(1, design.LABIRINTO_LARGURA, 2), random.randrange(1, design.LABIRINTO_ALTURA, 2)
            if self.labirinto[y][x] == '0' and [y, x] != self.jogador_pos and [y, x] != self.objetivo_pos:
                return [y, x]

    def gerar_portas(self):
        return [self.gerar_posicao_valida() for _ in range(2)]

    def gerar_monstros(self):
        return [self.gerar_posicao_valida() for _ in range(3)]

    def desenha_labirinto(self):
        largura_labirinto_px = design.LABIRINTO_LARGURA * design.TAMANHO_CELULA
        altura_labirinto_px = design.LABIRINTO_ALTURA * design.TAMANHO_CELULA
        offset_x = (self.tela.get_width() - largura_labirinto_px) // 2
        offset_y = (self.tela.get_height() - altura_labirinto_px) // 2

        for y, linha in enumerate(self.labirinto):
            for x, celula in enumerate(linha):
                cor = design.BRANCO if celula == '0' else design.PRETO
                pygame.draw.rect(
                    self.tela,
                    cor,
                    (
                        offset_x + x * design.TAMANHO_CELULA,
                        offset_y + y * design.TAMANHO_CELULA,
                        design.TAMANHO_CELULA,
                        design.TAMANHO_CELULA
                    )
                )

        for porta in self.portas:
            pygame.draw.rect(
                self.tela,
                design.DOURADO,
                (
                    offset_x + porta[1] * design.TAMANHO_CELULA,
                    offset_y + porta[0] * design.TAMANHO_CELULA,
                    design.TAMANHO_CELULA,
                    design.TAMANHO_CELULA
                )
            )

        for monstro in self.monstros:
            pygame.draw.rect(
                self.tela,
                design.ROSA,
                (
                    offset_x + monstro[1] * design.TAMANHO_CELULA,
                    offset_y + monstro[0] * design.TAMANHO_CELULA,
                    design.TAMANHO_CELULA,
                    design.TAMANHO_CELULA
                )
            )

    def desenha_jogador(self):
        largura_labirinto_px = design.LABIRINTO_LARGURA * design.TAMANHO_CELULA
        altura_labirinto_px = design.LABIRINTO_ALTURA * design.TAMANHO_CELULA
        offset_x = (self.tela.get_width() - largura_labirinto_px) // 2
        offset_y = (self.tela.get_height() - altura_labirinto_px) // 2

        pygame.draw.rect(
            self.tela,
            design.AZUL,
            (
                offset_x + self.jogador_pos[1] * design.TAMANHO_CELULA,
                offset_y + self.jogador_pos[0] * design.TAMANHO_CELULA,
                design.TAMANHO_CELULA,
                design.TAMANHO_CELULA
            )
        )

    def desenha_objetivo(self):
        largura_labirinto_px = design.LABIRINTO_LARGURA * design.TAMANHO_CELULA
        altura_labirinto_px = design.LABIRINTO_ALTURA * design.TAMANHO_CELULA
        offset_x = (self.tela.get_width() - largura_labirinto_px) // 2
        offset_y = (self.tela.get_height() - altura_labirinto_px) // 2

        pygame.draw.rect(
            self.tela,
            design.VERMELHO,
            (
                offset_x + self.objetivo_pos[1] * design.TAMANHO_CELULA,
                offset_y + self.objetivo_pos[0] * design.TAMANHO_CELULA,
                design.TAMANHO_CELULA,
                design.TAMANHO_CELULA
            )
        )

    def desenha_chaves(self):
        largura_labirinto_px = design.LABIRINTO_LARGURA * design.TAMANHO_CELULA
        altura_labirinto_px = design.LABIRINTO_ALTURA * design.TAMANHO_CELULA
        offset_x = (self.tela.get_width() - largura_labirinto_px) // 2
        offset_y = (self.tela.get_height() - altura_labirinto_px) // 2

        for chave in self.chaves:
            pygame.draw.rect(
                self.tela,
                design.AMARELO,
                (
                    offset_x + chave[1] * design.TAMANHO_CELULA,
                    offset_y + chave[0] * design.TAMANHO_CELULA,
                    design.TAMANHO_CELULA,
                    design.TAMANHO_CELULA
                )
            )


    def mover_monstros(self):
        for i, monstro in enumerate(self.monstros):
            direcao = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
            nova_pos = [monstro[0] + direcao[0], monstro[1] + direcao[1]]
            if 0 <= nova_pos[0] < design.LABIRINTO_ALTURA and 0 <= nova_pos[1] < design.LABIRINTO_LARGURA:
                if self.labirinto[nova_pos[0]][nova_pos[1]] == '0' and nova_pos != self.jogador_pos:
                    self.monstros[i] = nova_pos

    def mostrar_mensagem(self, mensagem):
        texto = self.fonte.render(mensagem, True, design.BRANCO)
        self.tela.blit(texto, (10, 10))

    def verificar_colisao_monstro(self):
        return any(self.jogador_pos == monstro for monstro in self.monstros)
    
    def mostrar_pontuçao_tempo(self):
        tempo_decorrido = (pygame.time.get_ticks() - self.tempo_inicio) // 1000  # Em segundos
        texto_pontuacao = self.fonte.render(f"Pontuação: {self.pontuacao}", True, design.BRANCO)
        texto_tempo = self.fonte.render(f"Tempo: {tempo_decorrido}s", True, design.BRANCO)
        self.tela.blit(texto_pontuacao, (10, 10))
        self.tela.blit(texto_tempo, (10, 50))

    def calcular_pontuacao(self):
        tempo_nivel = (pygame.time.get_ticks() - self.tempo_nivel) // 1000
        print(f"Tempo do nivel {tempo_nivel}")
        pontos_ganhos = max(100 - tempo_nivel, 10)  # Exemplo: quanto mais rápido, mais pontos
        self.pontuacao += pontos_ganhos

    def jogo_labirinto(self):
        clock = pygame.time.Clock()
        while self.nivel <= 20:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    nova_pos = list(self.jogador_pos)
                    if event.key == pygame.K_UP:
                        nova_pos[0] -= 1
                    elif event.key == pygame.K_DOWN:
                        nova_pos[0] += 1
                    elif event.key == pygame.K_LEFT:
                        nova_pos[1] -= 1
                    elif event.key == pygame.K_RIGHT:
                        nova_pos[1] += 1

                    if self.labirinto[nova_pos[0]][nova_pos[1]] == '0':
                        if nova_pos in self.portas and not self.possui_chave:
                            self.mostrar_mensagem("Você precisa de uma chave!")
                            continue
                        self.jogador_pos = nova_pos
                    
                    if self.jogador_pos in self.chaves:
                        self.possui_chave = True
                        self.chaves.remove(self.jogador_pos)

                    if self.jogador_pos == self.objetivo_pos:
                        self.calcular_pontuacao()
                        self.mostrar_mensagem(f"Parabéns! Nivel {self.nivel} concluído!")
                        pygame.display.flip()
                        pygame.time.delay(1000)
                        self.nivel += 1
                        if self.nivel > 20:
                            self.mostrar_mensagem("Você completou todos os níveis! Parabéns!")
                            pygame.display.flip()
                            pygame.time.delay(2000)
                            pygame.quit()
                            sys.exit()
                        self.iniciar_novo_nivel()

            if self.verificar_colisao_monstro():
                self.mostrar_mensagem("Game Over! Você foi derrotado por um monstro.")
                pygame.display.flip()
                pygame.time.delay(2000)
                pygame.quit()
                sys.exit()

            self.mover_monstros()
            self.tela.fill(design.PRETO)
            self.desenha_labirinto()
            self.desenha_jogador()
            self.desenha_objetivo()
            self.desenha_chaves()
            self.mostrar_pontuçao_tempo()
            pygame.display.flip()
            clock.tick(10)

if __name__ == "__main__":
    jogo = Game()
    jogo.jogo_labirinto()
