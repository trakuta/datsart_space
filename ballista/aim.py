import math


g = 9.80665  # гравитационная постоянная
pi = 3.1415926535898  # число ПИ
k = 0.001  # уменьшающий коэффициент массы снаряда


def ballista_distance(power):
    v0 = 700  # начальная скорость
    alpha = 30  # угол броска в градусах

    alpha = math.radians(alpha)  # перевод угла в радианы

    t = 2 * v0 * math.sin(alpha) / (g * (1 + k))  # время полета
    R = v0 ** 2 * math.sin(2 * alpha) / g  # дальность полета
    H = v0 ** 2 * (math.sin(alpha)) ** 2 / (2 * g * (1 + k))  # максимальная высота

    print(f"Время полета: {t}")
    print(f"Дальность полета: {R}")
    print(f"Максимальная высота: {H}")


def ballista_velocity(dist, vert_angle=45):

    angle_radians = vert_angle * pi / 180  # переводим в радианы
    v0 = math.sqrt((dist * g * k) / (math.sin(2 * angle_radians)))

    return v0


def ballista_power(mass):
    return mass * ballista_velocity()


def find_initial_velocity(distance, angle):
    angle_rad = math.radians(angle)
    velocity = math.sqrt(distance * g / (math.sin(2 * angle_rad))) * (1 / math.sqrt(1 + k))
    return velocity
