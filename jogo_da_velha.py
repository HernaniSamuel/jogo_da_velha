import pygame
import sys
import win32api
from time import sleep

pygame.init()
pygame.font.init()


class Matriz:
    def __init__(self):
        self.matriz = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.vez = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
        self.contagem_vezes = 0

    def preencher(self, coluna, linha, valor):
        valor_x = 0
        valor_y = 0
        if self.matriz[coluna][linha] == ' ':
            self.matriz[coluna][linha] = valor
            if linha == 0:
                valor_x = 100
            if linha == 1:
                valor_x = 300
            if linha == 2:
                valor_x = 500
            if coluna == 0:
                valor_y = 100
            if coluna == 1:
                valor_y = 300
            if coluna == 2:
                valor_y = 500
            if valor == 'X':
                tela.desenhar_x(valor_x, valor_y)
            if valor == 'O':
                tela.desenhar_o(valor_x, valor_y)
            self.contagem_vezes += 1

    def resultado(self):
        if self.matriz[0][0] == self.matriz[0][1] and self.matriz[0][0] == self.matriz[0][2] and self.matriz[0][0] != ' ':
            return [self.matriz[0][0], 0]

        if self.matriz[1][0] == self.matriz[1][1] and self.matriz[1][0] == self.matriz[1][2] and self.matriz[1][0] != ' ':
            return [self.matriz[1][0], 1]

        if self.matriz[2][0] == self.matriz[2][1] and self.matriz[2][0] == self.matriz[2][2] and self.matriz[2][0] != ' ':
            return [self.matriz[2][0], 2]

        if self.matriz[0][0] == self.matriz[1][0] and self.matriz[0][0] == self.matriz[2][0] and self.matriz[0][0] != ' ':
            return [self.matriz[0][0], 3]

        if self.matriz[0][1] == self.matriz[1][1] and self.matriz[0][1] == self.matriz[2][1] and self.matriz[0][1] != ' ':
            return [self.matriz[0][1], 4]

        if self.matriz[0][2] == self.matriz[1][2] and self.matriz[0][2] == self.matriz[2][2] and self.matriz[0][2] != ' ':
            return [self.matriz[0][2], 5]

        if self.matriz[0][0] == self.matriz[1][1] and self.matriz[0][0] == self.matriz[2][2] and self.matriz[0][0] != ' ':
            return [self.matriz[0][0], 6]

        if self.matriz[0][2] == self.matriz[1][1] and self.matriz[0][2] == self.matriz[2][0] and self.matriz[0][2] != ' ':
            return [self.matriz[0][2], 7]

    def conferir_posicoes(self):
        pontos = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if self.matriz[i][j] == ' ':
                    pontos += 1
        if pontos == 0:
            return True


class Tela:
    def __init__(self, largura, altura, titulo):
        self.largura = largura
        self.altura = altura
        self.titulo = titulo
        self.tela = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption(titulo)

        self.tela.fill((250, 250, 250))
        pygame.draw.line(self.tela, (0, 0, 0), (self.largura / 3, 10), (self.largura / 3, altura - 10), 1)
        pygame.draw.line(self.tela, (0, 0, 0), (self.largura / 3 * 2, 10), (self.largura / 3 * 2, altura - 10), 1)
        pygame.draw.line(self.tela, (0, 0, 0), (10, self.altura / 3), (self.largura - 10, altura / 3), 1)
        pygame.draw.line(self.tela, (0, 0, 0), (10, self.altura / 3 * 2), (self.largura - 10, altura / 3 * 2), 1)

    def desenhar_x(self, x, y):
        pygame.draw.line(self.tela, (250, 0, 0), (x-40, y-40), (x+40, y+40), 2)
        pygame.draw.line(self.tela, (250, 0, 0), (x+40, y-40), (x-40, y+40), 2)

    def desenhar_o(self, x, y):
        pygame.draw.circle(self.tela, (0, 250, 0), (x, y), 60)
        pygame.draw.circle(self.tela, (250, 250, 250), (x, y), 58)

    def desenhar_resultado(self, tipo, resultado):
        cor = (0, 0, 0)
        if tipo == 'O':
            cor = (0, 250, 0)
        if tipo == 'X':
            cor = (250, 0, 0)

        if resultado == 0:
            pygame.draw.line(self.tela, (cor), (30, 100), (self.largura-30, 100), 2)

        if resultado == 1:
            pygame.draw.line(self.tela, (cor), (30, 300), (self.largura-30, 300), 2)

        if resultado == 2:
            pygame.draw.line(self.tela, (cor), (30, 500), (self.largura-30, 500), 2)

        if resultado == 3:
            pygame.draw.line(self.tela, (cor), (100, 30), (100, self.altura-30), 2)

        if resultado == 4:
            pygame.draw.line(self.tela, (cor), (300, 30), (300, self.altura-30), 2)

        if resultado == 5:
            pygame.draw.line(self.tela, (cor), (500, 30), (500, self.altura-30), 2)

        if resultado == 6:
            pygame.draw.line(self.tela, (cor), (30, 30), (self.largura - 30, self.altura-30), 2)

        if resultado == 7:
            pygame.draw.line(self.tela, (cor), (30, self.altura-30), (self.largura - 30, 30), 2)

    def desenhar_velha(self):
        self.tela.fill((230, 230, 230))
        font = pygame.font.SysFont('Arial', 100)
        text = font.render('Deu velha!', True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.largura / 2, self.altura / 2))
        self.tela.blit(text, text_rect)


class Jogador:
    def __init__(self, tipo):
        self.tipo = tipo

    def escolher(self):
        if win32api.GetKeyState(0x01) < 0:
            mouse = pygame.mouse.get_pos()
            if mouse[0] <= 200 and mouse[1] <= 200:
                matriz.preencher(0, 0, self.tipo)

            if mouse[0] > 200 and mouse[0] <= 400 and mouse[1] <= 200:
                matriz.preencher(0, 1, self.tipo)

            if mouse[0] > 400 and mouse[1] <= 200:
                matriz.preencher(0, 2, self.tipo)

            if mouse[0] <= 200 and mouse[1] <= 400 and mouse[1] > 200:
                matriz.preencher(1, 0, self.tipo)

            if mouse[0] > 200 and mouse[0] <= 400 and mouse[1] > 200 and mouse[1] < 400:
                matriz.preencher(1, 1, self.tipo)

            if mouse[0] > 400 and mouse[1] > 200 and mouse[1] < 400:
                matriz.preencher(1, 2, self.tipo)

            if mouse[0] <= 200 and mouse[1] > 400:
                matriz.preencher(2, 0, self.tipo)

            if mouse[0] > 200 and mouse[0] <= 400 and mouse[1] > 400:
                matriz.preencher(2, 1, self.tipo)

            if mouse[0] > 400 and mouse[1] > 400:
                matriz.preencher(2, 2, self.tipo)


tela = Tela(600, 600, 'Jogo da velha')
matriz = Matriz()
jogador_um = Jogador('X')
jogador_dois = Jogador('O')


def jogo():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if matriz.vez[matriz.contagem_vezes] == 0:
            jogador_um.escolher()

        if matriz.vez[matriz.contagem_vezes] == 1:
            jogador_dois.escolher()

        if matriz.resultado():
            tela.desenhar_resultado(matriz.resultado()[0], matriz.resultado()[1])
            pygame.display.update()
            sleep(3)
            break

        if matriz.conferir_posicoes():
            if not matriz.resultado():
                tela.desenhar_velha()
                pygame.display.update()
                sleep(3)
                break

        pygame.display.update()


if __name__ == '__main__':
    jogo()
