import pygame

from classes.ScreenGame import ScreenGame
from classes.Glass import Glass
from classes.ColorsDict import ColorsDict
from classes.Shapes import Shapes
from classes.Score import Score

sg = ScreenGame()
glass = Glass()
cd = ColorsDict()
sh = Shapes()
score = Score()

pygame.init()

# the main game cycle
def run_game():

    grid = [[cd.spec_colors['BLACK']] * glass.width_cell_amount for _ in range(glass.width_cell_amount)]
    shape, color = sh.generate_shape(), cd.generate_color()
    x, y = (glass.width_cell_amount // 2 - len(shape[0]) // 2), 0
    fps = 3
    clock = pygame.time.Clock()
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    rotates_shape = list(zip(*reversed(shape)))
                    if not sh.check_collision(grid = grid, shape = rotates_shape, x = x, y = y, glass = glass, color = cd.spec_colors):
                        shape = rotates_shape
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if not sh.check_collision(grid = grid, shape = shape, x = x - 1, y = y, glass = glass, color = cd.spec_colors):
                x -= 1
        elif keys[pygame.K_RIGHT]:
            if not sh.check_collision(grid = grid, shape = shape, x = x + 1, y = y, glass = glass, color = cd.spec_colors):
                x += 1
        elif keys[pygame.K_DOWN]:
            if not sh.check_collision(grid = grid, shape = shape, x = x, y = y + 1, glass = glass, color = cd.spec_colors):
                y += 1

        if not sh.check_collision(grid = grid, shape = shape, x = x, y = y + 1, glass = glass, color = cd.spec_colors):
            y += 1

        else:
            glass.update_glass(grid = grid, shape = shape, x = x, y = y, color = color)
            glass.remove_lines(grid = grid, glass = glass, color = cd.spec_colors, score = score, screen = sg.screen)
            shape, color = sh.generate_shape(), cd.generate_color()
            x, y = glass.width_cell_amount // 2 - len(shape[0]) // 2, 0
            if sh.check_collision(grid = grid, shape = shape, x = x, y = y, glass = glass, color = cd.spec_colors):
                game_over = True

        sg.screen.fill(cd.spec_colors['BLACK'])
        glass.draw_glass(grid = grid, glass = glass, screen = sg.screen, color = cd.spec_colors)
        sh.draw_shape(shape = shape, x = x, y = y, color = color, screen = sg.screen, glass = glass)
        score.draw_score(screen = sg.screen,  glass = glass, color = cd.spec_colors['WHITE'])
        pygame.display.update()
        clock.tick(fps)

    font = pygame.font.Font(None, 40)
    text = font.render('Game Over', True, cd.spec_colors['WHITE'])
    sg.screen.blit(text, (sg.width // 2 - text.get_width() // 2, sg.hеight // 2 - text.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(3000)
    pygame.quit()

run_game()

