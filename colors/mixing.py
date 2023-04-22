from api.depot import *


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
    colors = 0
    r = g = b = 0
    for p in paints:
        colors += paints[p]
        tmp = get_rgb(p)
        r += tmp[0] * paint[p]
        g += tmp[1] * paints[p]
        b += tmp[3] * paints[p]
    r //= colors
    g //= colors
    b //= colors
    return (r << 16) ^ (g << 8) ^ b


def search_paint(target, arr: list):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] > target:
            r = mid - 1
        elif arr[mid] < target:
            l = mid + 1
        else:
            return arr[mid]
    return arr[l]


def mix_paints(target_color, max_mix=5):
    paints_list = get_all_paints_remains_list() 
    paints_list = paints_list['response']
    paints_list_keys = sorted(paints_list.keys())

    cur_target = target_color
    cur_color = 0
    print(len(paints_list_keys))
    # for _ in range(max_mix):

