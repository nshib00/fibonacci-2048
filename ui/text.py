import pygame as pg

from ui import colors
from player import Player

pg.font.init()

Player.load_best_score()

def print_text(text, screen, x, y, color=colors.BLACK, font_size=40):
    font = pg.font.Font('freesansbold.ttf', font_size)
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, (x, y))


def print_tile_values(screen):
    x = -40
    y = 50
    for row in Player.game_field:
        for tile_value in row:
            value_len = len(str(tile_value)) - 1
            x += 100
            if tile_value > 0:
                print_text(str(tile_value), screen, x+3-5*value_len, y, font_size=60-10*value_len)
        y += 100
        x = -40


def print_tile_value(screen, value, rect):
    value_len = len(str(value)) - 1
    if value in (13, 34, 55, 89, 233):
        valx = rect.centerx-20-10*value_len
        valy = rect.centery-25+2*value_len
    elif value_len + 1 == 4:
        valx = rect.centerx-8-10*value_len
        valy = rect.centery-22+2*value_len
        if value == 4181:
            valx = rect.centerx-6-10*value_len
    else:
        valx = rect.centerx-17-10*value_len
        valy = rect.centery-25+2*value_len
    if value > 0:
        print_text(
            str(value),
            screen,
            x=valx,
            y=valy,
            color=colors.DARK_GRAY,
            font_size=60-8*value_len-3*(value_len//3)
        )


def print_restart_button_text(screen, x=477, y=330):
    print_text('Restart', screen, x=x, y=y, font_size=35)


def print_menu_text(screen, menu_rect):
    score_len = len(str(Player.score))
    best_score_len = len(str(Player.best_score))
    print_text(f'Score:', screen, x=477, y=50)
    print_text(
        str(Player.score), 
        screen,
        x=menu_rect.centerx-20-10*(score_len-1),
        y=100,
        font_size=60-5*score_len+3*score_len//5+3*score_len//6
        )

    print_text(f'Best score:', screen, x=470, y=190, font_size=25)
    if Player.score > int(Player.best_score):
        Player.best_score = Player.score
    print_text(
        str(Player.best_score), 
        screen, 
        x=menu_rect.centerx-20-10*(best_score_len-1)+best_score_len//4, 
        y=230, 
        font_size=60-5*best_score_len+3*best_score_len//5+3*best_score_len//6
    )

    print_restart_button_text(screen)
    print_text('Game by nshib', screen, x=485, y=415, font_size=15)