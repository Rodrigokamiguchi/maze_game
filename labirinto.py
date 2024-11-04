import random
import design

class Desafio:
    def __init__(self):
        # Inicializa o labirinto
        self.labirinto = [['1' for _ in range(design.LABIRINTO_LARGURA)] for _ in range(design.LABIRINTO_ALTURA)]

    def criar_labirinto(self):
        # Inicia a geração do labirinto a partir de uma posição aleatória
        start_x, start_y = random.randrange(1, design.LABIRINTO_LARGURA, 2), random.randrange(1, design.LABIRINTO_ALTURA, 2)
        self.labirinto[start_y][start_x] = '0'  # Marca a célula inicial como caminho
        self.desenhar_labirinto(start_x, start_y)  # Gera o labirinto
        return self.labirinto

    def desenhar_labirinto(self, x, y):
        # Direções para movimento: cima, baixo, esquerda, direita
        direcoes = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(direcoes)  # Embaralha direções para criar um labirinto aleatório

        for dx, dy in direcoes:
            nx, ny = x + dx * 2, y + dy * 2  # Cálculo da nova posição

            # Verifica se a nova posição está dentro dos limites do labirinto
            if 0 < nx < design.LABIRINTO_LARGURA and 0 < ny < design.LABIRINTO_ALTURA and self.labirinto[ny][nx] == '1':
                self.labirinto[y + dy][x + dx] = '0'  # Remove a parede
                self.labirinto[ny][nx] = '0'  # Abre o caminho
                self.desenhar_labirinto(nx, ny)  # Recursão na nova posição

    # Função para imprimir o labirinto
    def imprimir_labirinto(self):
        for linha in self.labirinto:
            print(' '.join(linha))

# Exemplo de uso
if __name__ == "__main__":
    desafio = Desafio()
    labirinto = desafio.criar_labirinto()
    desafio.imprimir_labirinto()
