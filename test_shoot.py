from api.levels import get_next_level_info, start_next_level, get_current_level_info, finish_current_level
from api.catapult import shoot
from ballista.utils import horizontal_angl
from ballista.aim import ballista_velocity, ballista_power
from ballista.utils import calc_dist
from colors.mixing import mix_paints
from picture.picture import get_pixel_matrix
from api.catapult import post_req
import threading
import requests
import json


def fire(p1, p2, m):
    dist = calc_dist(p1, p2)
    v = ballista_velocity(dist)
    p = (m * v ** 2) / 2
    return int(p)

def make_shoot(turret_cord, pos, color_):
    color = mix_paints(color_, 10)
    m = sum([color[k] for k in color])
    power = fire(turret_cord, pos, m)
    hor_ang = horizontal_angl(turret_cord, pos)
    shoot(power, color, hor_ang, 45)
 

def turret(image_path, step):
    targets = get_pixel_matrix(image_path)
    X = len(targets)
    Y = len(targets[0])
    turret_x = X // 2
    turret_y = -300
    turret_cord = (turret_x, turret_y)
    for x in range(0, X, step):
        for y in range(0,  Y, step):
            if targets[x][y] != 0xffffff:
                make_shoot(turret_cord, (x, y),
                           targets[x][y])

def send_post():
    while True:
        while post_req.qsize() == 0:
            pass
        url, headers, body = post_req.get()
        ans = requests.post(url, headers=headers, data=body)
        if ans.status_code == 200:
            print('+')
            ans = json.loads(ans.text)
        else:
            print(ans.text)
 


def main():
    for i in range(1, 21):
        my_thread = threading.Thread(target=turret, args=('images/7.png', i))
        my_thread.start()
    for i in range(10):
        my_thread = threading.Thread(target=send_post)
        my_thread.start()
    # turret('images/6.png')
    #finish_current_level()
    #print(get_next_level_info())
    #print(get_current_level_info())
    #start_next_level(6)
    #make_shoot((124, -300), (50, 190), 0xE6B43E)


if __name__ == '__main__':
    main()
