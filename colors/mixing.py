

def mix_paints(paints: dict):
    '''
    Смешивание RGB цветов
    '''
    colors = 0
    r = g = b = 0
    for p in paints:
        colors += paints[p]
        r += (p >> 16) * paints[p]
        g += ((p >> 8) & 0xff) * paints[p]
        b += (p & 0xff) * paints[p]
    r //= colors
    g //= colors
    b //= colors
    return (r << 16) ^ (g << 8) ^ b

rgb = mix_paints({0xff0000: 1, 0x0000ff: 1, 0x00ff00: 1})
