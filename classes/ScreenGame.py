import pygame as pg

class ScreenGame:
    def __init__(self):
        self.width = 800
        self.hеight = 600

        self.screen = pg.display.set_mode((self.width, self.hеight))
        self.caption = pg.display.set_caption('Tetris')