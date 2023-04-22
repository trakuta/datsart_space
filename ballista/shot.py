from aim import ballista_velocity
from utils import calc_dist


def fire(p1, p2):
    dist = calc_dist(p1, p2)
    velocity = ballista_velocity(dist)
    return velocity