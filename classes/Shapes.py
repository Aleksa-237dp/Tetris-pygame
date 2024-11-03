import random
import pygame as pg

class Shapes:
    def __init__(self):
        self.shapes = [
                        [[1, 1, 1, 1]],
                        [[1, 1],
                         [1, 1]],
                        [[1, 1, 0],
                         [0, 1, 1]],
                        [[0, 1, 1],
                         [1, 1, 0]],
                        [[1, 1, 1],
                         [0, 1, 0]],
                        [[1, 1, 1],
                         [1, 0, 0]],
                        [[1, 1, 1],
                         [0, 0, 1]]]

        self.shape = None

    # генерация новой фигуры
    def generate_shape(self):
        self.shape = self.shapes[random.randint(0, len(self.shapes) - 1)]
        return self.shape

    # отрисовка текущей фигуры
    def draw_shape(self, shape, x, y, color, screen, glass):
        for row in range(len(shape)):
            for col in range(len(shape[row])):
                if shape[row][col] == 1:
                    pg.draw.rect(screen, color, ((x + col) * (glass.size_cell), (y + row) * glass.size_cell, 
                                glass.size_cell, glass.size_cell), 1)

    # проверка возможности размещения фигуры в данном положении
    def check_collision(self, grid, shape, x, y, glass, color):
        for row in range(len(shape)):
            for col in range(len(shape[row])):
                if shape[row][col] == 1:
                    if x + col < 0 or x + col >= glass.width_cell_amount or y + row >= glass.height_cell_amount or grid[y + row][x + col] != color['BLACK']:
                        return True
                  
        return False






