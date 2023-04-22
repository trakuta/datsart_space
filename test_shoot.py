from api.levels import get_next_level_info, start_next_level, get_current_level_info, finish_current_level
from api.catapult import shoot
from ballista.utils import horizontal_angl
from ballista.aim import ballista_velocity, ballista_power
from ballista.utils import calc_dist
from colors.mixing import mix_paints
from picture.picture import get_pixel_matrix


def fire(p1, p2, m):
    dist = calc_dist(p1, p2)
    v = ballista_velocity(dist)
    p = m * v ** 2 / 2
    return int(p)

def make_shoot(turret_cord, pos, color_):
    color = mix_paints(color_, 10)
    m = sum([color[k] for k in color])
    power = fire(turret_cord, pos, m)
    hor_ang = horizontal_angl(turret_cord, pos)
    shoot(power, color, hor_ang, 45)
 

def turret(image_path):
    targets = get_pixel_matrix(image_path)
    X = len(targets)
    Y = len(targets[0])
    turret_x = X // 2
    turret_y = -300
    turret_cord = (turret_x, turret_y)
    for x in range(0, X, 2):
        for y in range(0, Y, 2):
            if targets[x][y] != 0xffffff:
                make_shoot(turret_cord, (x, y), targets[x][y])


def main():
    turret('images/6.png')
    #finish_current_level()
    #print(get_next_level_info())
    #print(get_current_level_info())
    #start_next_level(6)
    #make_shoot((124, -300), (50, 190), 0xE6B43E)


if __name__ == '__main__':
    main()
