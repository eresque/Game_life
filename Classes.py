from random import randrange, randint

x = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1] # Массив создан так, чтобы при выборе между состоянием 0/1, предпочтение отдавалось 0


class Field:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.cell_matrix = [[Cell([i, j], x[randrange(0, 10)]) for i in range(width)] for j in range(height)]
        self.temp_cell_matrix = [[0 for i in range(width)] for j in range(height)]

    def neighbour_determination(self):
        for i in range(self.height):
            for j in range(self.width):
                if i - 1 >= 0:
                    self.cell_matrix[i][j].neighbour_append(self.cell_matrix[i - 1][j])
                if i + 1 < self.height:
                    self.cell_matrix[i][j].neighbour_append(self.cell_matrix[i + 1][j])
                if j - 1 >= 0:
                    self.cell_matrix[i][j].neighbour_append(self.cell_matrix[i][j - 1])
                if j + 1 < self.width:
                    self.cell_matrix[i][j].neighbour_append(self.cell_matrix[i][j + 1])
                if i - 1 >= 0 and j - 1 >= 0:
                    self.cell_matrix[i][j].neighbour_append(self.cell_matrix[i - 1][j - 1])
                if i - 1 >= 0 and j + 1 < self.width:
                    self.cell_matrix[i][j].neighbour_append(self.cell_matrix[i - 1][j + 1])
                if i + 1 < self.height and j - 1 >= 0:
                    self.cell_matrix[i][j].neighbour_append(self.cell_matrix[i + 1][j - 1])
                if i + 1 < self.height and j + 1 < self.width:
                    self.cell_matrix[i][j].neighbour_append(self.cell_matrix[i + 1][j + 1])

    def cond_changes(self):
        for i in range(self.height):
            for j in range(self.width):
                self.cell_matrix[i][j].condition = self.temp_cell_matrix[i][j]


class Cell:
    def __init__(self, coord, cond):
        self.coord = coord
        self.condition = cond
        self.neighbours = []

    def neighbour_append(self, nei_cell): # Добавление клетки в список соседей
        self.neighbours.append(nei_cell)

    def neig_cond(self):                  # Подсчет соседних заполненных клетов
        k = 0
        for i in self.neighbours:
            k += i.condition
        return k
