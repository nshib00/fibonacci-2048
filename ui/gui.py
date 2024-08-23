import pygame as pg
from ui import colors, text
from consts import SCREEN_SIZE

from player import Player
import field


def draw_tiles(screen):
    x = 35
    y = 30
    for row in range(4):
        for col in range(4):
            tile_rect = pg.draw.rect(
                screen,
                color=colors.values_and_colors[
                    Player.game_field[row][col]
                ],
                rect=pg.Rect(x, y, 90, 90),
                border_radius=5
            )
            pg.draw.rect(
                screen,
                color=colors.get_tile_border_color(Player.game_field[row][col]),
                rect=pg.Rect(x-2, y-2, 93, 93),
                border_radius=5,
                width=colors.get_tile_border_width(Player.game_field[row][col])
            )
            text.print_tile_value(screen, value=Player.game_field[row][col], rect=tile_rect)
            x += 100
        y += 100
        x = 35


def draw_button(screen, color=colors.LINEN, x=470, y=310, width=140, height=80, border_width=3):
    pg.draw.rect(screen, color, pg.Rect(x, y, width, height), border_radius=5)
    pg.draw.rect(
        screen, 
        colors.BLACK,
        pg.Rect(
            x-border_width,
            y-border_width,
            width+border_width,
            height+border_width,
        ),
        border_radius=5, 
        width=border_width
    )


def draw(screen):
    pg.draw.rect(screen, colors.TAN, pg.Rect(20, 20, 420, 420), border_radius=5)
    menu_rect = pg.draw.rect(screen, colors.TAN, pg.Rect(460, 20, 160, 420), border_radius=5)
    draw_button(screen)
    text.print_menu_text(screen, menu_rect)
    mouse_x, mouse_y = pg.mouse.get_pos()
    if mouse_x in range(470, 611) and mouse_y in range(310, 391):
        draw_button(screen, color=colors.WHITE)
        text.print_restart_button_text(screen)
    draw_tiles(screen)


def show_game_over_window(screen, clock):
    btnx, btny, btnw, btnh = 165, 280, 300, 100

    while True:
        screen.fill(colors.TAN)
        clock.tick(60)
        draw_button(
            screen, 
            x=btnx,
            y=btny,
            width=btnw,
            height=btnh
        )
        text.print_text('Game over!', screen, x=95, y=80, font_size=75)
        last_game_score = str(Player.score)
        text.print_text(f'Your score: {last_game_score}', screen, x=175-3*len(last_game_score), y=170)
        text.print_restart_button_text(screen, x=255, y=310)
        mouse_x, mouse_y = pg.mouse.get_pos()
        if mouse_x in range(btnx, btnx+btnw+1) and mouse_y in range(btny, btny+btnh+1):
            draw_button(screen, x=btnx, y=btny, width=btnw, height=btnh, color=colors.WHITE)
            text.print_restart_button_text(screen, x=255, y=310)
            if pg.mouse.get_pressed()[0]:
                Player.game_over = False
                Player.game_restarted = True
                field.generate()
                break

        pg.display.flip()
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                break