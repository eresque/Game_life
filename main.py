from Classes import Field
from functions import cell_condition_rand_choice, cell_condition_manual_choice
import pygame as pg

pg.init()

cell_width, cell_height = 300, 150  # Ввод кол-ва клеток по горизонтали и вертикали
pixel_cell_size = 5  # Ввод длины стороны клетки в пикселях

Gameboard = Field(cell_height, cell_width)
Gameboard.neighbour_determination()  # Определение соседей каждой клетки поля

cell_condition_rand_choice(Gameboard)    # дефолтно стоит автозаполнение поля клетками

# cell_condition_manual_choice(Gameboard) # функция ручного заполнения, при желании можно раскомментить и самому
                                          # заполнить поле, только советую в таком случае уменьшить размеры поля

resolution = width, height = cell_width * pixel_cell_size + 1, cell_height * pixel_cell_size + 1
sc = pg.display.set_mode(resolution)
sc.fill(pg.Color('white'))
pg.display.set_caption("ML&DL\Winter'22: Игра жизнь")
pg.display.set_icon(pg.image.load("Tinkoff.bmp"))
clock = pg.time.Clock()
FPS = 20  # Кол-во кадров, отрисовываемых в секунду
BLACK = (0, 0, 0)
PURPLE = (107, 63, 160)
WHITE = (255, 255, 255)

# Функция, рисующая разметку поля (можно включить при желании раскомментив строки 31-36; 44)

# def draw_net():
#     sc.fill(pg.Color('white'))
#     for x in range(0, width, pixel_cell_size):
#         pg.draw.line(sc, BLACK, (x, 0), (x, height))
#     for y in range(0, height, pixel_cell_size):
#         pg.draw.line(sc, BLACK, (0, y), (width, y))


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    # draw_net()

    for i in range(cell_height):
        for j in range(cell_width):
            if Gameboard.cell_matrix[i][j].condition == 0 and Gameboard.cell_matrix[i][j].neig_cond() == 3:
                pg.draw.rect(sc, PURPLE, (j * pixel_cell_size + 2, i * pixel_cell_size + 2, pixel_cell_size - 2, pixel_cell_size - 2))
                Gameboard.temp_cell_matrix[i][j] = 1
                continue
            if Gameboard.cell_matrix[i][j].condition == 1 and (2 == Gameboard.cell_matrix[i][j].neig_cond() or Gameboard.cell_matrix[i][j].neig_cond() == 3):
                pg.draw.rect(sc, PURPLE, (j * pixel_cell_size + 2, i * pixel_cell_size + 2, pixel_cell_size - 2, pixel_cell_size - 2))
                Gameboard.temp_cell_matrix[i][j] = 1
                continue
            else:
                pg.draw.rect(sc, WHITE, (j * pixel_cell_size + 2, i * pixel_cell_size + 2, pixel_cell_size - 2, pixel_cell_size - 2))
                Gameboard.temp_cell_matrix[i][j] = 0

    Gameboard.cond_changes()
    clock.tick(FPS)
    pg.display.update()
