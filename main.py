import pygame as pg
import sys

import ui.colors as colors
from ui import gui
import consts
import field
from player import Player


pg.init()
pg.display.init()

screen = pg.display.set_mode(consts.SCREEN_SIZE)
pg.display.set_caption('Fibonacci 2048')
icon = pg.image.load('images/icon.ico')
pg.display.set_icon(icon)
clock = pg.time.Clock()

field.generate()


while True:
    clock.tick(consts.FPS)
    screen.fill(colors.LINEN)
    gui.draw(screen)
    pg.display.flip()
    pg.display.update()
    mouse_x, mouse_y = pg.mouse.get_pos()

    if Player.game_over:
        gui.show_game_over_window(screen, clock)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            Player.save_best_score()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1: # если нажата левая кнопка мыши
                if mouse_x in range(470, 611) and mouse_y in range(310, 391) and not Player.game_restarted:
                    Player.game_restarted = True
                    field.generate()          
        elif event.type == pg.KEYDOWN:
            if event.key in (pg.K_UP, pg.K_w):
                field.move_tiles('up')
            elif event.key in (pg.K_DOWN, pg.K_s):
                field.move_tiles('down')
            elif event.key in (pg.K_LEFT, pg.K_a):
                field.move_tiles('left')
            elif event.key in (pg.K_RIGHT, pg.K_d):
                field.move_tiles('right')
            