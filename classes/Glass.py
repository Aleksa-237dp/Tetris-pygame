import pygame as pg

class Glass:
    def __init__(self):
        self.width_cell_amount = 15
        self.height_cell_amount = 15
        self.size_cell = 40

    # обновление сетки игрового поля
    def update_glass(self, grid, shape, x, y, color):
        for row in range(len(shape)):
            for col in range(len(shape[row])):
                if shape[row][col] == 1:
                    grid[y + row][x + col] = color

    # удаление заполненных линий
    def remove_lines(self, grid, glass, color, score, screen):

        full_lines = []
        for row in range(glass.height_cell_amount):
            if all(cell != color['BLACK'] for cell in grid[row]):
                full_lines.append(row)
        for row in full_lines:
            del grid[row]
            grid.insert(0, [color['BLACK']] * glass.width_cell_amount)
            score.change_score(10)
            score.draw_score(screen = screen, glass = glass, color = color['WHITE'])

    # отрисовка игрового поля
    def draw_glass(self, grid, glass, screen, color):
        
        # if len(grid) < glass.height_cell_amount or len(grid[0]) < glass.width_cell_amount:
        #     self.grid = [[0 for _ in range(glass.width_cell_amount)] for _ in range(glass.height_cell_amount)]
        
        for row in range(glass.height_cell_amount):
            for col in range(glass.width_cell_amount):
                pg.draw.rect(screen, grid[row][col], (col * glass.size_cell, row * glass.size_cell, glass.size_cell, glass.size_cell), 1)
        pg.draw.line(screen, color['GREY'], [glass.size_cell * glass.width_cell_amount + 1, 0],
        [glass.size_cell * glass.width_cell_amount + 1, screen.get_height()], 1)
