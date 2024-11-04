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

    def imprimir_labirinto(self):
        for linha in self.labirinto:
            print(' '.join(linha))


class Game:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((design.LARGURA, design.ALTURA))
        pygame.display.set_caption(design.TITULO_JOGO)

        # Cria e gera o labirinto
        self.desafio = Desafio()
        self.labirinto = self.desafio.criar_labirinto()

        # Posição inicial do jogador e objetivo
        self.jogador_pos = [1, 1]  # Posição inicial do jogador (x, y)
        self.objetivo_pos = [design.LABIRINTO_ALTURA - 2, design.LABIRINTO_LARGURA - 2]  # Posição do objetivo

    def desenha_labirinto(self):
        for y, linha in enumerate(self.labirinto):
            for x, celula in enumerate(linha):
                cor = design.BRANCO if celula == '0' else design.PRETO
                pygame.draw.rect(self.tela, cor, (x * design.TAMANHO_CELULA, y * design.TAMANHO_CELULA, design.TAMANHO_CELULA, design.TAMANHO_CELULA))

    def desenha_jogador(self):
        pygame.draw.rect(self.tela, design.AZUL, (self.jogador_pos[1] * design.TAMANHO_CELULA, self.jogador_pos[0] * design.TAMANHO_CELULA, design.TAMANHO_CELULA, design.TAMANHO_CELULA))

    def desenha_objetivo(self):
        pygame.draw.rect(self.tela, design.VERMELHO, (self.objetivo_pos[1] * design.TAMANHO_CELULA, self.objetivo_pos[0] * design.TAMANHO_CELULA, design.TAMANHO_CELULA, design.TAMANHO_CELULA))

    def jogo_labirinto(self):
        clock = pygame.time.Clock()
        while True:
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

                    # Verifica se o novo movimento é válido (não é uma parede)
                    if self.labirinto[nova_pos[0]][nova_pos[1]] == '0':
                        self.jogador_pos = nova_pos

                    # Verifica se o jogador encontrou o objetivo
                    if self.jogador_pos == self.objetivo_pos:
                        print("Parabéns! Você encontrou a saída!")
                        pygame.quit()
                        sys.exit()

            self.tela.fill(design.PRETO)
            self.desenha_labirinto()
            self.desenha_jogador()
            self.desenha_objetivo()
            pygame.display.flip()
            clock.tick(10)


if __name__ == "__main__":
    jogo = Game()
    jogo.jogo_labirinto()
