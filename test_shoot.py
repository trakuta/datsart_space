from api.levels import get_next_level_info, start_next_level, get_current_level_info
from api.catapult import shoot
from ballista.utils import horizontal_angl
from ballista.aim import ballista_velocity, ballista_power
from ballista.utils import calc_dist
from colors.mixing import mix_paints


def fire(p1, p2):
    dist = calc_dist(p1, p2)
    velocity = ballista_power(dist)
    return int(velocity)


def main():

    power = fire((124, -300), (200, 200))
    hor_ang = horizontal_angl((124, -300), (200, 200))
    color = mix_paints(0xE6B43E, 10)
    shoot(power, color, hor_ang, 45)
    print(color)
    print(get_current_level_info())


if __name__ == '__main__':
    main()
