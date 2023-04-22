import math


def calc_dist(p1, p2):
    return sum([(p1[i] - p2[i]) ** 2 for i in range(len(p1))]) ** 0.5


def horizontal_angl(canon: tuple, aim: tuple):
    if canon[0] == aim[0]:
        return 0
    elif canon[0] > aim[0]:
        a = canon[0] - aim[0]
    elif canon[0] < aim[0]:
        a = aim[0] - canon[0]
    b = math.fabs(canon[1]) + aim[1]
    angle_rad = math.atan(a/b)
    angl_degr = math.degrees(angle_rad)

    if canon[0] > aim[0]:
        return -angl_degr
    elif canon[0] < aim[0]:
        return angl_degr


if __name__ == '__main__':
    '''
    print(calc_dist((0, 0), (2, 1)))
    cos = (0 * 2 + 0 * 1) / calc_dist
    '''
    print(horizontal_angl((125, -300), (100, 200)))
