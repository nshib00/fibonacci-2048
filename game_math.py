from math import sqrt


phi = (sqrt(5) + 1) / 2


def mathround(num): # если дробная часть не меньше 0,5 - округляет в большую сторону, в противном случае - в меньшую.
    if num - int(num) >= 0.5:
        return int(num) + 1
    return int(num)


def increase_tile_value(curr_value):
    return mathround(curr_value * phi)
