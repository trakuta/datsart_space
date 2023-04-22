from api.levels import get_next_level_info, start_next_level, get_current_level_info
from api.catapult import shoot
from ballista.utils import horizontal_angl
from ballista.aim import ballista_velocity
from ballista.utils import calc_dist


def fire(p1, p2):
    dist = calc_dist(p1, p2)
    velocity = ballista_velocity(dist)
    return int(velocity)

def turret(image_path):
    targets = get_pixel_matrix(image_path)
    X = len(targets)
    Y = len(targets[0])
    turret_x = X // 2
    turret_y = -300
    turret_cord = (turret_x, turret_y)
    for x in range(X):
        for y in range(Y):
            if targets[x][y] ! = 0xffffff:
                power = fire(turret_y, (x, y))
                hor_ang = horizontal_angl(turret_cord, (x, y))
                color = targets[x][y] 
                shoot(power, color, hor_ang, 45)





def main():
    power = fire((124, -300), (215, 125))
    hor_ang = horizontal_angl((124, -300), (215, 125))
    color = {'197395': 1}
    shoot(power, color, hor_ang, 45)


if __name__ == '__main__':
    main()
