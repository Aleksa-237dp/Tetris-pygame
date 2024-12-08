import random

class ColorsDict:
    def __init__(self):
        self.colors = {'RED': (255, 0, 0),
                       'GREEN': (0, 255, 0),
                       'BLUE': (0, 0, 255),
                       'YELLOW': (255, 255, 0),
                       'CYAN': (0, 255, 255),
                       'MAGENTA': (255, 0, 255),
                       'ORANGE': (255, 165, 0), }
        self.spec_colors = {'BLACK': (0, 0, 0),
                            'GREY': (128, 128, 128),
                            'WHITE': (255, 255, 255), }

    # color generation
    def generate_color(self):
        self.color = self.colors[random.choice(list(self.colors.keys()))]
        return self.color
    
