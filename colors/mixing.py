from api.depot import *
from ballista.utils import calc_dist

def get_rgb(color):
    '''
    Получение 8-битных значений RGB из 24-х битного числа  
    '''
    r = color >> 16
    g = (color >> 8) & 0xff
    b = color & 0xff
    return (r, g, b)


def calculate_mixed_color(paints: dict):
    '''
    Смешивание RGB цветов
    '''
    if not paints:
        return 0
    colors = 0
    r = g = b = 0
    for p in paints:
        colors += paints[p]
        tmp = get_rgb(int(p))
        r += tmp[0] * paints[p]
        g += tmp[1] * paints[p]
        b += tmp[2] * paints[p]
    r = int(r / colors)
    g = int(g / colors)
    b = int(b / colors)
    return (r << 16) ^ (g << 8) ^ b


def search_paint(target: int, colors: list):
    min_dist = 2 ** 100
    cur_color = 0
    for color in colors:
        color = int(color)
        dist = calc_dist(get_rgb(target), get_rgb(color))
        if dist < min_dist:
            cur_color = color
            min_dist = dist
    print(dist)
    return cur_color


def get_missing_color(target_color: int, current_color: int,
                      colors_count: int):
    R_t, G_t, B_t = get_rgb(target_color)
    R_c, G_c, B_c = get_rgb(current_color)

    R_m = (colors_count + 1) * R_t - R_c * colors_count
    G_m = (colors_count + 1) * G_t - G_c * colors_count
    B_m = (colors_count + 1) * B_t - B_c * colors_count
    '''
    print(R_t, G_t, B_t)
    print(R_c, G_c, B_c)
    print(R_m, G_m, B_m)
    '''

    return (R_m << 16) ^ (G_m << 8) ^ (B_m)

def mix_paints(target_color: int, max_mix=20):
    paints_list = get_all_paints_remains_list() 
    paints_list = paints_list['response']
    colors = list(sorted(paints_list.keys()))

    paints = dict()
    cur_target = target_color
    for count in range(max_mix):
        cur_color = calculate_mixed_color(paints)
        if cur_color == target_color:
            return paints

        cur_target = get_missing_color(target_color, cur_color, count)
        paint_color = search_paint(cur_target, colors)
        # Сохраняем выбранный цвет
        if paint_color not in paints:
            paints[paint_color] = 1
        else:
            paints[paint_color] += 1

        # Забираем красу со склада 
        if paints_list[str(paint_color)] == 1:
            paints_list.pop(str(paint_color))
            colors.pop(paint_color)
        else:
            paints_list[str(paint_color)] -= 1
    return paints
