import pygame as pg

class Score:
    def __init__(self):
        self.score = 0

    def change_score(self, scores):
        self.score += scores

    # отрисовка очков
    def draw_score(self, screen, glass, color):
        font = pg.font.Font(None, 40)

        text = font.render('Счёт: ' + str(self.score), True, color)
        screen.blit(text, (glass.size_cell * glass.width_cell_amount +
                           (screen.get_width()- glass.size_cell * glass.width_cell_amount) // 10, 100))




