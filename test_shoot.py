from api.levels import get_next_level_info, start_next_level, get_current_level_info
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
    for x in range(X):
        for y in range(Y):
            if targets[x][y] != 0xffffff:
                make_shoot(turret_cord, (x, y), targets[x][y])


def main():
    # turret('images/1.jpg')
    make_shoot((124, -300), (200, 125), 0xE6B43E)


if __name__ == '__main__':
    main()
