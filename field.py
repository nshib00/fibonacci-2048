from player import Player
import game_math

import random
import itertools


FIELD_SIZE = 4
tiles_range = list(range(FIELD_SIZE))


def generate():
    Player.score = 0
    Player.game_restarted = False
    Player.game_field = [
        [0 for _ in range(4)] for _ in range(4)
    ]

    for _ in range(2):
        randrow, randcol = random.randint(0, 3), random.randint(0, 3)
        Player.game_field[randrow][randcol] = 1

    ones = sum(map(lambda row: row.count(1), Player.game_field))
    if ones == 1:
        Player.game_field[randrow][randcol] = 2

    
def rand_corner():
    return random.choice(
        [
            (0, 0), (0, 1), (0, 2), (0, 3),
            (1, 0), (1, 3), (2, 0), (2, 3),
            (3, 0), (3, 1), (3, 2), (3, 3)
        ]
    )

def get_zeros_indexes_list():
    indexes_list = [(i, j) for i in range(4) for j in range(4)]
    return [(i, j) for i, j in indexes_list if Player.game_field[i][j] == 0]


def make_new_number():
    zero_indexes_list = get_zeros_indexes_list()
    rand_corner = random.choice(zero_indexes_list)
    i, j = rand_corner
    if random.randint(1, 10) == 1:
        Player.game_field[i][j] = 2
    else:
        Player.game_field[i][j] = 1


def horizontal_move_exists():
    for i in range(4):
        for j in range(3):
            if Player.game_field[i][j] == Player.game_field[i][j+1]:
                return True
    return False


def vertical_move_exists():
    for i in range(3):
        for j in range(4):
            if Player.game_field[i][j] == Player.game_field[i+1][j]:
                return True
    return False


def check_overflow(make_number):
    try:
        if make_number or Player.score < 2:
            make_new_number()
    except IndexError:
        Player.save_best_score()
        Player.load_best_score()
        Player.game_over = True


def move_tiles(direction):
    merged = [[False for _ in range(4)] for _ in range(4)]
    make_number = True
    if direction == 'up':
        for i, j in itertools.product(tiles_range, repeat=2):
            shift = 0
            if i > 0:
                for k in range(i):
                    if Player.game_field[k][j] == 0:
                        shift += 1
                if shift > 0:
                    Player.game_field[i-shift][j] = Player.game_field[i][j]
                    Player.game_field[i][j] = 0
                if Player.game_field[i-shift-1][j] == Player.game_field[i-shift][j] and not merged[i-shift-1][j] and not merged[i-shift][j]:
                    Player.game_field[i-shift-1][j] = game_math.increase_tile_value(Player.game_field[i-shift-1][j])
                    Player.score += Player.game_field[i-shift-1][j] 
                    Player.game_field[i-shift][j] = 0
                    merged[i-shift-1][j] = True
        # if not any([merged[0][0], merged[0][1], merged[0][2], merged[0][3]]):
        #     make_number = False

    elif direction == 'down':
        for i, j in itertools.product(tiles_range, repeat=2):
            shift = 0
            if i < 3:
                for k in range(i+1):
                    if Player.game_field[3-k][j] == 0:
                        shift += 1
                if shift > 0:
                    Player.game_field[2-i+shift][j] = Player.game_field[2-i][j]
                    Player.game_field[2-i][j] = 0
                if 3 - i + shift <= 3:
                    if Player.game_field[2-i+shift][j] == Player.game_field[3-i+shift][j] and not merged[2-i+shift][j] and not merged[3-i+shift][j]:
                        Player.game_field[3-i+shift][j] = game_math.mathround(Player.game_field[3-i+shift][j] * game_math.phi)
                        Player.score += Player.game_field[3-i+shift][j]
                        Player.game_field[2-i+shift][j] = 0
                        merged[3-i+shift][j] = True
        # if not any([merged[3][0], merged[3][1], merged[3][2], merged[3][3]]):
        #     make_number = False

    elif direction == 'left':
        for i, j in itertools.product(tiles_range, repeat=2):
            shift = 0
            for k in range(j):
                if Player.game_field[i][k] == 0:
                    shift += 1
            if shift > 0:
                Player.game_field[i][j-shift] = Player.game_field[i][j]
                Player.game_field[i][j] = 0
            if Player.game_field[i][j-shift-1] == Player.game_field[i][j-shift] and not merged[i][j-shift-1] and not merged[i][j-shift]:
                Player.game_field[i][j-shift-1] = game_math.mathround(Player.game_field[i][j-shift-1] * game_math.phi)
                Player.score += Player.game_field[i][j-shift-1]
                Player.game_field[i][j-shift] = 0
                merged[i][j-shift-1] = True
        # if not any([merged[0][0], merged[1][0], merged[2][0], merged[3][0]]):
        #     make_number = False

    elif direction == 'right':
        for i, j in itertools.product(tiles_range, repeat=2):
            shift = 0
            for k in range(j):
                if Player.game_field[i][3-k] == 0:
                    shift += 1
            if shift > 0:
                Player.game_field[i][3-j+shift] = Player.game_field[i][3-j]
                Player.game_field[i][3-j] = 0
            if 4 - j + shift <= 3:
                if Player.game_field[i][4-j+shift] == Player.game_field[i][3-j+shift] and not merged[i][4-j+shift] and not merged[i][3-j+shift]:
                    Player.game_field[i][4-j+shift] = game_math.mathround(Player.game_field[i][4-j+shift] * game_math.phi)
                    Player.score += Player.game_field[i][4-j+shift]
                    Player.game_field[i][3-j+shift] = 0
                    merged[i][4-j+shift] = True
        # if not any([merged[0][3], merged[1][3], merged[2][3], merged[3][3]]):
        #     make_number = False

    # print([m for m in merged], make_number)
    check_overflow(make_number=make_number)
