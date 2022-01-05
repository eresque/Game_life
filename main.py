import copy

from Classes import Field, Cell
import pygame as pg

pg.init()

cell_width, cell_height = 100, 80
pixel_cell_size = 13

Gameboard = Field(cell_height, cell_width)
Gameboard.neighbour_determination()

resolution = width, height = cell_width * pixel_cell_size + 1, cell_height * pixel_cell_size + 1
sc = pg.display.set_mode(resolution)
pg.display.set_caption("ML&DL\Winter'22: Игра жизнь")
pg.display.set_icon(pg.image.load("Tinkoff.bmp"))
clock = pg.time.Clock()
FPS = 50
BERUZ = (48, 213, 200)


def draw_net():
    sc.fill(pg.Color('white'))
    for x in range(0, width, pixel_cell_size):
        pg.draw.line(sc, BERUZ, (x, 0), (x, height))
    for y in range(0, height, pixel_cell_size):
        pg.draw.line(sc, BERUZ, (0, y), (width, y))


sc.fill(pg.Color('white'))
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    # draw_net()

    for i in range(cell_height):
        for j in range(cell_width):
            if Gameboard.cell_matrix[i][j].condition == 0 and Gameboard.cell_matrix[i][j].neig_cond() == 3:
                pg.draw.rect(sc, (107, 63, 160), (
                    j * pixel_cell_size + 2, i * pixel_cell_size + 2, pixel_cell_size - 2, pixel_cell_size - 2))
                Gameboard.temp_cell_matrix[i][j] = 1
                continue
            if Gameboard.cell_matrix[i][j].condition == 1 and (
                    2 == Gameboard.cell_matrix[i][j].neig_cond() or Gameboard.cell_matrix[i][j].neig_cond() == 3):
                pg.draw.rect(sc, (107, 63, 160), (
                    j * pixel_cell_size + 2, i * pixel_cell_size + 2, pixel_cell_size - 2, pixel_cell_size - 2))
                Gameboard.temp_cell_matrix[i][j] = 1
                continue
            else:
                pg.draw.rect(sc, (255, 255, 255), (
                    j * pixel_cell_size + 2, i * pixel_cell_size + 2, pixel_cell_size - 2, pixel_cell_size - 2))
                Gameboard.temp_cell_matrix[i][j] = 0

    Gameboard.cond_changes()
    clock.tick(FPS)
    pg.display.update()
