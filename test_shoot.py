from api.levels import get_next_level_info, start_next_level, get_current_level_info
from api.catapult import shoot
from ballista.utils import horizontal_angl
from ballista.aim import ballista_velocity
from ballista.utils import calc_dist
from colors.mixing import mix_paints


def fire(p1, p2):
    dist = calc_dist(p1, p2)
    velocity = ballista_velocity(dist)
    return int(velocity)


def main():
    power = fire((124, -300), (215, 125))
    hor_ang = horizontal_angl((124, -300), (215, 125))
    color = mix_paints(197395, 1)
    shoot(power, color, hor_ang, 45)


if __name__ == '__main__':
    main()
